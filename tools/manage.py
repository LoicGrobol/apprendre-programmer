import functools
import os.path
import pathlib
import shutil
import subprocess
import sys

import click
import pathspec
from livereload import Server


def _build(build_dir: pathlib.Path, source_dir: pathlib.Path):
    build_dir = build_dir.resolve()
    build_dir.mkdir(exist_ok=True, parents=True)
    source_dir = source_dir.resolve()

    notebooks_target_dir = build_dir / "notebooks"
    notebooks_target_dir.mkdir(exist_ok=True)
    for d in (source_dir / "slides").glob("*/"):
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
            str(source_dir / "_jupyterlsite"),
            "--output-dir",
            str(build_dir / "jupyterlite"),
        ],
        cwd=build_dir,
    )
    shutil.copytree(
        build_dir / "jupyterlite", source_dir / "_site" / "jupyterlite", dirs_exist_ok=True
    )
    shutil.copytree(
        build_dir / "notebooks", source_dir / "_site" / "notebooks", dirs_exist_ok=True
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


@cli.command(help="Serve the site")
@click.argument(
    "build_dir",
    default=pathlib.Path.cwd() / "_build",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
def serve(build_dir: pathlib.Path):
    server = Server()
    server.serve(root=build_dir)


@cli.command(help="Build the site")
@click.argument(
    "source_dir",
    default=pathlib.Path.cwd(),
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--build-dir",
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
def build(build_dir: pathlib.Path | None, source_dir: pathlib.Path):
    if build_dir is None:
        build_dir = source_dir / "_build"
    _build(build_dir=build_dir, source_dir=source_dir)


@cli.command(help="Watch and serve the site")
@click.argument(
    "source_dir",
    default=pathlib.Path.cwd(),
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--build-dir",
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
def watch(build_dir: pathlib.Path | None, source_dir: pathlib.Path):
    if build_dir is None:
        build_dir = source_dir / "_build"
    ignore_patterns, gitignores = get_all_gitignores(source_dir)
    if ignore_patterns:
        ps = pathspec.PathSpec.from_lines("gitwildmatch", ignore_patterns)
        # TODO: update these when gitignores themselves change?

        ignore = ps.match_file
    else:
        ignore = None

    cmd = functools.partial(_build, build_dir=build_dir, source_dir=source_dir)
    cmd()
    server = Server()
    # TODO: doesn't seem to work because liverload is passing full paths and pathspec is expecting
    # paths relative to the repo root
    server.watch(source_dir, cmd, delay=2, ignore=ignore)
    server.serve(root=build_dir)


@cli.command(help="Cleanup build files etc.")
@click.argument(
    "source_dir",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--build-dir",
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
def clean(build_dir: pathlib.Path | None, source_dir: pathlib.Path):
    if build_dir is None:
        build_dir = source_dir / "_build"
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
