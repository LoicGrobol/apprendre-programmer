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

# Cours 9 : Itérables et dictionnaires

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

Dans ce notebook

- Des boucles plus agréables avec les itérables
- Un nouveau type de données : les dictionnaires

## Itérables

### Entraînement

Écrire une fonction `index_chars` qui prend en argument une chaîne de caractères et affiche chacun
des caractères de la chaîne sur une nouvelle ligne, précédé de sa position dans la chaîne. Par
exemple pour `"linguistique"`:

```text
0 l
1 i
2 n
3 g
4 u
5 i
6 s
7 t
8 i
9 q
10 u
11 e
```

```python

```

<!-- #region -->

<details><summary>Solution</summary>

```python
def index_chars(chaine):
    n = 0
    for c in chaine:
        print(n, c)
        n = n + 1

index_chars("Nanterre")
```

</details>
<!-- #endregion -->

```python
def index_chars(chaine):
    n = 0
    for c in chaine:
        print(n, c)
        n = n + 1

index_chars("Nanterre")
```

<!-- TODO: changer la section suivante en rappel pour l'an prochain : on l'a fait dans le cours while -->

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

Un des usages très répandu de `range` est de permettre de parcourir à la fois une séquence et ses
indices : au lieu de ça :

```python
mot = "linguistique"
index = 0
for lettre in mot:
    print(lettre, " indice :", index)
    index = index + 1
```

on peut écrire ça :

```python
mot = "linguistique"
for index in range(len(mot)):
    print(mot[index], "indice :", index)
```

qui est plus compact, et *un peu* plus agréable (on a plus à gérer manuellement le compteur).

Pour notre fonction précédente ça donne donc

```python
def index_chars(s):
    for index in range(len(s)):
        print(index, mot[index])

index_chars("linguistique")
```

### `enumerate` : compter ses pas

```python
for truc in enumerate("linguistique"):
    print(truc)
```

```python
liste = ["le", "petit", "chat", "est", "content"]
for truc in enumerate(liste):
    print(truc)
```

```python
liste = ["le", 2713, None, True, ["ab", "c"], "e"]
for truc in enumerate(liste):
    print(truc)
```

```python
print(enumerate("linguistique"))
```

```python
print(type(enumerate("linguistique")))
```

```python
enumerate("linguistique")[5]
```

La fonction `enumerate`, appliqué à une séquence renvoie un **itérable** (comme `range`) dont les
éléments sont des couples `(indice, élément)` composés des éléments de la séquence. Ça permet de
remplacer ceci :

```python
mot = "linguistique"
for i in range(len(mot)):
    print(mot[i], " indice :", i)
```

par ceci

```python
mot = "linguistique"
for couple in enumerate(mot):
    print(couple[1], " indice :", couple[0])
```

qui est *un peu* plus lisible. On peut aussi utiliser la syntaxe suivante :

```python
mot = "linguistique"
for idx, lettre in enumerate(mot):
    print(lettre, " indice :", idx)
```

```python
a, b = 1, 2
print(a)
print(b)
```

C'est *vraiment* plus lisible. C'est le style *pythonique* (recommandé en Python). Pour notre
fonction, la meilleure solution c'est donc

```python
def index_chars(s):
    for i, c in enumerate(s):
        print(i, c)

index_chars("linguistique")
```

### `zip` : la fermeture éclair

```python
villes = ["Orléans", "Tours", "Nanterre"]
cp = ["45000", "37000", "92000"]

for i, v in enumerate(villes):
    print(v, cp[i])
```

```python
villes = ["Orléans", "Tours", "Nanterre"]
cp = ["45000", "37000", "92000"]

for truc in zip(villes, cp):
    print(truc)
```

`zip` permet d'itérer sur plusieurs séquences en parallèle

```python
villes = ["Orléans", "Tours", "Nanterre"]
cp = ["45000", "37000", "92000"]
appreciation = ["cool", "génial", "super"]

for truc in zip(villes, cp, appreciation):
    print(truc)
```

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021"]
appreciation = ["cool", "génial", "super"]

for truc in zip(villes, annee, appreciation):
    print("Où:", truc[0], "Quand:", truc[1], "Comment:", truc[2])
