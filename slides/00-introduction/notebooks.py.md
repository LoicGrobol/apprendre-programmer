---
jupyter:
  jupytext:
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "skip"} -->
<!-- LTeX: language=fr -->
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 0 : Utiliser les notebooks Jupyter
==============================
<!-- #endregion -->

**Félicitations**

Vous avez réussi à ouvrir un notebook Jupyter.

Cliquez sur la cellule ci-dessous (le cadre avec `print(…`) dans une police différente), puis
 sur “▸ *Run*” dans la barre d'outils.

```python
print("Hello, world!")
```

Si vous voyez un message s'afficher, vous avez correctement exécuté la cellule. Si c'est la première
fois que vous exécutez un programme, félicitations ! J'espère que ce sera le premier d'une longue
série d'aventures programmatiques.

## Les notebooks

Avant de commencer à apprendre Python, vous allez devoir apprendre à utiliser les *notebooks* qui
seront notre outil de travail principal (mais pas le seul !).

Heureusement, c'est très facile et d'ici une semaine ou deux ça vous paraîtra complètement naturel.
Ce document devrait contenir toutes les informations dont vous aurez besoin, n'hésitez donc pas à le
garder sous la main.


### C'est quoi ? Et pourquoi on s'en sert ?

Un *notebook* est un environnement de programmation très différent (quoi que…) de ceux utilisés par
les développeureuses professionel⋅les pour concevoir des logiciels. Vous pouvez y penser comme un
cahier dans lequel vous pouvez insérer à la fois des programmes, du texte, des images, des liens
vers des vidéos…

Ce n'est pas forcément très utile pour concevoir un logiciel, mais pour *apprendre à programmer*,
c'est très utile : on peut ainsi annoter les programmes qu'on écrit avec des explications, ajouter
des instructions, des illustrations…

Pour ce cours, vous pouvez considérer les *notebooks* comme les chapitres d'un manuel de cours
interactif. Tous les programmes de ce manuel peuvent être exécutés (comme vous l'avez fait
ci-dessus) pour voir leur résultat **et vous pouvez y ajouter votre propre code et vos propres
textes**, comme si vous pouviez écrire dans les pages de votre manuel pour le modifier.

### Comment on s'en sert ?

Les *notebooks* sont à la fois **le matériel de cours** et le support pour **vos devoir**. Chacun
d'entre eux contient des exercices et ce sera à vous d'écrire vos solutions directement dans le
*notebook *et de le sauvegarder.

Il y a beaucoup de façons d'interagir avec des *notebooks* :

