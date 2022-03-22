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
Cours 8 : Manipulations de chaînes, itérables composites et dictionnaires
=========================================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-03-15
<!-- #endregion -->

Dans ce notebook

- Des méthodes pour convertir des chaînes de caractères en listes et *vice-versa*
- Des nouveaux itérables pour des boucles plus agréables
- Un nouveau type de données : les dictionnaires

## Encore des manipulations de chaînes 😤

Quelques nouvelles méthodes de manipulations de chaînes de caractères. On peut faire sans mais elles
sont très utiles.

### `replace`

`replace` **remplace** une chaîne de caractère dans une autre :

```python
message = "Salut poto. Ça fait plaisir de te voir, poto !"
nouveau_message = str.replace(message, "poto", "Alex")
print(message)
print(nouveau_message)
```

**Entraînement** : en utilisant les variables ci-dessous, affichez un message de bienvenue pour
chaque personne dans la liste `guests` :

```python
template = "Salut, [invité], ravi⋅e de te rencontrer !"
guests = ["Glimmer", "Bow", "Catra",]

# À toi de coder !
```

```python
template = "Salut, [invité], ravi⋅e de te rencontrer !"
guests = ["Glimmer", "Bow", "Catra",]

print(str.replace(template, "[invité]", guests[0]))
print(str.replace(template, "[invité]", guests[1]))
print(str.replace(template, "[invité]", guests[2]))
```

```python
template = "Salut, [invité], ravi⋅e de te rencontrer !"
guests = ["Glimmer", "Bow", "Catra",]

for g in guests:
    print(str.replace(template, "[invité]", g))
```

### `split`

`split` découpe, tronçonne, une chaîne de caractères

```python
texte = "You ever have that feeling, where you’re not sure if you’re awake or still dreaming?"
tokens = str.split(texte)
print(tokens)
```

C'est une façon rapide et simple (simpliste ?) de découper un texte en *tokens*.

Vous pouvez aussi utiliser un autre séparateur que les espaces :

```python
texte = "bleu|rouge|indigo|vert"
colours = str.split(texte, "|")
print(colours)
```

et les séparateurs peuvent être des chaînes arbitraires :

```python
texte = "bleu et rouge et indigo et vert"
colours = str.split(texte, " et ")
print(colours)
```

### `join`

`join` est d'une certaine façon l'inverse de `split` :

```python
names = ['Anna', 'Mary', 'John', 'Sebastian']
text = str.join(" and ", names)
print(text)
```

```python
letters = ['P', 'y', 't', 'h', 'o', 'n']
print(str.join("", letters))
```

### Utiliser les méthodes de chaîne

Ces méthodes peuvent aussi être utilisées directement, sans faire appel à `str` :

```python
texte = "bleu,rouge,indigo,vert"
colours = str.split(texte, ",")
print(colours)
```

est équivalent à

```python
texte = "bleu,rouge,indigo,vert"
colours = texte.split(",")
print(colours)
```

et

```python
names = ['Anna', 'Mary', 'John', 'Sebastian']
text = str.join(" and ", names)
print(text)
```

à

```python
names = ['Anna', 'Mary', 'John', 'Sebastian']
text = " and ".join(names)
print(text)
```

## D'autres façons d'itérer

Deux nouvelles fonctions qu'on utilise très souvent en Python. Là encore, on peut faire sans (par
exemple en utilisant `range`), mais elles rendent votre code plus lisible.

### `enumerate`

```python
liste = ["le", "petit", "chat", "est", "content"]
for truc in enumerate(liste):
    print(truc)
```

La fonction `enumerate`, appliqué à une séquence renvoie une **itérable** (comme `range`) dont les
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

C'est encore plus lisible et c'est le style recommandé en Python.

### `zip`

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


### Tuples

