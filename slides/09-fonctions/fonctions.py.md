---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 9 : Fonctions
===================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-03-22
<!-- #endregion -->

Dans ce notebook

- On retrouve la tortue !
- Écrire ses propres fonctions

Les exercices sont tirés du cours « Apprendre à programmer avec Python », donnée à l'Université
Sorbonne Nouvelle par Marine Delaborde et Pascal Amsili, que je remercie très chaleureusement.

## Rappel chéloniens

Le module Python `turtle` permet de dessiner simplement en Python, en contrôlant un agent qui laisse
une trace sur une toile. `turtle` parce que ça fait comme une tortue qui aurait marché dans de la
peinture.

`turtle` ne marche pas vraiment dans l'interface Jupyter Notebook. Pour ce qui suit, vous devrez
donc travailler soit dans un environnement de programmation Python local (par exemple
[Thonny](https://thonny.org/)), soit avec l'environnement en ligne [repl.it](repl.it) (pensez à bien
sélectionner le mode Python `turtle`). Pour le fonctionnement de Thonny, vous pouvez revenir au
[cours 2](../02-turtle/turtle.py.md).

Rappel : c'est en général plus agréable dans ce genre de cas d'utiliser des **scripts**: des
fichiers textes avec l'extension `.py` qui contiennent des programmes. Vous pouvez les ouvrir dans
Thonny (où ils s'affichent dans la zone d'édition) et les exécuter avec le bouton ▶️.

Les commandes de base en `turtle` :

- `forward(d)` avance de d pixels
- `backward(d)` recule de d pixels
- `left(a)` pivote vers la gauche de a degrés
- `right(a)` pivote vers la droite de a degrés
- `up()` relève le crayon pour avancer sans dessiner
- `down()` abaisse le crayon pour dessiner
- `reset()` remet le dessin à zéro
- `circle(r, a)` trace un arc de cercle de rayon `rayon` et d'angle `a` degrés. `a` est facultatif
  et vaut `360` par défaut (soit un cercle entier).
- `pensize(e)` épaisseur du tracé (pixels)
- `color(couleur)` couleur du tracé (par exemple `color("blue")`).

## 🐢 Exo 🐢

### Exercice 1

À l'aide des fonctions `turtle`, dessiner un carré de côté 100 pixels.

### Exercice 2

Reproduire la forme suivante à l’aide des fonctions `turtle`. Le cercle fait 100 pixels de rayon. Le
tracé est bleu et l’épaisseur du trait est de 3 pixels :

![Un cercle traversé par une ligne verticale. Le tracé est en bleu](img/io.png)

### Exercice 3

Reproduire la forme suivante à l’aide des fonctions `turtle`. Les segments font 60 pixels, le tracé
est en vert et d'épaisseur 3 pixels.

![Une croix grecque. Le tracé est en bleu](img/cross.png)

### Exercice 4

Reproduire la forme suivante à l’aide des fonctions `turtle`. Chaque carré mesure 60 pixels de côté
et il y a 30 pixels entre les carrés.

![Quatre carrés alignés sur une grille 2×2. Les carrés nord-ouest et sud-est sont bleus, les deux autres sont rouges.](img/squares.png)

## J'en ai marre de faire des copier-coller !

Est-ce que vous avez trouvé ce dernier exercice **désagréable** ?

---

Moi oui ! On a du écrire quatre fois les mêmes instructions pour dessiner un carré. Certes on peut
faire des copier-coller, mais c'est pénible. Et il se passe quoi si on a plus de carrés ?

On aurait aussi peut-être pu s'en sortir avec une boucle, mais ça aurait été compliqué.

En fait ce qu'il faudrait c'est une façon de sauvegarder une suite d'instructions et de pouvoir les
exécuter quand on veux. Comme ça il ne nous serait plus resté que le code pour positionner la tortue
au point de départ.

Bonne nouvelle : ça existe, et vous l'utilisez déjà sans le savoir.

---

Ce qu'il nous faut, ce sont des **fonctions**.

<!-- #region -->
## Les fonctions

### De vieilles connaissances

Vous connaissez déjà les fonctions
<!-- #endregion -->

```python
print("Hello les potos !")
```

```python tags=["skip-execution"]
input()
```

Vous connaissez `len`.

```python
len("hello")
```

```python
len([1, 2, 3])
```

```python
len({"Cats": "beautiful", "Python": "ton meilleur ami"})
```

Vous connaissez `float`, et `int` et `str`

```python
float(1)
```

```python
int("364")
```

```python
str(1)
```

Vous connaissez `str.lower` et bien d'autres

```python
str.lower("AAAAAAAAAAAH!")
```

Et vous connaissez les fonctions de `turtle` qu'on vient de voir.

Mais c'est quoi, en vrai, une fonction ?

Et est-ce qu'on peut en faire nous même ?

### Définir des fonctions

```python
def say_hello():
    print("Bonjour")

print("On va dire bonjour")
say_hello()
print("Encore")
say_hello()
print("Et encore")
```

Une fonction, c'est un bloc de code, une série d'instructions, un bout de programme auquel on donne
un nom pour pouvoir le réutiliser. Dans le cellule ci-dessus, on a donné le nom `say_hello` à un
morceau de code qui ne contient qu'une seule instruction `print("Bonjour")`.

Par la suite, à chaque fois qu'on écrit l'instruction `say_hello()`, c'est `print("Bonjour")` qui
est exécuté.On dit qu'on a **appelé** la fonction `say_hello`.


On peut le faire pour plusieurs instructions

```python
def sing():
    print("Alo")
    print("Salut")
    print("Sunt eu")
    print("un haiduc")

sing()
sing()
```

Note : dans un notebook, comme pour les variables, les fonctions définies dans une cellule sont
accessibles dans les autres cellules :

```python
say_hello()
```

<!-- #region -->
On définit une fonction à l'aide du mot-clé `def`, qui introduit un bloc d'instructions (le
**corps** de la fonction), qui seront celles liées au nom donné. Formellement :

```python
def <nom de la fonction>():
    <instruction 1>
    <instruction 2>
    …
```
<!-- #endregion -->

On peut mettre absolument n'importe quelle suite d'instructions dans le corps d'une fonction :


Utiliser des variables

```python
def calculer():
    un_nombre = 2713
    print(2*un_nombre)
    
calculer()
```

Et des structures

```python
def tests():
    print("On va calculer un truc")
    if 2713/2 < 1000:
        print("lol")
    else:
        print("mdr")

tests()
tests()
```

```python
def boucles():
    for mot in ["Python", "c'est", "trop", "bien"]:
        print(mot)
    print()

boucles()
boucles()
boucles()
```

**REMARQUE IMPORTANTE** comme tous les noms que vous donnez en Python, que ce soit a des variables
ou à des fonctions, Python n'attache aucune signification au nom d'une fonction : du point de vue de
Python, les trois fonctions suivantes sont complètement équivalentes.

```python
def f():
    print("machin")

def machin():
    print("machin")

def une_fonction_nom_très_très_long():
    print("machin")
    
machin()
f()
une_fonction_nom_très_très_long()
```

En général on essaie de donner aux fonctions — comme aux variables — un nom **descriptif**, qui dit
ce que fait la fonction. Ça rend le code plus lisible pour les humains (dont vous) qui liront votre
code. Mais Python n'en a absolument rien à cirer et son comportement sera toujours le même, quel que
soit le nom que vous donnez.

### 🟠 Entraînements 🟠

1\. Écrire un programme dans lequel

- Vous définissez une fonction nommmée `dire_bonjour` qui affiche `"Bonjour les amis !"`.
- Vous appellez trois fois cette fonction.

```python
def dire_bonjour():
    print("Bonjour les amis !")

dire_bonjour()
dire_bonjour()
dire_bonjour()
```

2\. Écrire un programme dans lequel

- Vous définissez une fonction (du nom que vous voulez) qui affiche mille fois `"spam"`
- Vous appellez une fois cette fonction.

```python
def spam():
    for i in range(1000):
        print("spam")

spam()
```

3\. Écrire un programme dans lequel

- Vous définissez une fonction (du nom que vous voulez) qui affiche une fois `"spam"`
- Vous appellez mille fois cette fonction.

```python
def spam2():
    print("spam")
    
for i in range(1000):
    spam2()
```

4\. Refaire l'exercice 4 précédent, mais en utilisant une fonction pour les instructions qui
dessinent un carré.

## Des paramètres

Les fonctions natives que vous connaissez – comme `print` — acceptent souvent des **paramètres** :
les deux appels suivants donnent des comportements différents parce qu'on a pas mis la même chose
entre les parenthèses qui suivent `print`.

```python
print("Hello")
```

```python slideshow={"slide_type": ""}
print("felknmoizegnmoIFEN MOe fbMOZE FGNZEG OMINQZERGMOINQBZEGOMNIZERG")
```

Certaines fonctions acceptent même plusieurs paramètres, comme `circle` dans `turtle`.

<small>`print` accepte même un nombre quelconque de paramètres, mais c'est hors sujet pour l'instant
pour nous</small>


Est-ce qu'on peut avoir la même chose pour nos fonctions : bien sûr !

```python
def dire_un_machin(truc):
    print(truc)

dire_un_machin("Obéron")
dire_un_machin("est un très beau chat")
```

Le principe est le suivant : au moment où on définit la fonction avec `def`, on peut donner dans les
parenthèses une liste de noms de paramètres. Ces paramètres seront ensuite utilisable comme des
variables dans le corps de la fonction :

```python
def carre(n):
    print("Le carré de", n, "est", n**2)
    
carre(2)
carre(4)
carre(3)
```

Une fonction peut avoir plusieurs arguments

```python
def somme(a, jerome):
    som = a + jerome
    print(som)
    
somme(4, 12)
somme(7,100)
somme(2712, 1)
```

Là encore, les noms des arguments, c'est vous qui les décidez. Ils ne portent pas de sens pour
Python.


Les arguments peuvent être utilisés dans les structures qu'on a vues :

```python
def bonjour(lang):
    if lang == "fr":
        print("Bonjour")
    elif lang == "bzh":
        print("Demat")
    else:
        print("LANGUE INCONNUE")

bonjour("fr")
bonjour("en")
```

```python
def enumère(l):
    print("Dans ta liste, il y a:")
    for elem in l:
        print("L'élément", elem)

enumère([1, 2, 3, "carbone"])
```


## 😺 Entraînements 😺

(Pensez à tester vos fonctions)

1\. Définir une fonction nommée `triple` qui accepte un argument, supposé être un nombre, et affiche
son triple.

```python
def triple(n):
    print(3*n)
    
triple(4)
triple(-16)
triple(14)
```

2\. Définir une fonction nommée `crier` qui accepte un argument, supposé être une chaîne de
caractères, et affiche cette chaîne mise tout en majuscules.

```python
def crier(chn):
    s = str.upper(chn)
    print(s)

crier("wesh")
```

3\. Définir une fonction nommée `produit` qui accepte deux arguments et affiche leur produit. Tester
`produit(3, 4)` et `produit("spam ", 5)`.

```python
def produit(a, b):
    print(a*b)

produit(3, 4)
produit("spam ", 5)
```

4\. Définir une fonction `carré`, qui accepte un argument `c`, supposé être un nombre entier et
dessine à l'aide de `turtle` un carré de côté `c`.

## (Optionnel) arguments nommés et valeurs par défaut

Par défaut, les arguments sont lus dans l'ordre où ils apparaissent dans la définition

```python
def f(a, b):
    print("a vaut", a)
    print("b vaut", b)
    
f(1, 2)
print()
f("Bonjour", 4)
```

Mais on peut forcer à les lire dans un autre ordre en les nommant dans l'appel

```python
f(b=3, a=6)
```

Nommer les arguments dans l'appel est particulièrement utile quand une fonction a de nombreux
arguments.


Enfin on peut avoir des arguments optionnels avec la syntaxe suivante

```python
def ma_fonction(a, truc="salut"):
    print("a vaut", a)
    print("truc vaut", truc)
    
ma_fonction(15, 19)
print()
ma_fonction(15)
print()
ma_fonction(a="machin")
```