- Vous être probablement en train de lire ceci via *Binder*, qui est un moyen rapide et pratique d'y
  accéder (les liens seront directement sur la page du cours et vous n'avez pas besoin
  d'inscription).
  - Pour chaque notebook du cours, cliquer sur le badge
    [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LoicGrobol/apprendre-programmer/main)
    vous emmène sur une instance de Binder avec le notebook déjà chargé
  - Attention : si vous restez trop longtemps sans exécuter de code dans Binder, votre session se
    coupe ! Vous pouvez toujours sauvegarder le notebook sur votre machine, mais si vous le
    recharger sur Binder, il faudra le ré-uploader
- Vous pouvez installer [Edupyter](https://www.edupyter.net/) sur votre machine, qui vous donnera
  accès à Jupyter et à l'éditeur de code Thonny, dont on se servira plus tard dans le cours.
- Si vous avez un compte Google, vous pouvez aussi y accéder dans [Google
  Colaboratory](https://colab.research.google.com), pour ça, il faut télécharger à partir du
  **lien** sur la page du cours le fichier `.ipynb`, puis le charger (avec *upload*) dans Colab
  - Les sauvegardes se font automatiquement dans votre espace Drive
  - La version de Python de Colab est un peu ancienne, normalement ça ne pose pas de problème pour
    ce cours, mais attention.
  - Pour en savoir plus, vous pouvez exécuter la cellule suivante pour voir une vidéo d'explications

```python
from IPython.display import IFrame
IFrame('https://www.youtube.com/embed/inN8seMm7UI', width=700, height=350)
```

Quelle que soit la plateforme que vous utilisez, je vous recommande très fortement de toujours sauvegarder vos notebooks dans un dossier sur votre machine (ou une clé ou…) pour ne pas les perdre.

Pour rendre vos exercices, passez par l'espace Cours en Ligne du cours (voir la page principale) :
une fois que vous avez rempli vos réponses aux exercices d'un notebook, vous le téléchargez sur
votre machine, puis vous le soumettez dans la section des exercices de la semaine sur Cours en
Ligne.

### Comment ça marche ?

Les *notebooks* sont divisés en cellule, certaines (comme celle-ci) contiennent du texte au format
[Markdown](https://fr.wikipedia.org/wiki/Markdown) et d'autres contiennent du code en Python. Vous
pouvez modifier et *exécuter* les cellules de code et vous pouvez modifier et formatter les cellules
de texte.

Pour exécuter une cellule, il faut cliquer dessus, puis sur le bouton « ▸ *Run* » (ou sur le bouton
▸ à gauche de la cellule dans Colab) :

```python
print("Cliquez sur « ▸ *Run* » pour exécuter cette cellule")
```

Vous pouvez aussi utiliser le raccourci clavier <kbd>ctrl</kbd>+<kbd>↩</kbd>. Il y a plein de
raccourcis clavier dans Jupyter, n'hésitez pas à explorer !

### Créer une nouvelle cellule

Vous pouvez facilement créer de nouvelles cellules :

- À l'aide du menu « *Insert* ».
- En utilisant le raccourci <kbd>echap</kbd>+<kbd>B</kbd> pour insérer une cellule en dessous de la
  cellule actuelle (ou <kbd>echap</kbd>+<kbd>A</kbd> pour le faire au dessus), puis en appuyant sur
  <kbd>↩</kbd> pour entrer en mode édition.

(Précisément : <kbd>echap</kbd> vous passe en mode « commande », puis <kbd>B</kbd> lance la commande
« insérer une cellule ci-dessous », et <kbd>↩</kbd> vous sort du mode commande pour passer en mode
édition).


### Code vs. Markdown

La barre d'outils vous indique si vous êtes en mode « Code » ou « Markdown », et vous pouvez
utiliser la boîte déroulate pour changer de mode.

Ou vous pouvez utiliser <kbd>echap</kbd>+<kbd>M</kbd> pour passer une cellule en mode Markdown ou
<kbd>echap</kbd>+<kbd>Y</kbd> pour la passer en mode code (n'oubliez pas de rappuyer sur
<kbd>↩</kbd> pour repasser en mode édition).


### Formater du Markdown


En mode Markdown, `*du texte entre deux astérisques*` est affiché en *italiques*. `**et quatres astériques**` font du **gras.**

Mettre du texte entre accents graves sert à signaler du `code` et les `#` servent à faire des titres.


### Plus d'infos…

… en suivant ce lien : <https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/>


## À toi de jouer

### 👶 Exo 👶

La cellule ci-dessous contient du code. Ne vous préoccupez pas de ce qu'il signifie pour l'instant, on s'entraîne juste !

1\. Cliquer sur la cellule pour la sélectionner, puis exécutez-la pour voir son résultat.

2\. Sélectionnez-la à nouveau, et dans la ligne `x = 5`, remplacez 5 par 10, puis exécutez-la à nouveau pour voir le nouveau résultat

```python
x = 5
print(x*2 + 1)
```

Si vous ne vous êtes pas trompé⋅e, vous devriez maintenant voir `21` sous la cellule. Sauvegarder le notebook :

- *File* > *Save* dans Colab
- *File* > *Download as* > *Notebook* dans Binder

### ✏️ Exo ✏️

Certains exercices ne vous demandent pas d'écrire du code, mais une réponse en texte. Pour ces
exercices, vous devrez modifier une cellule de texte. Ça fonctionne exactement pareil sauf qu'il
vous faut double-cliquer pour modifier une cellule de texte

Double-cliquez sur la cellule de texte ci-dessous pour passer en mode édition, écrire quelque chose
(quelque chose de joli pour illuminer la journée de votre prof par exemple), puis exécutez-la.
N'oubliez pas de sauvegarder.


*Replace this text by your own message*


Déposez ensuite le fichier ipynb que vous venez de télécharger sur Cours En Ligne.
