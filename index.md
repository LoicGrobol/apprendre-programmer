---
title: Informations et cours
layout: default
---

<!-- LTeX: language=fr" -->


## Nouvelles

- **2025-01-20** Premier cours de cette session le mardi 21 janvier 2025. *Be there and beware!*


## Infos pratiques

- **Quoi** « Apprendre à programmer », 4L6SC01P
- **Où** Salle L209, bâtiment Ricœur, Université Paris Nanterre, 200 avenue de la République,
  Nanterre
- **Quand** 12 séances, les mardis de 10:30 à 12:30, du 21/01 au 15/04
  - Voir le calendrier de l'université pour les dates de vacances.
- **Contact** Loïc Grobol [`<lgrobol@parisnanterre.fr>`](mailto:lgrobol@parisnanterre.fr)
- **Dépôt des exercices** de préférence sur [Cours en
  Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7736) (à venir) (clé d'inscription
  `rossum`) ou par email (voir ci-dessus.)

## Liens utiles

- Prendre rendez-vous pour des *office hours* en visio : [mon
  calendrier](https://calendar.app.google/N9oW2c9BzhXsWrrv9)
- [Espace Cours en Ligne](](https://coursenligne.parisnanterre.fr/course/view.php?id=7736))
  - Inscription libre avec la clé `rossum`
  - Attention, cet espace ne sert qu'aux dépôts de devoirs.
- [Page du cours de l'an dernier]({{site.url}}{{site.baseurl}}/2024)
- [Le dépôt Github du cours](https://github.com/LoicGrobol/apprendre-programmer/) contient toutes
  les sources permettant de générer le matériel du cours.
- Lien Binder de secours :
  [![Binder]({{site.binder_host}}/badge_logo.svg)]({{site.binder_host}}/v2/gh/LoicGrobol/apprendre-programmer/main)


## Séances

<!-- **ATTENTION** : Les liens hypertextes ci-dessous mènent vers des versions statiques des notebooks.
C'est pratique en cas de problème, mais pour suivre le cours et faire les exercices, il faut ouvrir
les versions interactives sur Binder.

<strong>Pour ouvrir les versions interactives, cliquez sur les boutons ![Launch in Binder
  badge](https://mybinder.org/badge_logo.svg)</strong>.

Une fois dans Binder, vous pouvez récupérer votre travail sous forme de fichier ipynb dans le menu
`File` →  `Download as` → `Notebook (ipynb)` et vous pouvez ouvrir un fichier ipynb qui est votre
machine avec `File` → `Open…` → `Upload` (en haut à droite) → `Upload` (à côté du nom de fichier). -->

Pour utiliser un notebook :

- Télécharger le fichier notebook (`.ipynb`) en cliquant sur le lien.
- Ouvrir [Basthon](https://notebook.basthon.fr/).
- Charger le notebook dans Basthon (`Fichier` → `Ouvrir`).
- Faites-y ce que vous avez à faire :-)
- Vous pouvez ensuite télécharger le notebook avec vos modifications (`Fichier` → `Enregistrer
  Sous`).

Vous pouvez aussi les télécharger pour les ouvrir sous votre machine, dans
[Edupyter](https://www.edupyter.net/) ou [Visual Studio Code](https://code.visualstudio.com/).

Une autre option, si vous avez un compte Google est d'utiliser
[Colaboratory](https://colab.research.google.com/) pour éditer les notebooks que vous avez
téléchargé.

### 2025-01-21 : Introduction, notebooks, entrées/sorties de bases et variables

- {% notebook_badges slides/00-introduction/infos-slides.py.md %}
  [Slides Informations]({{site.url}}{{site.baseurl}}/slides/00-introduction/infos-slides.py.ipynb)
- {% notebook_badges slides/00-introduction/notebooks.py.md %}
  [Utiliser les notebooks Jupyter]({{site.url}}{{site.baseurl}}/slides/00-introduction/notebooks.py.ipynb)
- {% notebook_badges slides/01-IO_variables_chaines/io_variables_chaines.py.md %}
  [Notebook IO et variables]({{site.url}}{{site.baseurl}}/slides/01-IO_variables_chaines/io_variables_chaines.py.ipynb)
  - {% notebook_badges slides/01-IO_variables_chaines/solutions.py.md %}
      [Solutions]({{site.url}}{{site.baseurl}}/slides/01-IO_variables_chaines/solutions.py.ipynb)

À rendre pour la prochaine fois : exercices du notebook « IO et variables ».

Installer aussi l'environnement [Thonny](https://thonny.org).

Pour installer Thonny sous ChromeOS, c'est [un peu plus
sophistiqué](https://boldidea.org/static/thonny/chromebook.html), mais c'est possible.

Pour les tablettes sous iOS ou Android, ça ne sera pas possible. Vous devriez pouvoir suivre
l'essentiel du cours avec [`repl.it`](https://repl.it), mais ce n'est pas idéal, tenez-moi au
courant si vous n'avez pas le choix et je ferai de mon mieux pour vous permettre de suivre.

### 2025-01-28 : Instructions conditionnelles

- {% notebook_badges slides/02-conditions/conditions.py.md %}
  [Slides Instructions conditionnelles]({{site.url}}{{site.baseurl}}/slides/02-conditions/conditions.py.ipynb)
  - {% notebook_badges slides/01-IO_variables_chaines/solutions.py.md %}
      [Solutions]({{site.url}}{{site.baseurl}}/slides/02-conditions/solutions.py.ipynb)

### 2025-02-04 : Boucles et séquences

- {% notebook_badges slides/04-index_listes_iter/index_listes_iter.py.md %}
  [Slides Boucles et séquences]({{site.url}}{{site.baseurl}}/slides/04-index_listes_iter/index_listes_iter.py.ipynb)
  - {% notebook_badges slides/01-IO_variables_chaines/solutions.py.md %}
      [Solutions]({{site.url}}{{site.baseurl}}/slides/04-index_listes_iter/solutions.py.ipynb)

### 2025-02-11 : TD `turtle` et boucle `while`

- {% notebook_badges slides/03-turtle/turtle.py.md %}
  [Notebook `turtle`]({{site.url}}{{site.baseurl}}/slides/03-turtle/turtle.py.ipynb)
- {% notebook_badges slides/05-td_while/td_while.py.md %}
  [Notebook `while`]({{site.url}}{{site.baseurl}}/slides/05-td_while/td_while.py.ipynb)

## Ressources

- [Real Python](https://realpython.com), des cours et des tutoriels souvent de très bonne qualité et
  pour tous niveaux.

### Cours et tutoriels

- [Le cours de France IOI](https://www.france-ioi.org/algo/chapters.php)
- [Le cours d'OpenClassroom](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python)
- [Un MOOC](https://www.fun-mooc.fr/fr/cours/apprendre-a-coder-avec-python/) sur FUN
- [Google's Python Class](https://developers.google.com/edu/python/). Guido a travaillé chez eux.
  Pas [ce
  Guido](http://vignette2.wikia.nocookie.net/pixar/images/1/10/Guido.png/revision/latest?cb=20140314012724),
  [celui-là](https://en.wikipedia.org/wiki/Guido_van_Rossum)

Plus avancés :

- [Le tutoriel officiel](https://docs.python.org/fr/3/tutorial/) en français !
- [Practical Python](https://dabeaz-course.github.io/practical-python/Notes/Contents.html)
- [Python Mastery](https://github.com/dabeaz-course/python-mastery)

### Jeux de développement

- [Coding Game](https://www.codingame.com/home)
- [newcoder.io](http://newcoder.io/). Des projets commentés, commencer par 'Data Visualization'
- [Code combat](https://codecombat.com/)

### Livres

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

## Licences

[![CC BY Licence
badge](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

Copyright © 2025 L. Grobol [\<lgrobol@tuta.com\>](mailto:lgrobol@tuta.com)

Sauf indication contraire, les fichiers présents dans ce dépôt sont distribués selon les termes de
la licence [Creative Commons Attribution 4.0
International](https://creativecommons.org/licenses/by/4.0/). Voir [le README](README.md#Licences)
pour plus de détails.

 Un résumé simplifié de cette licence est disponible à
 <https://creativecommons.org/licenses/by/4.0/>.

 Le texte intégral de cette licence est disponible à
 <https://creativecommons.org/licenses/by/4.0/legalcode>
