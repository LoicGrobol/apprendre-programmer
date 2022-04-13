---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.8
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Corrections TD récapitulatif 2
==============================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-04-13
<!-- #endregion -->

## Compteurs et accumulateurs

1\.

1.1 Écrire un programme qui compte le nombre de mots de moins de $4$ lettres dans la liste suivante,
puis affiche ce nombre

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

moins_de_quatre = 0
for mot in paragraphe:
    if len(mot) <= 4:
        moins_de_quatre = moins_de_quatre + 1
print(moins_de_quatre)
```

1.2 Même question pour les mots de plus de $6$ lettres

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

plus_de_six = 0
for mot in paragraphe:
    if len(mot) >= 6:
        plus_de_six = plus_de_six + 1
print(plus_de_six)
```

2\.

2.1 Écrire un programme qui compte le nombre de températures supérieures à $50$ dans la liste
`temperatures`, puis affiche ce nombre.

```python
temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]

total = 0
for t in temperatures:
    if t > 50.0:  # On pourrait aussi mettre 50, la différence c'est que 50.0 est un float, comme les températures
        total = total + 1
print(total)
```

2.2 Écrire un programme qui calcule la somme des températures de la liste `temperatures`, puis
affiche ce nombre.

```python
temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]

somme = 0
for t in temperatures:
    somme = somme + t
print(somme)
```

Ou sans boucle

```python
print(sum(temperatures))
```

2.3 Même question que 2.2, mais uniquement pour les températures de plus de $50$.

```python
temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]

somme = 0
for t in temperatures:
    if t >= 50:
        somme = somme + t
print(somme)
```

3\. Écrire un programme qui compte le nombre de mots commençant par une voyelle dans le paragraphe
suivant, puis affiche ce nombre.

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]

compte = 0
for mot in paragraphe:
    if mot[0] in voyelles:
        compte = compte + 1

print(compte)
```

4\. Écrire un programme qui stocke dans une liste `courts` tous les mots de moins de $6$ lettres de
la liste `paragraphe`, puis affiche `courts`.

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

courts = []
for mot in paragraphe:
    if len(mot) <= 6:
        courts.append(mot)

print(courts)
```

## Dictionnaires

1\.

1.1 Écrire un programme qui affiche les éléments correspondant aux clés `poisson`, `verseau` et
`balance` du dictionnaire `mon_dico`.

```python
mon_dico = {
    "capricorne": "janvier",
    "poisson": "février",
    "taureau": "juin",
    "balance": "pas bien",
    "sagitaire": "avant de s'en servir",
    "verseau": "mai"
}

print(mon_dico["capricorne"])
print(mon_dico["verseau"])
print(mon_dico["balance"])
```

Ou en plus classe

```python
for signe in ["capricorne", "verseau", "balance"]:
    print(mon_dico[signe])
```

1.2 Écrire à la suite de la cellule suivante un programme qui modifie `mon_dico` pour donner pour la
clé `"capricorne"` la valeur `"août"`, et pour ajouter la clé `"bélier"`, avec la valeur
`"octobre"`.

```python
mon_dico = {
    "capricorne": "janvier",
    "poisson": "février",
    "taureau": "juin",
    "balance": "pas bien",
    "sagitaire": "avant de s'en servir",
    "verseau": "mai"
}

mon_dico["capricorne"] = "août"
mon_dico["bélier"] = "octobre"
```

2\.

2.1 Écrire un programme qui compte le nombre de clés de plus de $5$ caractères dans le dictionnaire
`geriadur` et affiche ce nombre

```python
geriadur = {
    "Tour-tan": "Phare",
    "Porz": "Port",
    "Arvor": "Littoral",
    "Argoat": "Intérieur des terres",
    "Bro": "Pays",
    "Enez": "Île",
    "Kêr": "Ville",
    "Ti": "Maison",
    "Bihan": "Petit",
    "Bras": "Grand",
    "Krampouezh": "Crêpes",
    "Plou": "Paroisse",
    "Nevez": "Nouveau",
    "Gwenn": "Blanc",
    "Du": "Noir",
    "Glaz": "Bleu",
    "Gwer": "Vert",
    "Melen": "Jaune",
    "Ruz": "Rouge",
    "Evaj": "Boisson",
}

compte = 0
for k in geriadur:
    if len(k) >= 5:
        compte = compte + 1

print(compte)
```

2.2 Même question, mais pour les **valeurs** de plus de $7$ caractères.

```python
geriadur = {
    "Tour-tan": "Phare",
    "Porz": "Port",
    "Arvor": "Littoral",
    "Argoat": "Intérieur des terres",
    "Bro": "Pays",
    "Enez": "Île",
    "Kêr": "Ville",
    "Ti": "Maison",
    "Bihan": "Petit",
    "Bras": "Grand",
    "Krampouezh": "Crêpes",
    "Plou": "Paroisse",
    "Nevez": "Nouveau",
    "Gwenn": "Blanc",
    "Du": "Noir",
    "Glaz": "Bleu",
    "Gwer": "Vert",
    "Melen": "Jaune",
    "Ruz": "Rouge",
    "Evaj": "Boisson",
}

compte = 0
for v in geriadur.values():
    if len(v) >= 7:
        compte = compte + 1

print(compte)
```

3\. Écrire un programme qui crée un dictionnaire `rime` dont les clés sont les mots de la liste
`vocab` et tel que pour chacun de ces mots, `w` `rime[w]` vaut `True` si `w` finit par une voyelle et `False` sinon.

```python
vocab = [
    "Brezhoneg",
    "Demat",
    "Kenavo",
    "Trugarez",
    "Laouenn",
    "Marc'had",
    "Biniou",
]

rime = dict()

for w in vocab:
    rime[w] = w[-1] in voyelles

print(rime)
```

## Fonctions


1\.

1.1 Définir une fonction nommée `bonjour`, qui affiche `"Bonjour"`.

```python
def bonjour():
    print("Bonjour")

bonjour()
```

1.2 Définir une fonction nommée `salut`, qui demande la saisie d'un nom, puis affiche une salutation
en fonction, par exemple `"Salut, Morgan !`" si le nom saisi est `"Morgan"`.

```python tags=["skip-execution"]
def salut():
    nom = input("Quel est ton nom: ")
    print("Salut,", nom)

salut()
```

2\. Définir une fonction nommée `double`, qui accepte un argument et affiche son double.

```python
def double(n):
    print(2*n)

double(43)
double(-2)
```

3\. Définir une fonction nommée `somme` qui accepte deux arguments et affiche leur somme.

```python
def somme(a, b):
    print(a+b)

somme(5, 6)
somme(13, 12)
somme("hello", "world")
```

4\. Définir une fonction qui accepte un nombre comme argument et renvoie son double si ce nombre est
positif et son carré s'il est négatif.

```python
def fun(n):
    if n >= 0:
        return 2*n
    else:
        return n**2

print(fun(5))
print(fun(-20))
```

5\. Définir une fonction qui accepte une chaîne de caractères comme argument et renvoie la chaîne
mise en majuscule si elle commence par une voyelle, et `False` sinon.

```python
def weird(chaine):
    if chaine[0].lower() in voyelles:
        return chaine.upper()
    else:
        return False

print(weird("An Dro"))
print(weird("Hanter Dro"))
```