```

Là aussi on peut utiliser cette nouvelle syntaxe pour que ce soit plus lisible :

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021"]
appreciation = ["cool", "génial", "super"]

for ou, quand, comment in zip(villes, annee, appreciation):
    print("Où:", ou, "Quand:", quand, "Comment:", comment)
```

Est-ce que vous voyez comment simuler `enumerate` en utilisant `zip` ?

```python
mot = "linguistique"

for i, c in zip(range(len(mot)), mot):
    print(c, " indice :", i)
```

Un truc récent depuis Python 3.12 (?), le paramètre `strict`.

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021", "2024"]

for v, a in zip(villes, annee):
    print(a, v)
```

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021", "2024"]

for v, a in zip(villes, annee, strict=True):
    print(a, v)
```

### Tuples

Un dernier point : c'est quoi exactement ces éléments que renvoient les itérations sur des `zip` e
des `enumerate`, ça ressemble à des listes, mais avec des parenthèses ?

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021"]
appreciation = ["cool", "génial", "super"]

for truc in zip(villes, annee, appreciation):
    print(type(truc))
```

Ce sont des `tuple`s, effectivement ça ressemble à des listes, mais pas tout à fait.

```python
un_tuple = (1, 2, 3, 4)
print(un_tuple)
print(type(un_tuple))
```

```python
un_tuple = (1, "uh", 8, (2, 7, 1, "a"), "machin", [1, 2], "truc")
print(un_tuple[0])
print(un_tuple[2:4])
```

La différence principale, c'est qu'ils sont **immutables**.

Ceci ne pose pas de problème :

```python
une_liste = [1, "uh", "sense", 8, "machin", "truc"]
print(une_liste)
une_liste[1] = "hey!"
print(une_liste)
```

Ceci est une erreur

```python tags=["raises-exception"]
un_tuple = (1, "uh", "sense", 8, "machin", "truc")
print(un_tuple)
un_tuple[1] = "hey!"
print(un_tuple)
```

```python
une_liste = [1, "uh", "sense", 8, "machin", "truc"]
print(une_liste)
une_liste.append("hey!")
print(une_liste)
```

```python tags=["raises-exception"]
un_tuple = (1, "uh", "sense", 8, "machin", "truc")
print(un_tuple)
un_tuple.append("hey!")
print(un_tuple)
```

## Dictionnaires

On va faire une pause avec les boucles pour parler d'une nouvelle structure de données omniprésente
en Python : les dictionnaires.

On a vu des structures de données ordonnées comme les listes et les chaînes de caractères qui
permettent d'accéder à leurs éléments *via* des indices numériques.

Les dictionnaires sont une extension de ce concept à une situation où les indices ne sont pas des
entiers, mais peuvent être des données arbitraires, on parle alors de **clés**.

On crée un dictionnaire (du type `dict`) avec la syntaxe suivante :

```python
dico = {"éclair": "une pâtisserie", "Python": "un langage", "mot de passe": 2048, 8: "sense"}
print(type(dico))
print(dico)
```

Quand ils sont longs, on peut les noter sur plusieurs lignes :

```python
dico = {
    "éclair": "une pâtisserie de forme longue et de courte durée",
    "Python": "un langage de programmation créé par Guido van Rossum",
    "mot de passe": 15331,
    8: "the number of sensates in a cluster",
}
print(dico)
```

Dans la notation `{k: v}`, on dit que `k` est une **clé** et `v` est la **valeur** associée à `k`.
On peut accéder à la valeur associée à une clé avec l'opération d'indexation dont vous avez
l'habitude :

```python
dico = {"éclair": "une pâtisserie", "Python": "un langage", "mot de passe": 2048, 8: "sense"}
v = dico["éclair"]
print(v)
print(dico["Python"])
print(dico[8])
```

Et on peut ajouter un couple clé/valeur ou modifier le dictionnaire de la même façon

```python
mon_dictionnaire = {"machin": 3, "truc": "bidule"}
print(mon_dictionnaire)
mon_dictionnaire["machin"] = "chose"
print(mon_dictionnaire)
mon_dictionnaire["Horizon"] = "Zero Dawn"
print(mon_dictionnaire)
```

Pour créer un dictionnaire vide, on utilise `dict()` :

```python
mon_dictionnaire = dict()
print(mon_dictionnaire)
mon_dictionnaire["machin"] = "chose"
print(mon_dictionnaire)
mon_dictionnaire["Horizon"] = "Zero Dawn"
print(mon_dictionnaire)
```

```python
locals()
```

### Clés et valeurs

Les **valeurs** stockées dans un dictionnaire peuvent être n'importe quel objet et une même valeur
peut apparaître plusieurs fois

```python
mon_dict = {
    "a": 1,
    "b": [1, 2, 3, 4, "hello"],
    "c": 1,
    "d": {"un dict": "dans un dict !"},
}
print(mon_dict)
```

```python
mon_dict = {
    "a": 1,
    "b": [1, 2, 3, 4, "hello"],
    "c": 1,
    "d": {"un dict": "dans un dict !"},
}
la_liste = mon_dict["b"]
print(la_liste)
print(la_liste[2])
print((mon_dict["b"])[2])
print(mon_dict["b"][2])
```

```python
mon_dict = {
    "a": 1,
    "b": [1, 2, 3, 4, "hello"],
    "c": 1,
    "d": {"un dict": "dans un dict !", "a": "bcd"},
}
le_dico = mon_dict["d"]
print(le_dico )
print(le_dico["un dict"])
print(mon_dict["d"])
print(mon_dict["d"]["a"])
```

Les clés en revanche sont uniques (ou plus exactement, chaque clé n'est associée qu'à une seule
valeur) :

```python
mon_dict = {
    "a": "truc",
    "b": "machin",
    "a": "chose",
}
print(mon_dict)
```

De plus les clés ne peuvent pas être des objets **mutables** — dont on peut modifier la valeur —
comme les listes ou les dictionnaires :

```python tag=["raises-exception"]
mon_dict = {
    ["a", "b"]: "truc",
    "b": "machin",
}
```

À votre avis pourquoi ?

Ça vous laisse quand même une grande latitude :

```python
int_keys = {13: "hello", 12: "world"}
float_keys = {48.2: "hello", 3.0: "world"}
string_keys = {"hello": "world", "goodbye": "earth"}
bool_keys = {True: "hello", False: "world"}
tuple_keys = {("a", "b"): "hello", 2713: "world"}
```

Quelle est la taille maximale que peut atteindre un dictionnaire dont toutes les clés sont de type
`bool` ?

## Étude de cas : les codes ISO 639

Voici un dictionnaire qui contient une liste de quelques langues indexées par leur code
[ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

```python
iso_639 = {
    "ny": "Chewa", 
    "zh": "Chinese",
    "cs": "Czech", 
    "da": "Danish",
    "dv": "Divehi",
    "br": "Breton",
    "gcf": "Guadeloupean Creole French",
}
```

### Accéder aux éléments

On peut accéder aux noms de langues en utilisant leur clé

```python
print("La valeur de 'ny' est", iso_639["ny"])
print("La valeur de 'da' est", iso_639["da"])
```

**Question** En utilisant ce dictionnaire, modifier la cellule suivante pour afficher la chaîne
`"Divehi"`

```python
print(iso_639["ny"])
```

Si on veut simplement tester si une clé est présente, on peut utiliser l'opérateur `in` :

```python
print("ny" in iso_639)
print("fr" in iso_639)
```

### Ajouter et supprimer des éléments

On peut facilement ajouter un nouvel élément au dictionnaire :

```python
iso_639["ru"] = "Russian"
print(iso_639)
```

On peut aussi en supprimer, en utilisant le mot clé `del` :

```python
iso_639["fr"] = "French"
print(iso_639)
del iso_639["fr"]
print(iso_639)
```

### Parcourir un dictionnaire

Les dictionnaires sont des **itérables**, et on peut les parcourir dans une boucle `for` :

```python
for language in iso_639:
    print(language)