Un dernier point : c'est quoi exactement ces éléments que renvoient `zip` et `enumerate`, ça
ressemble à des listes mais avec des parenthèses ?

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
un_tuple = (1, "uh", "sense", 8, "machin", "truc")
print(un_tuple[0])
print(un_tuple[2:4])
```

La différence principale, c'est qu'ils sont **immutables**.

Ceci ne pose pas de problème :

```python
une_liste = [1, "uh", "sense", 8, "machin", "truc"]
une_liste[1] = "hey!"
print(une_liste)
```

Ceci est une erreur

```python tags=["raises-exception"]
un_tuple = (1, "uh", "sense", 8, "machin", "truc")
un_tuple[1] = "hey!"
print(un_tuple)
```

## Dictionnaires

On va faire une (brève) pause avec les boucles pour parler d'une nouvelle structure de données
omniprésente en Python : les dictionnaires.

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
On peut accéder à la valeur associé à une clé avec l'opération d'indexation dont vous avez
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

### Clés et valeurs

Les **valeurs** stockées dans un dictionnaire peuvent être n'importe quel objet, et une même valeur
peut apparaître plusieurs fois

```python
mon_dict = {
    "a": 1,
    "b": [1, 2, 3, 4, "hello"],
    "c": 1,
    "d": {"un dict": "dans un dict !"},
}
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
int_keys = {37: "hello", 9: "world"}
float_keys = {48.2: "hello", 3.0: "world"}
string_keys = {"hello": "world", "goodbye": "earth"}
bool_keys = {True: "hello", False: "world"}
```

Quelle est la taille maximale que peut atteindre un dictionnaire dont toutes les clés sont de type
`bool`.

## Étude de cas : les codes ISO 639

<!-- TODO: commencer plutôt par un Dict[str, str] et passer aux listes dans un second temps -->

Voici un dictionnaire qui contient une liste de quelques langues indexées par leur code [ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

```python
iso_639 = {
    "ny": ["Chichewa", "Chewa", "Nyanja"], 
    "zh": ["Chinese"], 
    "cs": ["Czech"], 
    "da": ["Danish"], 
    "dv": ["Divehi", "Maldivian"],
}
```

### Accéder aux éléments

On peut accéder aux listes de langues en utilisant leur clé

```python
print("La valeur de 'ny' est", iso_639["ny"])
print("La valeur de 'da' est", iso_639["da"])
```

**Question** En utilisant ce dictionnaire, modifier la cellule suivante pour afficher la chaîne
`"Chewa"`


```python

```

Si on veut simplement tester si une clé est présente, on peut utiliser l'opérateur `in` :

```python
print("ny" in iso_639)
print("fr" in iso_639)
```

### Ajouter et supprimer des éléments

On peut facilement ajouter un nouvel élément au dictionnaire :

```python
iso_639["ru"] = ["Russian"]
print(iso_639)
```

On peut aussi en supprimer, en utilisant le mot clé `del`

```python
iso_639["fr"] = ["French"]
print(iso_639)
del iso_639["fr"]
print(iso_639)
```

### Parcourir un dictionnaire

Les dictionnaires sont des **itérables**, et on peut les parcourir dans une boucle `for`.

```python
for language in iso_639:
    print(language)
```

**Attention** : ce sont les **clés** qu'on parcourt

### Entraînement

Modifier la boucle `for` ci-dessous pour qu'elle affiche la sortie suivante :

```text
ny -> ['Chichewa', 'Chewa', 'Nyanja']
zh -> ['Chinese']
cs -> ['Czech']
da -> ['Danish']
dv -> ['Divehi', 'Maldivian']
ru -> ['Russian']
```

```python
# Coder ici
for language in iso_639:
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
for i in range(len(fruits)):
    f = fruits[i]
    p = prix[i]
    tarifs[f] = p
print(tarifs)
```

Qu'on peut écrire plus proprement soit comme ceci

```python
fruits = ["pomme", "poire", "banane", "maracuja"]
prix = [0.50, 0.75, 1.0, 1.2]
tarifs = dict()
for i, f in enumerate(fruits):
    tarifs[f] = prix[i]
print(tarifs)
```

Ou encore mieux

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
`08_iterables_dictionnaires_PRENOM_NOM.ipynb` (pour Morgan Lefeuvre par exemple, ce serait
`08_iterables_dictionnaires_Morgan_Lefeuvre.ipynb`) et me le transmettre avant dimanche 2022-03-20
au soir.

- De préférence via [Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7694)
  (clé d'inscription `rossum`)
- À défaut, par mail, à `<lgrobol@parisnanterre.fr>`

Attention : **l'extension doit être `.ipynb`**.

### Présence et absence

Voici deux listes.

```python
text = ['a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', 
        'fruit', 'picking', 'there', 'try', 'little', 'around', 'appearances', 'appeared', 'all', 
        'crossed', 'basis', 'improbability', 'their', 'discworld', 'black', 'to', 'death', 'future', 
        'only', 'my', 'robe', 'things', 'for', 'it', 'existed', 'said', 'sake', 'sometimes', 'right', 
        'way', 'that', 'country', 'chessboard', 'quoth', 'well', 'domestic', 'skull', 'wonderful', 
        'hooded', 'or', 'empty', 'bottom', 'mirror', 'himself', 'rather', 'over', 'every', 'triangle', 
        'roses', 'border', 'orbiting', 'was', 'from', 'show', 'be', 'pecked', 'bones', 'just', 'universe', 
        'me', 'triangular', 'gets', 'worth', 'have', 'climbed', 'service', 'fluttered', 'top', 'but', 
        'grey', 'claws', 'at', 'rats', 'creep', 'own', 'pattern', 'point', 'white', 'than', 'dark', 
        'therefore', 'frame', 'this', 'not', 'the', 'could', 'mind', 'turtle', 'scrabble', 'better', 
        'industries', 'looked', 'an', 'cherubs', 'life', 'anything', 'more', 'small', 'and', 'of', 'his', 
        'on', 'skulls', 'elephants', 'in', 'thoughts', 'seen', 'nearest', 'expectantly', 'other', 'side', 
        'shape', 'total', 'so', 'world', 'look', 'sun']

