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
Cours 6 : Corrections
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

## Sorties


> 1\. Écrire dans la cellule ci-dessous un programme qui affiche votre nom complet, comme ceci :
> 
> ```text
> Loïc Grobol
> ```

```python
print("Loïc Grobol")
```

> 2\. Écrire dans la cellule ci-dessous un programme qui affiche votre année et votre lieu de
> naissance, séparés par une ligne vide, comme ceci :
> 
> ```text
> 1991
> 
> Orléans
> ```

```python
print("1991")
print()
print("Orléans")
```

## Types de base et opérations

> 1\. Affichez les résultats des calculs suivants : $2713+4096$, $\frac{12-75}{3}$, $2^{10}$,
> $(-1)^{45+766}$ et $(512-256)\times\left(-\frac{3}{2}\right)$.

```python
print(2713+4096)
print(12-75)
print(2**10)
print((-1)**(46+766))
print((512-256)*(-3/2))
```

Pour le dernier, on aurait aussi pu écrire `(512-256)*(-(3/2))`, mais comme
$-\frac{3}{2}=\frac{-3}{2}$, ça revient au même.

> 2\. Construire et afficher une chaîne de caractères composée de $4096$ répétition des caractères
> `UPX>*`.

```python
print(4096*"UPX>*")
```

> 3\. Construire et afficher une chaîne de caractères contenant `This is fine` suivie de $1024$ fois
> `🔥`.

```python
print("This is fine" + 1024*"🔥")
```

> 4\. Déterminer sans les exécuter les valeurs de retour des instructions suivantes, écrivez les
> résultats dans la cellule de texte en-dessous.


```python
True or True
```

```python
True or False
```


```python
False and False
```

```python
(False or True) and True
```

```python
False or (True and True)
```

```python
("machin" in "truc") and (1 + 1 == 2)
```

```python
("a" in "apples") or (1 + 1 == 5)
```


```python
("apples" in "a") or (1 + 1 == 5)
```

```python
(("apple" in "apples") and (1 + 1 == 3)) or (5 < 10)
```

## Opérations sur les chaînes de caractères


> 1\. Mettre en minuscules la chaine de caractères `"ILliil1ILiiIILLL!1lIÎï"` et afficher le
> résultat.

```python
print(str.lower("ILliil1ILiiIILLL!1lIÎï"))
```

> 2\. Mettre en casse de titre la chaîne de caractères `Les maîtres de l'ombre` et afficher le
> résultat.

```python
print(str.title("Les maîtres de l'ombre"))
```

## Variables

> 1\. Compléter la cellule suivante afin d'afficher la valeur de la variable `spam`

```python
spam = "spam, spam, lovely spam"
print(spam)
```

```python
type(spam)
```

> 2\. Créer une variable contenant la chaîne de caractère `"Bonjour, tout le monde"`

```python
message = "Bonjour, tout le monde"
```

> 3\. Stocker le résultat du calcul suivant dans une variable et afficher son résultat :
> $\frac{36}{5}$

```python
res = 36/5
print(res)
```

> 4\.
>
> 1. Stocker $86$ dans une variable et $33$ dans une autre.
> 2. Stocker la somme dans une autre variable et afficher le résultat.
> 3. Afficher le type de la somme.

```python
un_nombre = 86
un_autre_nombre = 33
la_somme = un_nombre + un_autre_nombre
print(la_somme)
print(type(la_somme))
```

> 5\. Même chose que 4., mais avec les valeurs `"py"` et `"thon"`.

```python
une_chaine = "py"
une_autre_chaine = "thon"
la_concaténation = une_chaine + une_autre_chaine
print(la_concaténation)
print(type(la_concaténation))
```

## Entrées

> 1\. Demander la saisie d'un nombre et afficher son triple.

```python tags=["skip-execution"]
entree = int(input("Dis-moi un nombre: "))
print(3*entree)
```

Attention à ne pas oublier le `int`.

> 2\. Demander la saisie d'une chaîne de caractères et l'afficher tout en majuscules.

```python tags=["skip-execution"]
entree = input("Dis-moi quelque chose: ")
print(str.upper(entree))
```

> 3\. Demander la saisie d'une chaîne de caractères. Afficher `True` si elle contient `spam` et
> `False` sinon.

```python tags=["skip-execution"]
entree = input("Dis-moi quelque chose: ")
print("spam" in entree)
```

> 4\. Écrire un programme qui demande à son utilisateurice son année de naissance et affiche l'âge
> qu'aura cette personne en 2050.

```python tags=["skip-execution"]
annee = int(input("Tu es né⋅e quand ? "))
age_2050 = 2050-annee
print("En 2050, tu auras", age_2050, " ans")
```

## Instruction conditionnelle `if`

> 1\. Écrire un programme qui affiche `trop petit` si le résultat du calcul $\frac{2^{11}}{3}$ est
> plus petit que $1000$ sans jamais afficher le résultat du calcul lui-même.

```python
if (2**11)/3 < 1000:
    print("trop petit")
```

