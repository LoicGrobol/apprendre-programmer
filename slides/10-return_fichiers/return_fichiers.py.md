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
Cours 10 : valeur de retour et accès aux fichiers
=================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-03-29
<!-- #endregion -->

Dans ce notebook

- Un nouveau pouvoir pour les fonctions
- Accéder à des fichiers externes.

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

Elles passent en fait toutes la valeur `None` : un objet spécial de Python qui signifie
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
renvoie toujours la même chose, pas vraiment la peine de faire une fonction, une variable
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

## Lire des fichiers

There are two files in the folder `files`: `novartis_microsoft.txt` and `grades.csv`. To open or create a file, we will use the following syntax:

    with open(path_to_file, mode) as name_of_open_file:
        # code where the open file is referred to as name_of_open_file
        
`path_to_file` is a string that points to the file that we want to open or create. The current notebook is in the `notebooks` repository, and therefore in order to give the adress of, for example,  `novartis_microsoft.txt`, we need to provide the following path: `'files/novartis_microsoft.txt'`.

`mode` is a string that defined the mode in which you are going to work with the file. The main modes are the following ones:
  * `'r'` (read): in this case we expect the file with the indicated name to already exist, and we are going to read the file line-by-line, where lines are separated by a new line character from each other;
  * `'w'` (write): opening a file with a writing mode will _create_ that file on the computer and will allow us to write strings into that file;
  * `'a'` (append): opens an already existent files and allows to add new lines to the end of that file.
  
There are many other modes in which it is possible to open a file, but you can read about them on your own [here](https://stackabuse.com/file-handling-in-python/).


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    for line in file:
        print(line)
```

The variable `file` is a name for the .txt file when it is loaded in the memory and ready to be processed. Its type is `<class '_io.TextIOWrapper'>` and it is an iterable that contains ordered strings.


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    print("Type of `file`:", type(file), "\n")
    for line in file:
        print(type(line))
        print(line)
```

Every line in a text file ends with a new line character `\n` -- this is how we know when a new line starts! However, if you want to avoid printing a new line every time you are displaying the line, we can use the string method `strip`.


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    for line in file:
        print(line.strip(), end = " ")
```

If instead of iterating through the lines of the file you want to get access to all of them at once, we can read all the lines of it into some variable by using `readlines` method: it creates a list of strings, where every string is a separate line of the file.


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    lines = file.readlines()
    print(type(lines))
    print(lines)
```

Another way to avoid overt iteration and to get lines one by one, is to read them in memory one after another by using the `readline` method.


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)
```

Notice, that every time you execute `readline`, it moves the the next line of the file. We need to use `seek` method that goes to the bite indicated of the file, and therefore using `seek(0)` will move us back to the very beginning of the file.


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)
    file.seek(0)
    line = file.readline()
    print(line)
```

If you are using the `with open(filepath, mode)` syntax, the file is being open in the memory only while the indented code is being executed. As soon as we finished executing the code within the `with` codeblock, the variable `file` becomes unavailable.


```python
with open('files/novartis_microsoft.txt', 'r') as file:
    line = file.readline().strip()
    print(line)
    
line = file.readline()
```

## Écrire dans des fichiers

As I mentioned before, the mode `w` opens the files in the writing mode, i.e. creates the files.

* `readline` reads a line and returns a _string_ containing that line;
* `readlines` reads all lines and returns a _list of strings_.

In the writing mode, there are methods that write line or lines in a similar manner:

* `writeline` takes a _string_ as its argument and writes it to the newly created file;
* `writelines` takes a _list of strings_ as its argument and writes all of them to the newly created file.


```python
file = open('files/newfile.txt', 'w')
text_to_write = ["Hello world!", "It is Wednesday.", "Middle of the week!"]
file.writelines(text_to_write)
file.close()
```

**Warning:** it is possible to write only lists of strings. If the data that needs to be written contains other data types, make sure to convert them to strings!


```python
file = open('files/newfile.txt', 'w')
text_to_write = ["Hello world!", 42]
file.writelines(text_to_write)
file.close()
```

The usual `str` function takes care of converting nearly any datatype to its string representation.


```python
file = open('files/newfile.txt', 'w')
text_to_write = ["Hello world! ", str(42)]
file.writelines(text_to_write)
file.close()
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

## Exercices
