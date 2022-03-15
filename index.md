---
title: Informations et cours
toc: true
---

[comment]: <> "LTeX: language=fr"

## Nouvelles

- **2022-03-07** pas de cours le mardi 08/03/2022.
- **2022-01-24** un [espace sur Cours en
  Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7694) a été créé. **Il ne
  contiendra rien de plus qu'un lien vers la page où vous vous trouvez**, mais vous pouvez y déposer
  vos exercices hebdomadaires pour une gestion plus pratique. La clé d'accès est `rossum`.
- **2022-01-20** l'exercice 4 des slides « IO et variables » a été mis à jour pour corriger une
  erreur. Si vous avez déjà résolu l'ancienne version, ne changez rien, mais sinon faites plutôt la
  nouvelle.

## Infos pratiques

- **Quoi** « Apprendre à programmer », 4L6SC01P
- **Où** Salle R05, bâtiment Ricœur, Université Paris Nanterre, 200 avenue de la République,
  Nanterre
- **Quand** 12 séances, les mardis de 10:30 à 12:30, du 17/01 au 18/04
  - Voir [le calendrier de
    l'université](https://etudiants.parisnanterre.fr/calendrier-universitaire-2021-2022-1018180.kjsp)
    pour les dates de vacances.
- **Contact** Loïc Grobol [`<lgrobol@parisnanterre.fr>`](mailto:lgrobol@parisnanterre.fr)
- **Dépôt des exercices** de préférence [sur Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7694) (clé d'inscription `rossum`)
  ou par email (voir ci-dessus.)

## Séances

**ATTENTION** : Les liens hypertextes ci-dessous mènent vers des versions statiques des notebooks.
C'est pratique en cas de problème, mais pour suivre le cours et faire les exercices, il faut ouvrir
les versions interactives sur Binder.

<strong>Pour ouvrir les versions interactives, cliquez sur les boutons ![Launch in Binder
  badge](https://mybinder.org/badge_logo.svg)</strong>.

Une fois dans Binder, vous pouvez récupérer votre travail sous forme de fichier ipynb dans le menu
`File` →  `Download as` → `Notebook (ipynb)` et vous pouvez ouvrir un fichier ipynb qui est votre
machine avec `File` → `Open…` → `Upload` (en haut à droite) → `Upload` (à côté du nom de fichier).

Vous pouvez aussi les télécharger sous forme de fichier `.py` pour les ouvrir sur votre machine (par
exemple avec Thonny).

Une autre option, si vous avez un compte Google est d'utiliser
[Colaboratory](https://colab.research.google.com/) pour éditer les notebooks que vous avez
téléchargé.

### 2022-01-17 : Introduction, entrées/sorties de bases et variables

- {% notebook_badges slides/00-introduction/introduction-slides.py.md %}
  [Slides Introduction](slides/00-introduction/introduction-slides.py.html)
- {% notebook_badges slides/01-IO_variables_chaines/io_variables_chaines.py.md %}
  [Slides IO et variables](slides/01-IO_variables_chaines/io_variables_chaines.py.html)

À rendre pour la prochaine fois : exercices du notebook « IO et variables ».

Installer aussi l'environnement [Thonny](https://thonny.org).

Pour installer Thonny sous ChromeOS, c'est [un peu plus
sophistiqué](https://boldidea.org/static/thonny/chromebook.html), mais c'est possible.

Pour les tablettes sous iOS ou Android, ça ne sera pas possible. Vous devriez pouvoir suivre
l'essentiel du cours avec [`repl.it`](https://repl.it), mais ce n'est pas idéal, tenez-moi au
courant si vous n'avez pas le choix et je ferai de mon mieux pour vous permettre de suivre.

### 2022-01-24 : Dessiner avec `turtle` et instructions conditionnelles

- {% notebook_badges slides/01-IO_variables_chaines/corrections.py.md %}
  [Corrections des exercices](slides/01-IO_variables_chaines/corrections.py.html)
- {% notebook_badges slides/02-turtle/turtle.py.md %}
  [Slides Turtle](slides/02-turtle/turtle.py.html)
- {% notebook_badges slides/03-conditions/conditions.py.md %}
  [Slides instructions conditionnelles](slides/03-conditions/conditions.py.html)

À rendre pour la prochaine fois : exercices du notebook « instructions conditionnelles », attention
le mode de rendu change légèrement.

### 2022-02-01 : Indices, listes et boucle `for`

- {% notebook_badges slides/03-conditions/corrections.py.md %}
  [Corrections des exercices](slides/03-conditions/corrections.py.html)
- {% notebook_badges slides/04-index_listes_iter/index_listes_iter.py.md %}
  [Slides indices, listes et itération](slides/04-index_listes_iter/index_listes_iter.py.html)

À rendre pour la prochaine fois : entraînement 🛠️ et exercices dans le notebook « Indexation, listes
et itération ».

### 2022-02-08 : Exercices et compléments sur les boucles

- {% notebook_badges slides/04-index_listes_iter/corrections.md %}
  [Corrections des exercices](slides/04-index_listes_iter/corrections.py.html)
- {% notebook_badges slides/05-td_while/td_while.py.md %}
  [Slides exercices et compléments sur les boucles](slides/05-td_while/td_while.py.html)

### 2022-02-15 : Récapitulatif

Résumé des épisodes précédents, avec **plein** d'exos.

- {% notebook_badges slides/06-recapitulatif/recapitulatif.py.md %}
[Notebook récapitulatif](slides/06-recapitulatif/recapitulatif.py.html)

À rendre pour la prochaine fois : les exercices du notebook.

### 2022-02-21 : Compléments sur les boucles et les séquences

- {% notebook_badges slides/05-td_while/corrections.py.md %}
  [Corrections slides exercices et compléments sur les
  boucles](slides/05-td_while/corrections.py.html)
- {% notebook_badges slides/06-recapitulatif/corrections.py.md %}
  [Corrections exos récapitulatifs](slides/06-recapitulatif/corrections.py.html)
- {% notebook_badges slides/07-complements_boucles_sequences/complements_boucles_sequences.py.md %}
  [Slides compléments boucles et
  séquences](slides/07-complements_boucles_sequences/complements_boucles_sequences.py.html)

### 2022-03-08 : Pas de cours

### 2022-03-15 : Manipulations de chaînes, itérables composites et dictionnaires

- {% notebook_badges slides/07-complements_boucles_sequences/corrections.md %}
  [Corrections exercices ompléments sur les boucles et les séquences](slides/07-complements_boucles_sequences/corrections.py.html)
- {% notebook_badges slides/08-iterables_dictionnaires/iterables_dictionnaires.py.md %}
  [Slides itérables composites et dictionnaires](slides/08-iterables_dictionnaires/iterables_dictionnaires.py.html)


## Ressources

- [Le dépôt Github du cours](https://github.com/LoicGrobol/apprendre-programmer/) contient toutes
  les sources permettant de générer le matériel du cours.

### Python général

Il y a beaucoup, beaucoup de ressources disponibles pour apprendre Python. Ce qui suit n'est qu'une
sélection.

#### Livres

- *How to think like a computer scientist*, Jeffrey Elkner, Allen B. Downey, et Chris Meyers. Vous
  pouvez l'acheter. Vous pouvez aussi le lire
  [ici](http://openbookproject.net/thinkcs/python/english3e/)
- *Dive into Python*, Mark Pilgrim. [Ici](http://www.diveintopython3.net/) vous pouvez le lire ou
  télécharger le pdf.
- *Learning Python*, Mark Lutz.
- *Beginning Python*, Magnus Lie Hetland.
- *Python Algorithms: Mastering Basic Algorithms in the Python Language*, Magnus Lie Hetland.
  Peut-être un peu costaud pour des débutants.
- *Programmation Efficace. Les 128 Algorithmes Qu'Il Faut Avoir Compris et Codés en Python au Cours
  de sa Vie*, Christoph Dürr et Jill-Jênn Vie. Si le cours vous paraît trop facile. Le code Python
  est clair, les difficultés sont commentées. Les algos sont très costauds.

#### Web

Il vous est vivement conseillé d'utiliser un (ou plus) des sites et tutoriels ci-dessous.

- [Real Python](https://realpython.com), des cours et des tutoriels souvent de très bonne qualité et
  pour tous niveaux.
- [Coding Game](https://www.codingame.com/home). Vous le retrouverez dans les exercices
  hebdomadaires.
- [Code Academy](https://www.codecademy.com/fr/learn/python)
- [newcoder.io](http://newcoder.io/). Des projets commentés, commencer par 'Data Visualization'
- [Google's Python Class](https://developers.google.com/edu/python/). Guido a travaillé chez eux.
  Pas [ce
  Guido](http://vignette2.wikia.nocookie.net/pixar/images/1/10/Guido.png/revision/latest?cb=20140314012724),
  [celui-là](https://en.wikipedia.org/wiki/Guido_van_Rossum#/media/File:Guido_van_Rossum_OSCON_2006.jpg)
- [Mooc Python](https://www.fun-mooc.fr/courses/inria/41001S03/session03/about#). Un mooc de
  l'INRIA, carré.
- [Code combat](https://codecombat.com/)

### Divers

- La chaîne YouTube [3blue1brown](https://www.youtube.com/c/3blue1brown) pour des vidéos de maths
  générales.
- La chaîne YouTube de [Freya Holmér](https://www.youtube.com/c/Acegikmo) plutôt orientée *game
  design*, mais avec d'excellentes vidéos de géométrie computationnelle.

## Licences

[![CC BY Licence
badge](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

Copyright © 2022 Loïc Grobol [\<loic.grobol@gmail.com\>](mailto:loic.grobol@gmail.com)

Sauf indication contraire, les fichiers présents dans ce dépôt sont distribués selon les termes de
la licence [Creative Commons Attribution 4.0
International](https://creativecommons.org/licenses/by/4.0/). Voir [le README](README.md#Licences)
pour plus de détails.

 Un résumé simplifié de cette licence est disponible à
 <https://creativecommons.org/licenses/by/4.0/>.

 Le texte intégral de cette licence est disponible à
 <https://creativecommons.org/licenses/by/4.0/legalcode>
