---
title: Informations et cours
layout: default
permalink: /2023/
---

[comment]: <> "LTeX: language=fr"


## Nouvelles

- **2022-01-15** Premier cours de cette session le mardi 17 janvier 2023. *Be there and beware!*


## Infos pratiques

- **Quoi** « Apprendre à programmer », 4L6SC01P
- **Où** Salle N19, bâtiment Éphémère 2, Université Paris Nanterre, 200 avenue de la République,
  Nanterre
- **Quand** 12 séances, les mardis de 10:30 à 12:30, du 17/01 au 18/04
  - Voir [le calendrier de
    l'université](https://etudiants.parisnanterre.fr/calendrier-universitaire/calendrier-universitaire-2022-2023)
    pour les dates de vacances.
- **Contact** Loïc Grobol [`<lgrobol@parisnanterre.fr>`](mailto:lgrobol@parisnanterre.fr)
- **Dépôt des exercices** de préférence [sur Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7459) (clé d'inscription `rossum`)
  ou par email (voir ci-dessus.)

## Liens utiles

- [Espace Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7459)
  - Inscription libre avec la clé `rossum`
  - Attention, cet espace ne sert qu'aux dépôts de devoirs.
- [Page du cours de l'an dernier]({{site.url}}{{site.baseurl}}/2022)
- [Le dépôt Github du cours](https://github.com/LoicGrobol/apprendre-programmer/) contient toutes
  les sources permettant de générer le matériel du cours.
- Lien Binder de secours :
  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LoicGrobol/apprendre-programmer/main)


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

### 2023-01-17 : Introduction, notebooks, entrées/sorties de bases et variables

- {% notebook_badges slides/00-introduction/introduction-slides.py.md %}
  [Slides Introduction](slides/00-introduction/introduction-slides.py.ipynb)
- {% notebook_badges slides/00-introduction/notebooks.py.md %}
  [Utiliser les notebooks Jupyter](slides/00-introduction/notebooks.py.ipynb)
- {% notebook_badges slides/01-IO_variables_chaines/io_variables_chaines.py.md %}
  [Notebook IO et variables](slides/01-IO_variables_chaines/io_variables_chaines.py.ipynb)
  - {% notebook_badges slides/01-IO_variables_chaines/solutions.py.md %}
    [solutions](slides/01-IO_variables_chaines/solutions.py.ipynb)


À rendre pour la prochaine fois : exercices du notebook « IO et variables ».

Installer aussi l'environnement [Thonny](https://thonny.org).

Pour installer Thonny sous ChromeOS, c'est [un peu plus
sophistiqué](https://boldidea.org/static/thonny/chromebook.html), mais c'est possible.

Pour les tablettes sous iOS ou Android, ça ne sera pas possible. Vous devriez pouvoir suivre
l'essentiel du cours avec [`repl.it`](https://repl.it), mais ce n'est pas idéal, tenez-moi au
courant si vous n'avez pas le choix et je ferai de mon mieux pour vous permettre de suivre.


### 2023-01-24 : Instructions conditionnelles, `turtle` et scripts

- {% notebook_badges slides/02-conditions/conditions.py.md %}
  [Notebook Conditions](slides/02-conditions/conditions.py.ipynb)
- {% notebook_badges slides/03-turtle/turtle.py.md %}
  [Notebook Turtle](slides/03-turtle/turtle.py.ipynb)
  - [solutions](slides/03-turtle/solutions.py)

### 2023-02-07 : Boucles

À faire pour le prochain cours : suivre les notebooks suivants, faire les exercices **puis**
vérifier avec les solutions. Je suis joignable par email si vous coincez, et on fera un
récapitulatif quand on aura enfin un cours en présentiel.

(Pensez vraiment — vraiment — **vraiment** à vous servir de [Python Tutor](https://pythontutor.com/)
pour tous les exercices sur les boucles).

- {% notebook_badges slides/04-index_listes_iter/index_listes_iter.py.md %}
  [Notebook listes et boucle `for`](slides/04-index_listes_iter/index_listes_iter.py.ipynb)
  - {% notebook_badges slides/04-index_listes_iter/solutions.py.md %}
    [Solutions](slides/04-index_listes_iter/solutions.py.ipynb)
- {% notebook_badges slides/05-td_while/td_while.py.md %}
  [Notebook boucle `while`](slides/05-td_while/td_while.py.ipynb)
  - {% notebook_badges slides/05-td_while/solutions.py.md %}
    [Solutions](slides/05-td_while/solutions.py.ipynb)

### 2023-02-14 : Récapitulatif

Résumé des épisodes précédents, avec **plein** d'exos.

- {% notebook_badges slides/06-recapitulatif/recapitulatif.py.md %}
[Notebook récapitulatif](slides/06-recapitulatif/recapitulatif.py.ipynb)
  - {% notebook_badges slides/06-recapitulatif/corrections.py.md %}
[Solutions](slides/06-recapitulatif/corrections.py.ipynb)

À rendre pour la prochaine fois : les exercices du notebook.

### 2023-02-21 : Compléments sur les boucles et les séquences

- {% notebook_badges slides/07-complements_boucles_sequences/complements_boucles_sequences.py.md %}
  [Notebook boucles et
  séquences](slides/07-complements_boucles_sequences/complements_boucles_sequences.py.ipynb)

### 2023-03-07 : Itérables et dictionnaires

- {% notebook_badges slides/08-iterables_dictionnaires/iterables_dictionnaires.py.md %} [Notebook
  itérables et dictionnaires](slides/08-iterables_dictionnaires/iterables_dictionnaires.py.ipynb)

### 2023-03-21 : Fonctions

- {% notebook_badges slides/09-fonctions/fonctions.py.md %}
  [Notebook fonctions](slides/09-fonctions/fonctions.py.ipynb)
  - {% notebook_badges slides/09-fonctions/solutions.py.md %} [Solutions](slides/09-fonctions/solutions.py.ipynb)

### 2023-03-28 : Valeurs de retour et accès à des fichiers

- {% notebook_badges slides/10-return_fichiers/return_fichiers.py.md %}
  [Slides retour et fichiers](slides/10-return_fichiers/return_fichiers.py.ipynb)

### 2023-04-04 : Récapitulatif (en temps libre)

- {% notebook_badges slides/11-recapitulatif-2/recapitulatif-2.py.md %} [Exercices récapitulatifs
  2](slides/11-recapitulatif-2/recapitulatif-2.py.ipynb)
  - {% notebook_badges slides/11-recapitulatif-2/corrections.py.md %}
    [Solutions](slides/11-recapitulatif-2/corrections.py.ipynb)
- {% notebook_badges assignment/projet-2023.py.md %}
  [Consignes mini-projet](assignment/projet-2023.py.ipynb)
  - [`lexique.txt`](assignment/lexique.txt), pensez à l'uploader si vous travaillez dans Colab.

### 2023-04-18 : Partiel

- {% notebook_badges exams/exam-2023.py.md %} [Partiel](exams/exam-2023.py.ipynb)

## Ressources

- [Real Python](https://realpython.com), des cours et des tutoriels souvent de très bonne qualité et
  pour tous niveaux.

### cours et tutoriels

- [Le tutoriel officiel](https://docs.python.org/fr/3/tutorial/) en français !
- [Google's Python Class](https://developers.google.com/edu/python/). Guido a travaillé chez eux.
  Pas [ce
  Guido](http://vignette2.wikia.nocookie.net/pixar/images/1/10/Guido.png/revision/latest?cb=20140314012724),
  [celui-là]
- [Code Academy](https://www.codecademy.com/fr/learn/python)

Plus avancés :

- [Practical Python](https://dabeaz-course.github.io/practical-python/Notes/Contents.html)
- [Python Mastery](https://github.com/dabeaz-course/python-mastery)

### Jeux de développement

- [Coding Game](https://www.codingame.com/home)
- [newcoder.io](http://newcoder.io/). Des projets commentés, commencer par 'Data Visualization'
(https://en.wikipedia.org/wiki/Guido_van_Rossum#/media/File:Guido_van_Rossum_OSCON_2006.jpg)
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

Copyright © 2023 Loïc Grobol [\<loic.grobol@gmail.com\>](mailto:loic.grobol@gmail.com)

Sauf indication contraire, les fichiers présents dans ce dépôt sont distribués selon les termes de
la licence [Creative Commons Attribution 4.0
International](https://creativecommons.org/licenses/by/4.0/). Voir [le README](README.md#Licences)
pour plus de détails.

 Un résumé simplifié de cette licence est disponible à
 <https://creativecommons.org/licenses/by/4.0/>.

 Le texte intégral de cette licence est disponible à
 <https://creativecommons.org/licenses/by/4.0/legalcode>
