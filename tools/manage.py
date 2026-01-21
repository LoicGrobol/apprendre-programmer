import functools
import os.path
import pathlib
import shutil
import subprocess
import sys
from typing import Any

import click
import jinja2 as j2
import pathspec
import tomllib
import yaml
from jinja2.loaders import FileSystemLoader
from livereload import Server
from markdown_it import MarkdownIt
from markdown_it.renderer import RendererHTML
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.front_matter import front_matter_plugin


# TODO: uuuuuuglyyyyy
def render_md(
    source_file: pathlib.Path,
    environment: j2.Environment,
    context: dict[str, Any] | None = None,
) -> tuple[str, str | None]:
    if context is None:
        context = {}

    layout = context.get("default_layout", "default")

    # Ridiculous
    inner_template = j2.Environment(
        loader=FileSystemLoader(source_file.parent),
        autoescape=j2.select_autoescape(),
        auto_reload=False,
    ).get_template(source_file.name)
    markdown_content = inner_template.render(context)
    md = (
        MarkdownIt("commonmark", renderer_cls=RendererHTML)
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .enable("table")
    )
    tokens = md.parse(markdown_content)
    if tokens[0].type == "front_matter":
        front_matter = yaml.safe_load(tokens[0].content)
        context["page"] = front_matter
        layout = front_matter.get("layout", layout)
        permalink = front_matter.get("permalink")
    else:
        permalink = None

    outer_template = environment.get_template(f"{layout}.html")
    content = md.render(markdown_content)
    return outer_template.render({**context, "content": content}), permalink


def _build_site(
    build_dir: pathlib.Path,
    source_dir: pathlib.Path,
    config_overrides: dict[str, Any] | None = None,
):
    with (source_dir / "config.toml").open("rb") as in_stream:
        config = tomllib.load(in_stream)

    if config_overrides is not None:
        config.update(config_overrides)

    context = {"site": config}

    env = j2.Environment(
        loader=FileSystemLoader(source_dir / "templates"),
        autoescape=j2.select_autoescape(),
        auto_reload=False,
    )

    contents_dir = source_dir / "contents"
    for f in contents_dir.glob("**/*.md"):
        content, permalink = render_md(source_file=f, environment=env, context=context)
        if permalink is None:
            target = build_dir / f.relative_to(contents_dir)
        else:
            if permalink.endswith("/"):
                permalink = f"{permalink}/index.html"
            if permalink.startswith("/"):
                target = build_dir / permalink[1:]
            else:
                target = build_dir / f.parent.relative_to(contents_dir) / permalink
        print(f"{f} → {target}", file=sys.stderr)
        target.write_text(content)


def _build_jl(build_dir: pathlib.Path, jupyterlite_dir: pathlib.Path, notebooks_dir: pathlib.Path):
    notebooks_target_dir = build_dir / "notebooks"
    notebooks_target_dir.mkdir(exist_ok=True)

    for d in notebooks_dir.glob("*/"):
        shutil.copytree(d, notebooks_target_dir / d.name, dirs_exist_ok=True)

    subprocess.run(  # noqa: S603
        [  # noqa: S607
            "jupytext",
            "--to",
            "ipynb",
            *notebooks_target_dir.glob("**/*.py.md"),
        ]
    )
    subprocess.run(  # noqa: S603
        [  # noqa: S607
            "jupyter",
            "lite",
            "build",
            "--contents",
            str(build_dir / "notebooks"),
            "--lite-dir",
            jupyterlite_dir,
            "--output-dir",
            str(build_dir / "jupyterlite"),
        ],
        cwd=build_dir,
    )
    # JupyterLite stop polluting my build dir >:[
    (build_dir / ".jupyterlite.doit.db").unlink()


def _build(
    build_dir: pathlib.Path,
    source_dir: pathlib.Path,
    config_overrides: dict[str, Any] | None = None,
    jl: bool = False,
):
    build_dir = build_dir.resolve()
    build_dir.mkdir(exist_ok=True, parents=True)
    source_dir = source_dir.resolve()

    _build_site(
        build_dir=build_dir,
        config_overrides=config_overrides,
        source_dir=source_dir / "site",
    )
    if not jl:
        _build_jl(
            build_dir=build_dir,
            jupyterlite_dir=source_dir / "jupyterlite",
            notebooks_dir=source_dir / "notebooks",
        )


def get_all_gitignores(base_dir: pathlib.Path) -> tuple[list[str], list[pathlib.Path]]:
    # First try to find a .git
    root = base_dir.resolve()
    while not (root / ".git").exists():
        # Filesystem root: abort mission
        if root.parent == root:
            root = base_dir
            break
        root = root.parent
    gitignores = list(root.glob("**/*.gitignore"))
    patterns = []
    for f in gitignores:
        prefix = str(f.parent.relative_to(root))
        with f.open() as in_stream:
            for p in in_stream:
                if p and not p.isspace() and not p.startswith("#"):
                    patterns.append(os.path.join(prefix, p.strip()))  # noqa: PTH118
    return patterns, gitignores


@click.group()
def cli():
    pass


@cli.command(help="Build the site")
@click.argument(
    "source_dir",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--build-dir",
    default=pathlib.Path.cwd() / "_build",
    show_default=True,
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
@click.option("--jl / --no-jl", default=True)
def build(build_dir: pathlib.Path, jl: bool, source_dir: pathlib.Path):
    _build(build_dir=build_dir, jl=jl, source_dir=source_dir)


@cli.command(help="Watch and serve the site")
@click.argument(
    "source_dir",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--build-dir",
    default=pathlib.Path.cwd() / "_build",
    show_default=True,
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
@click.option("--port", default=5000, show_default=True, type=int)
@click.option(
    "--watch / --no-watch",
    default=False,
)
def serve(build_dir: pathlib.Path, port: int, source_dir: pathlib.Path, watch: bool):
    ignore_patterns, gitignores = get_all_gitignores(source_dir)
    if ignore_patterns:
        ps = pathspec.PathSpec.from_lines("gitwildmatch", ignore_patterns)
        # TODO: update these when gitignores themselves change?

        ignore = ps.match_file
    else:
        ignore = None

    cmd = functools.partial(
        _build,
        build_dir=build_dir,
        source_dir=source_dir,
        config_overrides={"url": f"http://localhost:{port}"},
    )
    cmd()
    server = Server()
    # TODO: doesn't seem to work because liverload is passing full paths and pathspec is expecting
    # paths relative to the repo root
    if watch:
        server.watch(source_dir, cmd, delay=2, ignore=ignore)
    server.serve(root=build_dir)


@cli.command(help="Cleanup build files etc.")
@click.argument(
    "source_dir",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--build-dir",
    default=pathlib.Path.cwd() / "_build",
    show_default=True,
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
def clean(build_dir: pathlib.Path, source_dir: pathlib.Path):
    for p in [build_dir]:
        if p == source_dir:
            raise ValueError(f"Attempting to clean source dir {source_dir}")
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
        else:
            print(f"File not found for cleanup: {p}", file=sys.stderr)


if __name__ == "__main__":
    cli()