> 2\. Demander la saisie d'une chaîne de caractères en posant la question `"Voyelle ou
> consonne ?"`. Afficher `a` si la saisie est `"voyelle"`, `b` si la saisie est `"consonne"`.
> N'affichez rien pour toute autre saisie.

```python tags=["skip-execution"]
entree = input("Voyelle ou consonne ? ")
if entree == "voyelle":
    print("a")
elif entree == "consonne":
    print("b")
```

> 3\. Demander la saisie d'une chaîne de caractères contenant un nombre. Afficher `🥶` si ce nombre
> est inférieur à $5$, $😌$ s'il est entre $5$ et $16$ et $🥵$ sinon.

```python tags=["skip-execution"]
temp = int(input("Dis-moi une température: "))
if temp < 5:
    print("🥶")
elif 5 <= temp < 16:
    print("😌")
else:
    print("🥵")
```

On pouvait aussi écrire `5 <= temp and temp < 16` pour la deuxième condition ou l'échanger avec la
condition `else`.

> 4\. Demandez à votre utilisateurice de saisir sa couleur préférée :
>
> - Si la réponse contient `rouge`, affichez `🟥!`.
> - Si la réponse contient `vert`, affichez `🟩!`.
> - Si la réponse contient `violet` ou `indigo`, affichez `💜!`.
> - Si la réponse est n'importe quoi d'autre, demandez `Tu penses avoir bon goût ?`.
>   - Si la réponse à cette deuxième question est `oui`, affichez `😂`
>   - Sinon, affichez `👉👉`

```python tags=["skip-execution"]
col = input("C'est quoi ta couleur préférée ? ")
if "rouge" in col:
    print("🟥!")
elif "vert" in col:
    print("🟩!")
elif "violet" in col or "indigo" in col:
    print("💜!")
else:
    taste = input("Tu penses avoir bon goût ? ")
    if taste == "oui":
        print("😂")
    else:
        print("👉👉")
```

On pouvait utiliser `str.lower` pour rendre ça plus sympa.

## Séquences et listes

> 1\. En utilisant uniquement les chaînes de caractères déjà définies (pas forcément toutes) dans la
> cellule-ci dessous, modifiez cette cellule pour afficher `le nouveau monde tarde à apparaître`

```python
lst = [" ", "le", "nouveau", "monde", "tarde", "à", "apparaître"]
print(
    lst[1] + lst[0]
    + lst[2] + lst[0]
    + lst[3] + lst[0]
    + lst[4] + lst[0]
    + lst[5] + lst[0]
    + lst[6]
)
```

En prenant un peu d'avance

```python
lst = [" ", "le", "nouveau", "monde", "tarde", "à", "apparaître"]
print(str.join(lst[0], lst[1:]))
```

> 2\. Même question

```python
lst = [" ", "le", "nouveau", ["monde", "tarde", "à"], "apparaître"]
print(
    lst[1] + lst[0]
    + lst[2] + lst[0]
    + lst[3][0] + lst[0]
    + lst[3][1] + lst[0]
    + lst[3][2] + lst[0]
    + lst[4]
)
```

> 3\. Même question

```python
lst = [" ", "le", "nouveau", ["monde", ["tarde"], "à"], "apparaître"]
print(
    lst[1] + lst[0]
    + lst[2] + lst[0]
    + lst[3][0] + lst[0]
    + lst[3][1][0] + lst[0]
    + lst[3][2] + lst[0]
    + lst[4]
)
```

> 4\. Même question

```python
lst = [" ", "le", "nouveau", "apparaître monde tarde à"]
print(
    lst[1] + lst[0]
    + lst[2] + lst[0]
    + lst[3][11:16] + lst[0]
    + lst[3][17:22] + lst[0]
    + lst[3][23] + lst[0]
    + lst[3][:10] + lst[0]
)
```

On pouvait aussi utiliser les espaces de `lst[3]` directement, par exemple `lst[3][:11]` au lieu de
`lst[3][:10] + lst[0]`.

Ou, en prenant beaucoup d'avance :

```python
lst = [" ", "le", "nouveau", "apparaître monde tarde à"]
lst2 = str.split(lst[3])
print(str.join(lst[0], [*lst[1:3], *lst2[1:], lst2[0]]))
```

> 5\. Même question

```python
lst = [" ", "le", [[[["nouveau"]]]], "apparaître monde tarde à"]
print(
    lst[1] + lst[0]
    + lst[2][0][0][0][0] + lst[0]
    + lst[3][11:16] + lst[0]
    + lst[3][17:22] + lst[0]
    + lst[3][23] + lst[0]
    + lst[3][:10] + lst[0]
)
```

> 6\. Même question en utilisant que des nombres négatifs ou nuls

```python
lst = [" ", "le", "nouveau", ["monde", "tarde", "à"], "apparaître"]
print(
    lst[-4] + lst[0]
    + lst[-3] + lst[0]
    + lst[-2][0] + lst[0]
    + lst[-2][-2] + lst[0]
    + lst[-2][-1] + lst[0]
    + lst[-1]
)
```

> Bonus : en utilisant que des nombres strictement négatifs.