```

**Attention** : ce sont les **clés** qu'on parcourt

### Entraînement

En utilisant la variable suivante,

```python
iso_639 = {
    "ny": "Chewa", 
    "zh": "Chinese", 
    "cs": "Czech", 
    "da": "Danish", 
    "dv": "Divehi",
    "br": "Breton",
}
```

Modifier la cellule ci-dessous pour qu'elle affiche la sortie suivante :

```text
ny -> Chewa
zh -> Chinese
cs -> Czech
da -> Danish
dv -> Divehi
ru -> Russian
```

```python
for language in iso_639:
    # Modifier ici
    print(language)
```

### Parcourir les paires clé/valeur

Si on veut parcourir un dictionnaire en accédant aux couples clé/valeur (ce qui arrive souvent), on
peut utiliser la méthode `items`.

```python
for pair in iso_639.items():
    print("Paire:", pair)
    print("Clé:", pair[0])
    print("Valeur:", pair[1])
    print()
```

Quel est le type de `pair` dans la boucle ci-dessus ?

On peut aussi l'écrire ainsi :

```python
for cle, valeur in iso_639.items():
    print("Clé:", cle)
    print("Valeur:", valeur)
    print()
```

### Créer un dictionnaire

Une recette courante consiste à créer un dictionnaire dans une boucle à partir du contenu
d'itérables, par exemple ici pour une liste de fruits avec leurs prix :

```python
fruits = ["pomme", "poire", "banane", "maracuja"]
prix = [0.50, 0.75, 1.0, 1.2]
tarifs = dict()
for f, p in zip(fruits, prix):
    tarifs[f] = p
