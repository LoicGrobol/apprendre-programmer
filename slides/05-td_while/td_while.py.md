---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 5 : Exercices et compléments sur les boucles
==================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

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

En Python, on préfère en général utiliser des boucles `for` — qui sont plus adaptée à l'organisation
du langage — et les boucle `while` ont tendance à être moins utilisées. Cependant, on peut
facilement simuler une boucle `for` avec une boucle `while`. Ainsi :

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
