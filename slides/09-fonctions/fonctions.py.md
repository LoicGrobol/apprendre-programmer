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
- `pensize(e)` épaisseur du tracé (pixels)$
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

Vous connaissez `print` et `input` et `len`.

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
ce que fait la fonction. Ça rend le code plus lisibles pour les humains (dont vous) qui liront votre
code. Mais Python n'en a absolument rien à cirer et son comportement sera toujours le même, quel que
soit le nom que vous donnez.

### 🟠 Entraînements 🟠

1\. Écrire une fonction nommmée `dire_bonjour` qui affiche `"Bonjour les amis !"` et écrire un
programme qui appelle trois fois cette fonction.

2\. Écrire un programme dans lequel

- Vous définissez une fonction (du nom que vous voulez) qui affiche mille fois `"spam"`
- Vous appellez une fois cette fonction.

3\. Écrire un programme dans lequel

- Vous définissez une fonction (du nom que vous voulez) qui affiche une fois `"spam"`
- Vous appellez une fois cette fonction.

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
def dire_un_truc(truc):
    print(truc)

dire_un_truc("Obéron")
dire_un_truc("est un très beau chat")
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
    if langue == "fr":
        print("Bonjour")
    elif langue == "bzh":
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

## 😺 Entraînements 😺

(Pensez à tester vos fonctions)

1\. Définir une fonction nommée `triple` qui accepte un argument, supposé être un nombre, et affiche
son double.

2\. Définir une fonction nommée `crier` qui accepte un argument, supposé être une chaîne de
caractères, et affiche cette chaîne mise tout en majuscules.

3\. Définir une fonction nommée `produit` qui accepte deux arguments et affiche leur produit. Tester
`produit(3, 4)` et `produit("spam ", 5)`.

4\. Définir une fonction `carré`, qui accepte un argument `c`, supposé être un nombre entier et
dessine à l'aide de `turtle` un carré de côté `c`.

## Valeur de retour

Pour l'instant, les fonctions qu'on a définies affichent toujours quelque chose. Ce n'est pas une
obligation :

```python
def ssss(arg):
    bidule = arg*2
    for i in range(10):
        bidule = bidule + arg
        
ssss(3)
```

Ici, la fonction `ssss` a bien été exécutée, mais elle ne fait rien de visible.


Par contre, remarquez un truc : parfois dans le passé, on a stocké le résultat de fonctions dans des
variables. Par exemple

```python
longueur = len("anticonstitutionnellement")
```

On a bien appelé la fonction `len`, qui n'affiche rien. Donc rien ne s'affiche.


En revanche, on a bien fait quelque chose ici : on a donnée une valeur à la variable `longueur`.

```python
print(longueur)
```

Autrement dit, `len` ne fait pas un affichage : elle transmet plutôt une information : la longueur
de son argument.



Et nos fonctions, elles passent une information ?

```python
def bonjour():
    print("Salut")
    
varbl = bonjour()
```

Pas vraiment :

```python
print(varbl)
```

Elles passent en fait toutes la valeur `None` : un objet spéciale de Python qui signifie
littéralement « rien ».


Comment on fait alors ? On leur donne une **valeur de retour** avec le mot-clé `return` :

```python
def renvoi():
    return "Salut"

varbl = renvoi()
```

Vous voyez la différence ? On a rien affiché ici. Par contre :

```python
print(varbl)
```

on a bien **renvoyé** une valeur.


Renvoyer une valeur, c'est surtout utile quand on a des paramètres, on va pas se mentir (sinon on
renvoie toujours la même chose, pas vraiment la peine de faire une fonction, une vairiable
suffirait.

```python
def somme(a, b):
    return a+b

a = somme(5, 10)
print(a)
```

Et comme d'habitude, vous pouvez mettre un appel de fonction partout où vous pouvez écrire une
valeur littérale :

```python
print(somme(12, 75))
```

```python
print(somme("ha", "ha"))
```

**Attention** maintenant à bien faire la différence :


Cette fonction **affiche** quelque chose et ne **renvoie** rien (ou `None`)

```python
def affiche(arg):
    print("Mon argument est " + arg)

ret = affiche("thing")
print(ret)
```

Celle-ci n'**affiche** rien et **renvoie** quelque chose

```python
def renvoie(arg):
    return "Mon argument est " + arg

ret = renvoie("thing") # Ceci n'affiche rien
print(ret)
```

Celle-ci fait les deux

```python
def porquenolosdos(arg):
    print("Voici mon argument: " + arg)
    return "Mon argument est " + arg

ret = porquenolosdos("thing")
print(ret)
```

## ↩️ Entraînements ↩️

1\. Écrire une fonction sans arguments, qui renvoie le nombre `2713`

2\. Écrire une fonction qui accepte un argument et renvoie son double

3\. Écrire une fonction qui accepte deux arguments, affiche la valeur du premier et renvoie le
triple du deuxième

4\. Écrire une fonction qui accepte un argument, supposé être une liste, qui affiche le premier
élément de cette liste et renvoie la valeur du dernier.

5\. Écrire une fonction qui accepte un argument, supposé être une liste de chaînes de caractères,
qui renvoie la plus longue chaîne de la liste.
