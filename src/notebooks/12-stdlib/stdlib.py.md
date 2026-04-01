---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->

<!-- #region slideshow={"slide_type": "slide"} -->

# Cours 13 : La bibliothèque standard de Python

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

Dans ce notebook :

- Importer un module
- Les modules utiles inclus dans Python

## La doc

Pour l'instant, nous avons programmé en Python en utilisant les fonctionnalités de base du langage :
mot-clés (comme `def` ou `if`) et fonctions prédéfinies (comme `len` ou `input`).

La documentation de Python est très bien faite. Elle n'est pas prévue pour des débutant⋅es en
programmation, mais… Vous n'êtes plus des débutant⋅es, n'est-ce pas ? Dans ce cours on va essayer de
s'y référer un maximum et de s'entraîner à l'utiliser. Commencez par aller voir la
[liste des fonctions par défaut](https://docs.python.org/3/library/functions.html).

À partir de cette liste, et en allant voir sa documentation spécifique : que fait la fonction
`hex` ?

La documentation a aussi une fonction de recherche (qui est perfectible), mais surtout un
[index](https://docs.python.org/3/genindex.html). À l'aide de ce dernier : à quoi sert la fonction
`pow` ?

La documentation est partiellement disponible en français, mais la version la plus à jour est celle
en anglais. Elle comprend également un [tutoriel](https://docs.python.org/3/tutorial/index.html)
(que vous avez maintenant le niveau pour suivre !) et une référence
[complète des fonctionnalités du langage](https://docs.python.org/3/library/index.html).

## Modules

### Import ?

Rappelez vous

> Entrez les commandes suivantes dans la console :
>
> ```python
> from turtle import *
> shape("turtle")
> ```

> On peut obtenir un entier aléatoire en utilisant la fonction `randint` du module `random` :
>
> ```python
> import random
> random.randint(8)
> ```

> […] ou encore le module `copy`
>
> ```python
> import copy
>
> a = [1, 2, 3]
> b = copy.copy(a)
> ```

C'est quoi à la fin `import` ?

Python nous fournit en fait bien plus d'outils que les *built-ins* qu'on a vu plus haut. Il propose
aussi des outils pour faire des maths, manipuler les fichiers plus facilement, accéder à internet,
gérer des dates, des traductions, manipuler des fichiers son…

C'est beaucoup et ça ne serait pas pratique d'avoir tout par défaut dans les *built-ins* :

- On risquerait d'avoir des collisions de noms. Par exemple entre la fonction `list` qui permet de
  lister les fichiers compressés dans un fichiers zip, et la fonction *built-in* `list` qui créée
  des listes à partir d'itérables.
- Chaque fonction qui est chargée en mémoire prend de la place, ralentit potentiellement le
  programme etc. Or la plupart des programmes n'ont pas besoin d'utiliser tout ça en même temps.

La solution : les modules !

Un module Python est un ensemble de variables et de fonctions, défini dans un fichier à part. Si on
veut accéder à ces éléments, on peut le charger en mémoire (l'« importer ») à l'aide du mot clé
`import`.

```python
import random
```

Une fois qu'on a importé un module il sert d'*espace de nom* : une fois `random` importé, sa
fonction `randint` nous devient accessible sous le nom composé `random.randint`, à comprendre comme
« l'objet qui a été défini comme `randint` dans le module `random` » :

```python
print(random.randint(4))
```

La liste de tous les modules distribués avec Python (sa « bibliothèque standard ») est disponible
dans [la doc](https://docs.python.org/3/py-modindex.html) (c'est le lien « modules » en haut à
droite de la page). Si vous allez chercher `random` dans cette liste, vous arriverez à
[sa page de documentation spécifique](https://docs.python.org/3/library/random.html#module-random).

### 🧑🏻‍🔬 Entraînement 🧑🏻‍🔬

1\. Comment s'appelle le module de la bibliothèque standard qui sert à manipuler des expressions
régulières ?

2\. À quoi sert la fonction `time_ns` du module `time` ?

3\. À l'aide du module `random`, écrivez une fonction qui génère deux `float` aléatoires compris
entre $0$ et $1$ et renvoie leur somme. Pensez à la tester ! Indice : allez voir du côté de la
section « *Real-valued distributions* ».

```python
```

### From import ?

Il arrive parfois qu'on ait seulement besoin d'une ou quelques fonctions d'un module. Par exemple,
je me sers souvent de `math.ceil` (qui sert à quoi ?), et c'est un peu désagréable d'avoir à écrire
tout le nom à la fois. Et encore, ce n'est rien à côté de
`xmlrpc.server.SimpleXMLRPCServer.register_instance`

Bien sûr je pourrais ruser, par exemple en définissant moi-même une fonction `ceil` :

```python
import math

def ceil(x):
    return math.ceil(x)

ceil(9.1)
```

Ou — ce qui est déjà beaucoup mieux — en stockant `math.ceil` dans une variable avec un nom court

```python
import math

# J'aurais aussi pu l'appeller "c" ou "truc"
ceil = math.ceil

ceil(1.3)
```

C'est quand même un peu verbeux pour un truc qu'on fait assez souvent, alors Python nous fournit un
raccourci : la syntaxe `import … from …` :

```python
from math import ceil

ceil(-0.2)
```

Au lieu d'importer tout l'espace de noms du module `math`, j'importe uniquement la fonction qui
m'intéresse. Et si son nom ne me plaît pas, je peux la renommer en plus avec la syntaxe
`from … import … as …` :

```python
from math import ceil as machin

machin(12.9)
```

### 🐔 Entrainement 🐔

1\. Importer uniquement la fonction du module `math` qui permet de calculer la racine carrée d'un
nombre. Calculer $√2713$.

2\. En important une seule fonction, afficher la date et l'heure actuelle

### `*`?

On a utilisé pour `turtle` la syntaxe `from turtle import *`. Cette syntaxe permet d'importer tout
un module dans l'espace de nom principal. Ainsi la fonction `turtle.forward` devient directement
disponible sous le nom `forward`. C'est **une très mauvaise pratique** : entre autres parce que
quand vous lisez du code où elle a été utilisée, il est très difficile de savoir où les objets ont
été définis. Vous ne devriez **jamais** avoir à l'utiliser.

## Module utiles

On a déjà vu `math` et `random`, en voici quelques autres

## `re`, les expressions régulières

Rappelez-vous les expressions régulières : elles servent à répondre à des questions comme « étant
donnée une chaîne de caractères, est-ce que cette chaîne contient une suite de trois chiffres :

```python
import re

motif = "[0-9][0-9][0-9]"

if re.search(motif, "foo123bar"):
    print("oui")
else:
    print("non")

if re.search(motif, "truc 65787b idu le"):
    print("oui")
else:
    print("non")

if re.search(motif, "Bonjour"):
    print("oui")
else:
    print("non")
```

Les expressions régulières de Python sont un peu différentes de celles qu'on a vu l'an dernier, mais
le principe général reste le même : on utilise un mini-langage compact pour représenter un motif,
puis on peut utiliser des fonctions telles que `re.search` pour chercher des occurrences de ce motif
dans une chaîne de caractères.

[Real Python](https://realpython.com/regex-python/) a un tutoriel très complet dessus, que je vous
encourage fort à suivre.

- re
- maths
- itertools
- csv
- pathlib
