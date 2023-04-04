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


