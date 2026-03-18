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
Cours 5 : Compléments sur les boucles
=====================================

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

Dans ce notebook

- La boucle conditionnelle `while`.

## 🔄 Exo 🔄

Voici une liste

```python
fruits = ["pomme", "poire", "kiwi", "maracuja"]
```

Demandez à l'utilisateurice un nom de fruit et affichez `"😋"` s'il est dans la liste et `"🤨"`
sinon.

```python

```

## Blockly games

- [Le labyrinthe](https://blockly.games/maze?lang=fr)
- Si vous vous ennuyez : [turtle dans Blockly](https://blockly.games/turtle?lang=fr), vous pouvez
  aussi faire les mêmes exercices avec `turtle` en Python, ce sont des bons entraînements.

## Boucle conditionnelle `while`

Les boucles **itératives** `for` permettent de parcourir une séquence, en accédant à ses éléments
les uns à la suite des autres et en exécutant à chaque itération (chaque « tour ») une même série
d'instructions.

La boucle **conditionnelle** `while` (« tant que ») permet, elle aussi de répéter plusieurs fois une
série d'instructions, mais au lieu d'être contrôlée par une séquence, elle est contrôlée par une
condition :

```python
nombre = 0
while nombre < 10:
    print(nombre)
    nombre = nombre + 1
print("Terminé!")
```

Pouvez-vous expliquer le comportement de cette cellule ?

---

<!-- #region -->
La structure introduite par `while` permet d'exécuter une série d'instructions, un *bloc*,
matérialisé comme d'habitude par l'indentation tant qu'une certaine condition est vraie. Sa syntaxe,
qui ressemble à celle de l'instruction conditionnelle `if` est la suivante :

```python
while CONDITION:
    # le code à exécuter tant que la condition est vérifiée, c-à-d est évaluée True
```

<!-- #endregion -->

La différence cruciale avec `if`, est que, avec `while`, le bloc est exécuté autant de fois que la
condition est vraie, et pas seulement une fois. Comparez ainsi :

```python
n = 5
if n < 7:
    print(n)
    n = n+1
```

avec :

```python
n = 5
while n < 7:
    print(n)
    n = n + 1
```

Que se passe-t-il si la condition est fausse dès le début ?

```python
n = 8
while n < 7:
    print(n)
    n = n + 1
```

Pouvez-vous en déduire ce qui se passe dans ce cas ?

```python
while False:
    print("Bonjour !")
```

Et dans ce cas ? **Attention, réfléchissez avant d'exécuter la cellule.**

```python tags=["skip-execution"]
n = 0
while True:
    print("spam", n)
    n = n + 1
```

Vous pouvez interrompre l'exécution en appuyant deux fois sur `i`. Redémarrez ensuite le kernel.

---

Quand on utilise `while`, il faut toujours s'assurer que la condition peut devenir fausse (qu'on
puisse la **falsifier**), autrement il s'agira d'une **boucle infinie**. On peut vouloir le faire
exprès, mais il faut quand même un mécanisme pour sortir d'une telle boucle, sinon le programme ne
s'arrête jamais.

Enfin, il peut arriver qu'on veuille interrompre l'exécution d'une boucle avant que la condition
soit falsifiée. C'est possible avec l'instruction `break` :

```python
n = 0
while n < 9:
    print(n)
    if n == 7:
        break
    n = n + 1
```

On peut toujours faire sans et pour l'instant ça ne nous sera pas trop utile, mais si jamais vous
tombez dessus vous saurez de quoi il s'agit.

## 🤔 Exo 🤔

On peut obtenir un entier aléatoire en utilisant la fonction `randint` du module `random` :

```python
import random
```

```python
random.randint(4, 8)  # Exécuter plusieurs fois cette cellule
```

Écrivez un programme qui :

- Choisit aléatoirement un nombre entre $1$ et $16$
- Demande à l'utilisateurice de deviner le nombre en lui proposant de réessayer tant que le nombre
  n'a pas été trouvé.

Exemple de sortie :

```text
J'ai choisi un nombre entre 1 et 10. Essaie de le deviner !
Fais ton choix: 1
Essaie encore: 5
Essaie encore: 7
Essaie encore: 2
Bravo! C'était bien 2
```

---

En Python, on préfère en général utiliser des boucles `for` — qui sont plus adaptées à
l'organisation du langage — et les boucle `while` ont tendance à être moins utilisées. Cependant, on
peut facilement simuler une boucle `for` avec une boucle `while`. Ainsi :

```python
l = ["spam", "spam", "lovely spam", "wonderful spam"]
for s in l:
    print(s)
```

est équivalent à

```python
l = ["spam", "spam", "lovely spam", "wonderful spam"]
i = 0
while i < len(l):
    print(l[i])
    i = i + 1
```

Inversement, il n'est pas évident de simuler le comportement suivant avec une boucle `for`

```python tags=["skip-execution"]
ingredients_disponibles = ["piment", "poireau", "champignon", "carotte"]
ingredient = input("Donne-moi un ingrédient: ")

while ingredient not in ingredients_disponibles:
    print("J'en ai pas !")
    ingredient = input("Donne-moi un ingrédient: ")
    
print("Ah, oui,", ingredient, "j'en ai")
```


### `range` : les intervalles entiers

Comment faire pour afficher dix fois « Bonjour » ?

Il y a une réponse simpliste : « je copie-colle `print("Bonjour")` dix fois ».

Mais ce n'est pas très satisfaisant, non ?

Une solution avec la boucle `for` :

```python
for a in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Bonjour")
```

Mais ce n'est toujours pas très pratique d'écrire cette liste. Surtout pour ne rien en faire.
Heureusement, il y a un outil pour nous faciliter la vie : la fonction `range` :

```python
for truc in range(10):
    print("Bonjour")
```

Pas mal, non ?

**Note de style** dans la cellule précédente, on utilise jamais la valeur de `truc`. En Python,
quand on doit donner un nom à une variable qu'on utilise par ailleurs pas, la convention est de
l'appeler `_`. Vous trouverez donc souvent des trucs écrits comme.

```python
for _ in range(10):
    print("Bonjour")
```

```python
for i in range(10):
    print(i)
```

Vous devinez ce que renvoie `range(10)` ? À votre avis que renverrait `range(16)` ?

On teste ?

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)
```

```python
print(range(10))
```

Ce n'est pas très informatif. Dans les temps anciens de la version 2 de Python, `range(n)` renvoyait
la liste des entiers de $0$ à $n$. Depuis, les temps ont changé et `range` renvoie simplement un
objet de type `range`.

```python
print(type(range(10)))
```

Pourquoi `range` ne renvoie pas une liste ? Parce que ça permet d'éviter de stocker tous les
éléments de la liste en mémoire, ça prend moins de place, votre machine est contente.

Mais vous pouvez quand même itérer dessus :

```python
for i in range(16):
    print(i)
```

On dit que les objets de type `range` sont des ✨**itérables**✨.

En plus de la borne supérieure, on peut aussi spécifier la borne inférieure :

```python
for i in range(2, 16):
    print(i)
```

Les règles sont toujours les mêmes en Python : la borne inférieure est incluse, la borne supérieure
est exclue.

```python
for value in range(512, 1024):
    print(value)
```

Bon, mais si on veut **vraiment** la liste de ces nombres ?

On peut convertir un `range` en liste en utilisant la fonction `list` :

```python
print("L'objet range:", range(10))
print("La liste qui correspond:", list(range(10)))
```

```python
list("abcxde")
```

Enfin, on peut également (mais c'est plus rarement utile) préciser le pas :

```python
for value in range(1, 10, 2):
    print(value)
```
