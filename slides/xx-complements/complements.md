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
Cours XX : Complements
=================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

xxxx-xx-xx
<!-- #endregion -->

Dans ce notebook, tous les trucs qu'on a pas vu dans le cours faute de temps.

## Compléments

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

### Changement de casse

Un concept important en TAL est celui de « sac de mots ». Il s'agit d'un modèle sémantique très
simple où on fait l'hypothèse que le sens d'un texte peut être représenté par la liste des mots
qu'il contient et leurs nombres d'occurrence. Intuitivement, si un texte par d'animaux de compagnie,
on s'attend à rencontre plus souvent les mots *chat* ou *chien* que s'il s'agit d'un texte sur la
politique française.

Certains mots, cependant, apparaissent à peu près avec la même fréquence dans tous les types de
textes : *et*, *un*, *la*… On les appelle parfois « mots vides » ou « *stop words* », puisqu'ils
n'apportent pas d'information pour ce modèle, et on commence en général par les enlever des textes à
représenter.

De même, pour beaucoup d'applications en linguistique, la casse (majuscules et minuscules) n'est pas
informative. Par exemple pour enlever les *stop words* d'un texte, on veut les enlever peu importe
leur casse (*Un*, *un*, *UN*…). Cependant, pour Python, *Un* et *un* des chaînes de caractères
différentes.

```python
"un" == "UN"
```

Pour nous aider, il existe une façon de mettre tout en minuscules

```python
str.lower("UN")
```

```python
"un" == str.lower("uN")
```

Les fonctions `str.upper` et `str.title` permettent d'autres normalisations.

```python
print("The uppercase of 'the' is '" + str.upper("the") + "'.")
```

```python
print("The title version of 'hello world' is '" + str.title("hello world") + "'.")
```

Et il existe des fonctions pour vérifier si une chaîne de caractères est normalisée


- `str.isupper` vérifie qu'une chaîne de caractères est en majusculese;
- `str.islower` vérifie qu'une chaîne de caractères est en minuscules;
- `str.istitle` vérifie qu'une chaîne de caractères est en casse de titre.


```python
str.isupper("HELLO WORLD!")
```

```python
str.islower("hello world!")
```

```python
str.istitle("Hello World!")
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

### Immutabilité des chaînes de caractères

String indexes cannot be reassigned, i.e. the existent parts of the string cannot be modified directly:


```python
string = "hello"
string[-1] = "a"
```

If we have a task to "mask" all vowels from a text, we will need to create a new string based on the old one.

**Practice** Withouth looking at the code in the next cell, can you think of how to do it?


```python
vowels = "aoiue"
text = "This is a sentence that should contain no vowels."

#try it here by yoursel!
```


```python
vowels = "aoiue"
text = "This is a sentence that should contain no vowels."

masked_text = ""
for char in text:
    if char not in vowels:
        masked_text += char
    else:
        masked_text += "*"
print(masked_text)
```

**Practice:** You are given a string `alphabet` that contains all English letters, and a string `text`.


```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = "A chessboard appeared, but it was triangular, and so big that only the nearest point could be seen."
```

Write code that makes this string lowercase and deletes punctuations from the text.

```python

```

### Mutabilité des listes

Les méthodes de listes qu'on a vu **modifient** les listes directement (*in-place*).

```python
ma_liste = ["a"]
ma_liste.append("b")
print(ma_liste)
```

Ce n'était pas le cas des méthodes de chaînes de caractères

```python
str1 = "a"
print(str.upper(str1))
print(str1)
```

En Python, les `str` sont **immutables** et les listes sont **mutables**. Ça a d'autres conséquences
peu intuitives. Comparez ainsi :

```python
a = 1
b = a
a = a + 1
print("a vaut ", a)
print("b vaut ", b)
```

et

```python
a = [1, 2, 3]
b = a
a[1] = 2713
print("a vaut ", a)
print("b vaut ", b)
```

Pour faire une **copie** indépendante d'une liste, on peut utiliser la fonction `list` :

```python
a = [1, 2, 3]
b = list(a)
a[1] = 2713
print("a vaut ", a)
print("b vaut ", b)
```

On peut également utiliser ceci :

```python
a = [1, 2, 3]
b = a[:]  # ← notez la différence
a[1] = 2713
print("a vaut ", a)
print("b vaut ", b)
```


## Fichiers tabulaires

It is in fact possible to engineer a way to work with csv files using the same methods we already discussed.


```python
with open('files/grades.csv', 'r') as file:
    for line in file:
        print(line.strip())
```

Every line of the file is still a string, and therefore to represent them as a list of values, we will need to split them.


```python
with open('files/grades.csv', 'r') as file:
    for line in file:
        print(line.strip().split(","))
```

A simpler way to read csv files in Python is to use `csv` package.

### Bonus : le module `csv`

```python
import csv
```

In order to read a csv file using the `csv` package, right after opening the file, we need to define a `csv.reader` for it. It will parse the rows automatically!


```python
with open('files/grades.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
```

Similarly, to write files, we want to define a `scv.writer` and change the editing mode to `w`. Then we will be able to write rows of the csv one-by-one by applying `writerow` method to the `csv.writer` object.


```python
with open('files/greetings.csv', 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(["hello", "hi", "howdy"])
    csvwriter.writerow(["zdravstvujte", "privet", "hej"])
```

You can read more about the functionality of the `csv` package [here](https://docs.python.org/3/library/csv.html).


### Exercices dico et str

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
text = [
    'a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', 
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
    'shape', 'total', 'so', 'world', 'look', 'sun'
]

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
1\. Écrire une fonction `unique_words`, qui prend une chaine de caractères renvoie une liste contenant tous les mots du texte,
sans doublons, et en minuscules. Le résultat devrait être le suivant (l'ordre peut être différent) :

```console
>>> unique_words(text)
['a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', 'fruit', 'picking', 'there', 'try', 'little', 'around', 'appearances', 'appeared', 'all', 'crossed', 'basis', 'improbability', 'their', 'discworld', 'black', 'to', 'death', 'future', 'only', 'my', 'robe', 'things', 'for', 'it', 'existed', 'said', 'sake', 'sometimes', 'right', 'way', 'that', 'country', 'chessboard', 'quoth', 'well', 'domestic', 'skull', 'wonderful', 'hooded', 'or', 'empty', 'bottom', 'mirror', 'himself', 'rather', 'over', 'every', 'triangle', 'roses', 'border', 'orbiting', 'was', 'from', 'show', 'be', 'pecked', 'bones', 'just', 'universe', 'me', 'triangular', 'gets', 'worth', 'have', 'climbed', 'service', 'fluttered', 'top', 'but', 'grey', 'claws', 'at', 'rats', 'creep', 'own', 'pattern', 'point', 'white', 'than', 'dark', 'therefore', 'frame', 'this', 'not', 'the', 'could', 'mind', 'turtle', 'scrabble', 'better', 'industries', 'looked', 'an', 'cherubs', 'life', 'anything', 'more', 'small', 'and', 'of', 'his', 'on', 'skulls', 'elephants', 'in', 'thoughts', 'seen', 'nearest', 'expectantly', 'other', 'side', 'shape', 'total', 'so', 'world', 'look', 'sun']
```

(évidemment ne faites pas juste un copier-coller)

(la fonction [`str.lower`](https://docs.python.org/dev/library/stdtypes.html#str.lower) est bien
utile)

<!-- #endregion -->

```python

```

2\. Écrire une fonction `get_bigrams`, qui, étant donné un mot en argument, renvoi

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