print(tarifs)
```

On peut aussi le faire avec n'importe quelle expression

```python
mots = ["il", "y", "a", "un", "lama", "dans", "mon", "salon"]
commence_par_une_voyelle = dict()
for le_mot in mots:
    if le_mot[0] in "aeiouyàéèêïôùÿ":
        commence_par_une_voyelle[le_mot] = True
    else:
        commence_par_une_voyelle[le_mot] = False
print(commence_par_une_voyelle)
```

## Exercices

Répondre à ces exercices directement dans le notebook, le sauvegarder sous un nom de la forme
`09_iterables_Prénom_Nom.ipynb` (pour Morgan Lefeuvre par exemple, ce serait
`09_iterables._Morgan_Lefeuvre.ipynb`) et me le transmettre

- De préférence via [Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7694)
  (clé d'inscription `rossum`)
- À défaut, par mail, à `<lgrobol@parisnanterre.fr>`

Attention : **l'extension doit être `.ipynb`**.

N'hésitez pas à revenir sur les cours et les corrigés précédents pour trouver des idées.

### Consonnes

Voici une liste de voyelles

```python
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]
```

Écrire une fonction `compte_consonnes` qui prend un mot en argument et renvoie le nombre de
consonnes (donc de lettre qui ne sont pas de voyelles) dans ce mot.

```python

```

### 🍄 Accumuler dans une liste 🍄

Écrire un programme qui demande à l'utilisateurice de saisir les uns après les autres ses cinq
aliments préférés. Stocker ces réponses dans une liste, puis affichez les éléments de cette liste,
chacun sur une ligne.

```python

```

### ⚒️ N-grammes ⚒️

Le concept de **n-gramme** est fondamental en TAL. Un n-gramme, c'st une suite de $n$ symboles. Par
exemple dans le mot « banane », les 2-grammes (bigrammes) de caractères sont :

- ba
- an
- na
- ne

Et dans le mot « linguiste », les 3-grammes (trigrammes) de caractères sont :

- lin
- ing
- ngu
- gui
- uis
- ist
- ste

1\. Écrire une fonction `get_bigrams` qui prend en argument un mot (sous forme d'une chaîne de
caractères) et renvoie la liste de tous les bigrammes de caractères de ce mot, sans doublons.

```python

```

2\. Écrire une fonction `get_ngrams` qui prend en argument un mot et un entier `n` et renvoie la
liste des n-grammes de caractères de ce mot, sans doublons.

Indices :

- Attention aux cas particuliers : que faire des `n` premiers et derniers caractères du mot ? Que
  faire si le mot fait moins de n caractères…

```python

```

### Réflexion

Quelques questions sur votre travail :

- Combien de temps avez-vous passé à faire ces exercices ?
- Combien de temps avez-vous passé à relire le cours (ou les cours précédents) ?
- Avez-vous l'impression d'avoir bien mémorisé les concepts et les techniques vus jusqu'ici ?
- Qu'est-ce qui vous paraît le plus compliqué ?
- À votre avis, pourquoi ?

Merci de bien répondre à chacune de ces questions dans la cellule de texte ci-dessous (n'oubliez pas
de l'exécuter avant de sauvegarder) : elles me permettent d'ajuster le cours en fonction de vos
besoins, avec un peu de chance, elles devraient également vous aider à guider votre travail et à
apprécier votre progression.
