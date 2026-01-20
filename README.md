<!-- LTeX: language=fr -->

Apprendre à programmer
======================

[![Licence : CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)

Contenus pour le cours « Apprendre à programmer » de la L3 SDL, parcours LCN, Université Paris
Nanterre.


- [Site du cours](https://loicgrobol.github.io/apprendre-programmer/)
- [Dépôt GitHub](https://github.com/LoicGrobol/apprendre-programmer)

Contact : [<loic.grobol@parisnanterre.fr>](mailto:loic.grobol@parisnanterre.fr)

## Développement

Pour travailler au développement de ce cours :

1. Créer un environnement virtuel et l'activer
2. Installer les dépendances

   ```bash
   pip install -U -r requirements.txt
   ```

3. Démarrer jupyter

   ```bash
   jupyter notebook
   ```

   Idéalement ça devrait aussi marcher avec jupyterlab
4. On peut alors modifier les fichiers markdown dans jupyter comme si c'étaient des notebooks grâce
   à la magie de [jupytext](https://github.com/mwouts/jupytext)

Autres éléments magiques :

- On peut ouvrir les notebooks en md sur Binder grâce au [postBuild](postBuild) qui dit de compiler
  l'extension jupytext. Par contre, le build initial de l'image est assez lent. (même avec
  `--minimize=False` qui [accélère un
  peu](https://github.com/jupyterlab/jupyterlab/issues/4824#issuecomment-697188390))
- Les badges « open in binder » sont générés avec le tag Liquid `{% notebook_badges
  chemin/du/notebook %}`.
  - Voir [`_plugins/notebooks.rb`](_plugins/notebooks.rb) pour comprendre comment ça marche.
  - Utilise les variables `site.{baseurl,repository,repo_branch}` définies dans
    [`_config.yml`](config.yml).

## Générer le site en local

Penser à activer asdf si besoin

Dependencies:

- Ruby
- Bundle

Setup:

```console
gem install jekyll bundler
bundle config set --local path 'vendor/bundle'
bundle install
```

Regenerate:

```bash
pyton tools/manage.py build
bundle exec jekyll build
bundle exec jekyll serve
```

Astuce pour les pages : Jekyll n'est pas très bon pour les pages qui ne sont pas des postes de blog,
les ajouter dans `_pages` (ce qui fonctionne parce qu'on l'a mis dans `_config.yml`)- et leur donner
un `permalink` dans le header.

## Binder

(En cours)

Pour accélérer le lancement des notebooks dans Binder, on utilise [un repo d'environnement
](https://github.com/LoicGrobol/apprendre-programmer-environ) différent (l'idée est que comme ce
repo change rarement, il y a rarement besoin de reconstruire l'image pour Binder). Il faut penser à
le mettre à jour quand on change les dépendances ici **tout en lui laissant `nbgitpuller`**.

## Licences

[![CC BY Licence
badge](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

Copyright © 2025 L. Grobol [\<lgrobol@tuta.com\>](mailto:lgrobol@tuta.com)

Sauf indication contraire, les fichiers présents dans ce dépôt sont distribués selon les termes de
la licence [Creative Commons Attribution 4.0
International](https://creativecommons.org/licenses/by/4.0/).

Un résumé simplifié de cette licence est disponible à
<https://creativecommons.org/licenses/by/4.0/>.

Le texte intégral de cette licence est disponible à
<https://creativecommons.org/licenses/by/4.0/legalcode>