words = ["shape", "linguistics", "every", "even", "world", "chessboard", "water", "sake"]
```

Créer un dictionnaire dont les clés sont les mots de la liste `words` et les valeurs associées sont
`True` si le mot est dans `text` et `False` sinon. Vous devriez obtenir quelque chose comme

```text
{'shape': True, 'linguistics': False, 'every': True, 'even': False, 'world': True, 
'chessboard': True, 'water': False, 'sake': True}
```

```python

```

## Encore des bigrammes

Voici un texte

```python
text = "It was dark, like the bottom of a well. There was a pattern of skulls and bones around \
the frame, for the sake of appearances; Death could not look himself in the skull in a mirror \
with cherubs and roses around it. The Death of Rats climbed the frame in a scrabble of claws and \
looked at Death expectantly from the top. Quoth fluttered over and pecked briefly at his own \
reflection, on the basis that anything was worth a try. Show me, said Death, show me my thoughts. \
A chessboard appeared, but it was triangular, and so big that only the nearest point could be seen. \
Right on this point was the world - turtle, elephants, the little orbiting sun and all. It was the \
Discworld, which existed only just this side of total improbability and, therefore, in border country. \
In border country the border gets crossed, and sometimes things creep into the universe that have \
rather more on their mind than a better life for their children and a wonderful future in the \
fruit picking and domestic service industries. On every other black or white triangle of the \
chessboard, all the way to infinity, was a small grey shape, rather like an empty hooded robe."
```

<!-- #region -->
1\. Écrire un programme qui génère la liste `unique_words`, qui contient tous les mots du texte,
sans doublons, et en minuscules. Le résultat devrait être le suivant (l'ordre peut être différent) :

```python
['a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', 'fruit', 'picking', 'there', 'try', 'little', 'around', 'appearances', 'appeared', 'all', 'crossed', 'basis', 'improbability', 'their', 'discworld', 'black', 'to', 'death', 'future', 'only', 'my', 'robe', 'things', 'for', 'it', 'existed', 'said', 'sake', 'sometimes', 'right', 'way', 'that', 'country', 'chessboard', 'quoth', 'well', 'domestic', 'skull', 'wonderful', 'hooded', 'or', 'empty', 'bottom', 'mirror', 'himself', 'rather', 'over', 'every', 'triangle', 'roses', 'border', 'orbiting', 'was', 'from', 'show', 'be', 'pecked', 'bones', 'just', 'universe', 'me', 'triangular', 'gets', 'worth', 'have', 'climbed', 'service', 'fluttered', 'top', 'but', 'grey', 'claws', 'at', 'rats', 'creep', 'own', 'pattern', 'point', 'white', 'than', 'dark', 'therefore', 'frame', 'this', 'not', 'the', 'could', 'mind', 'turtle', 'scrabble', 'better', 'industries', 'looked', 'an', 'cherubs', 'life', 'anything', 'more', 'small', 'and', 'of', 'his', 'on', 'skulls', 'elephants', 'in', 'thoughts', 'seen', 'nearest', 'expectantly', 'other', 'side', 'shape', 'total', 'so', 'world', 'look', 'sun']
```

(évidemment ne faites pas juste un copier-coller)

<!-- #endregion -->

```python

```

2\. Écrire un programme qui extrait à partir de la liste `unique_words` la liste `attested_bigrams`
des bigrammes de caractères qui apparaissent dans le texte.

**Indice** On a déjà écrit du code pour extraire des bigrammes dans une séance précédente.

```python

```

3\. Voici une liste des lettres de l'alphabet anglais. Utilisez-la pour générer une liste
`possible_bigrams` de tous les bigrammes de caractères théoriquement possibles en anglais.


```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

4\. Écrire un programme qui génère la liste `unattested_bigrams` des bigrammes de caractères
non attestés, c'est-à-dire de tous les bigrammes qui sont possibles, mais qu'on ne trouve pas dans
ce texte.

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


*Écrivez ici*