```python
lst = [" ", "le", "nouveau", ["monde", "tarde", "à"], "apparaître"]
space = lst[::-1][-1]
print(
    lst[-4] + lst[-5]
    + lst[-3] + lst[-5]
    + lst[-2][-3] + lst[-5]
    + lst[-2][-2] + lst[-5]
    + lst[-2][-1] + lst[-5]
    + lst[-1]
)
```

## Édition de listes

> 1\. Modifiez la liste suivante à l'aide des instructions ci-dessus pour former l'alphabet latin

```python
lst = ["a", "b", "c", "g", "g", "g", "h", "i", "j", "spam", "k", "l", 1, "m", "n", "o", "p", "q", "r", "s", "t", "v"]
lst.remove("g")
lst.remove("g")
lst.remove("spam")
lst.remove(1)
lst.insert(3, "f")
lst.insert(3, "e")
lst.insert(3, "d")
lst.insert(-1, "u")
lst.extend(["w", "x", "y", "z"])
print(lst)
```

## Boucles d'itération

> 1\. Afficher sur des lignes séparées les carrés de nombres de la liste suivante :

```python
lst = [1, 3, 1, 2, 10, -75]
for elem in lst:
    print(elem**2)
```

> 2\. En utilisant une boucle les mots suivants, chacun sur une ligne, en casse de titre (avec
> `str.title`)

```python
words = ["tRAIteMENT", "automAtique", "du", "langage", "à", "l'", "universitÉ", "paris", "nanterre"]
for mot in words:
    print(str.title(mot))
```

> 3\. Pour chacune des familles de langues indo-européennes de la liste suivante, demandez à
> l'utilisateurice d'entrer une langue de la famille. Stockez ces entrées dans une liste et affichez
> cette liste à la fin.

```python tags=["skip-execution"]
familles = ["Romanes", "Germaniques", "Balto-slaves", "Celtiques", "Indo-ariennes"]
langues = []
for fam in familles:
    lng = input("Entrer une langue " + fam + ": ")
    langues.append(lng)
print(langues)
```

## Power of Thor

> [Power of Thor E01](https://www.codingame.com/training/easy/power-of-thor-episode-1)

<!-- #region -->

On peut penser à une première version basique : on cherche d'abord à avoir la bonne abscisse, puis
la bonne ordonnée :

```python
# Code original pour réupérer les positions
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# **AJOUTS** on garde en mémoire la position actuelle
current_tx = initial_tx
current_ty = initial_ty

while True:
    # À conserver pour faire plaisir à CodinGame
    remaining_turns = int(input())

    if light_x > current_tx:
        print("E")
        current_tx = current_tx + 1
    elif light_x < current_tx:
        print("W")
        current_tx = current_tx - 1
    # Attention : les ordonnées vont de haut en bas
    elif light_y > current_ty:
        print("S")
        current_ty = current_ty + 1
    else:
        print("N")
        current_ty = current_ty - 1
```

Problème, ça ne marche pas pour le test 4 « *optimal angle* ». Ce qui cloche c'est qu'on utilise pas
les diagonales, ce qui nous fait perdre du temps. On peut arranger ça en combinant les cas quand on
doit changer à la fois d'abscisse et d'ordonnée :

```python
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_tx = initial_tx
current_ty = initial_ty

while True:
    remaining_turns = int(input())

    if light_x > current_tx:
        if light_y > current_ty:
            print("SE")
            current_ty = current_ty + 1
        elif light_y < current_ty:
            print("NE")
            current_ty = current_ty - 1
        else:
            print("E")
        current_tx = current_tx + 1
    elif light_x < current_tx:
        if light_y > current_ty:
            print("SW")
            current_ty = current_ty + 1
        elif light_y < current_ty:
            print("NW")
            current_ty = current_ty - 1
        else:
            print("W")
        current_tx = current_tx - 1
    elif light_y > current_ty:
        print("S")
        current_ty = current_ty + 1
    else:
        print("N")
        current_ty = current_ty - 1
```

Ce coup-ci ça marche, par contre, c'est très verbeux : on se répète beaucoup. Voici une solution
plus compacte en déterminant indépendamment les déplacements sur chacun des axes et en combinant les
résultats à la fin :

```python
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_tx = initial_tx
current_ty = initial_ty

while True:
    remaining_turns = int(input())
    
    if light_x > current_tx:
        direction_ew = "E"
        current_tx = current_tx + 1
    elif light_x < current_tx:
        direction_ew = "W"
        current_tx = current_tx - 1
    else:
        direction_ew = ""
    
    if light_y > current_ty:
        direction_sw = "S"
        current_ty = current_ty + 1
    elif light_y < current_ty
        direction_sw = "N"
        current_ty = current_ty - 1
    else:
        direction_sw = ""

    print(direction_sw + direction_ew)
```

Comme d'habitude, il y a beaucoup d'autres solutions et en particulier des beaucoup plus compactes. C'est un bon entraînement de chercher la façon de résoudre ce problème en un minimum de caractères, on dit qu'on fait du *Code Golf*.

<!-- #endregion -->