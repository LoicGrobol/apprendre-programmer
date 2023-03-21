---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "skip"} -->
<!-- LTeX: language=fr -->
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 9 : solutions
===================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## 🐢 Exo 🐢
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Exercice 1

À l'aide des fonctions `turtle`, dessiner un carré de côté 100 pixels.

```python
from turtle import *

shape("turtle")

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
```

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "subslide"} -->
### Exercice 2

Reproduire la forme suivante à l’aide des fonctions `turtle`. Le cercle fait 100 pixels de rayon. Le
tracé est bleu et l’épaisseur du trait est de 3 pixels :

![Un cercle traversé par une ligne verticale. Le tracé est en bleu](img/io.png)

```python
from turtle import *

shape("turtle")
color("blue")
pensize(3)
circle(100)
left(90)
forward(200)
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Exercice 3

Reproduire la forme suivante à l’aide des fonctions `turtle`. Les segments font 60 pixels, le tracé
est en vert et d'épaisseur 3 pixels.

![Une croix grecque. Le tracé est en bleu](img/cross.png)

```python
from turtle import *

shape("turtle")
color("green")
pensize(3)

forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)

forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)

forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)

forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Exercice 4

Reproduire la forme suivante à l’aide des fonctions `turtle`. Chaque carré mesure 60 pixels de côté
et il y a 30 pixels entre les carrés.

![Quatre carrés alignés sur une grille 2×2. Les carrés nord-ouest et sud-est sont bleus, les deux autres sont rouges.](img/squares.png)

```python
from turtle import *

shape("turtle")

color("red")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)

up()
left(180)
forward(90)
left(180)
down()

color("blue")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)

up()
right(90)
forward(90)
left(90)
down()

color("red")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)

up()
forward(90)
down()

color("blue")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
```
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
### 🟠 Entraînements 🟠

1\. Écrire un programme dans lequel

- Vous définissez une fonction nommée `dire_bonjour` qui affiche `"Bonjour les ami⋅es !"`.
- Vous appelez trois fois cette fonction.
<!-- #endregion -->

```python
def dire_bonjour():
    print("Bonjour les ami⋅es")

dire_bonjour()
dire_bonjour()
dire_bonjour()
```

<!-- #region slideshow={"slide_type": "subslide"} -->
2\. Écrire un programme dans lequel

- Vous définissez une fonction (du nom que vous voulez) qui affiche mille fois `"spam"`.
- Vous appelez une fois cette fonction.
<!-- #endregion -->

```python
def spam1k():
    for _ in range(1000):
        print("spam")

spam1k()
```

```python
def spam1k2():
    print(1000*"spam\n")

spam1k2()
```

<!-- #region slideshow={"slide_type": "subslide"} -->
3\. Écrire un programme dans lequel

- Vous définissez une fonction (du nom que vous voulez) qui affiche une fois `"spam"`.
- Vous appelez mille fois cette fonction.
<!-- #endregion -->

```python
def spam():
    print("spam")

for _ in range(1000):
    spam()
```

<!-- #region slideshow={"slide_type": "subslide"} -->
4\. Refaire l'exercice 4 précédent, mais en utilisant une fonction pour les instructions qui
dessinent un carré.

```python
from turtle import *

def draw_square():
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    left(90)

shape("turtle")

color("red")
draw_square()

up()
left(180)
forward(90)
left(180)
down()

color("blue")
draw_square()

up()
right(90)
forward(90)
left(90)
down()

color("red")
draw_square()

up()
forward(90)
down()

color("blue")
draw_square()
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## 😺 Entraînements 😺

(Pensez à tester vos fonctions)

1\. Définir une fonction nommée `triple` qui accepte un argument, supposé être un nombre, et affiche
son triple.
<!-- #endregion -->

```python
def triple(n):
    res = 3*n
    print(res)

triple(4)
triple(-16)
triple(14)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
2\. Définir une fonction nommée `crier` qui accepte un argument, supposé être une chaîne de
caractères, et affiche cette chaîne mise tout en majuscules.
<!-- #endregion -->

```python
def crier(chaine):
    print(chaine.upper())

crier("vive la révolution")
```

<!-- #region slideshow={"slide_type": "subslide"} -->
3\. Définir une fonction nommée `produit` qui accepte deux arguments et affiche leur produit. Tester
`produit(3, 4)` et `produit("spam ", 5)`.
<!-- #endregion -->

```python
def produit(a, b):
    resultat = a*b
    print(resultat)

produit(3, 4)
produit("spam ", 5)
```

<!-- #region slideshow={"slide_type": "subslide"} -->
4\. Définir une fonction `carré`, qui accepte un argument `c`, supposé être un nombre entier et
dessine à l'aide de `turtle` un carré de côté `c`.

```python
def carré(c):
    forward(c)
    left(90)
    forward(c)
    left(90)
    forward(c)
    left(90)
    forward(c)
    left(90)
```
<!-- #endregion -->

