---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 10 : Compléments
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

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

<!-- #region -->
<details>
<summary>Solution</summary>

Basique :

```python
template = "Salut, [invité], ravi⋅e de te rencontrer !"
guests = ["Glimmer", "Bow", "Catra",]

print(str.replace(template, "[invité]", guests[0]))
print(str.replace(template, "[invité]", guests[1]))
print(str.replace(template, "[invité]", guests[2]))
```

Acide :

```python
template = "Salut, [invité], ravi⋅e de te rencontrer !"
guests = ["Glimmer", "Bow", "Catra",]

for g in guests:
    print(str.replace(template, "[invité]", g))
```
</details>
<!-- #endregion -->
</details>

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

**Practice** can you think of how to do it?


```python
vowels = "aoiue"
text = "This is a sentence that should contain no vowels."

#try it here by yoursel!
```


<!-- #region -->
<details>
<summary>Solution</summary>

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
</details>
<!-- #endregion -->

**Practice:** You are given a string `alphabet` that contains all English letters, and a string `text`.


```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = "A chessboard appeared, but it was triangular, and so big that only the nearest point could be seen."
```

Write code that makes this string lowercase and deletes punctuations from the text.

```python

```

## Mutabilité des listes

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
