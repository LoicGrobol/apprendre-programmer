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
Cours 11 : TD récapitulatif 2
============================

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)
<!-- #endregion -->

Dans ce notebook

- Des exercices.
- Encore des exercices.
- Toujours des exercices.
- Basiquement la suite du [premier récapitulatif](../06-recapitulatif/recapitulatif.py.md)

Il y a des rappels pour chacune des notions, mais n'hésitez pas à aller relire les cours précédents
et les corrections des exercices.

**Si vous révisez en autonomie : commencez par refaire [le premier
récapitulatif](../06-recapitulatif/recapitulatif.py.md) et à revoir [sa
correction](../06-recapitulatif/corrections.py.md).** En particulier sa section « utiliser un
notebook » si vous avez des doutes.

## Fonctions

> De la même façon qu'on a vu comment utiliser des variables pour stocker et réutiliser des valeurs,
> une fonction est une façon de sauvegarder et de réutiliser un bloc d'instructions.

```python
def fun():
    print("Bonjour tout le monde")
    print("Comment ça va ?")

fun()
print("autre chose")
fun()
fun()
```

> Si on veut transmettre une variable à une fonction, on peut le faire en lui donnant des
> **arguments**, comme `val` dans la fonction `spam` ci-dessous :

```python
def spam(val):
    print("Tu m'as donné l'argument", val)
    print("Je sais pas quoi en faire, mais c'est sympa")
    print("Je vais le répéter")
    print(val)
    print("Encore trois fois")
    for i in range(3):
        print(val)

spam(5)
spam(-12)
spam("helloooo")
```

> Attention, les variables définies dans une fonction ne sont pas accessibles en dehors

```python tags=["raises-exception"]
def egg(n):
    m = n**2
    # Ici m existe
    print("m vaut", m)

egg(4)
# Mais pas là
print("m vaut", m)
```

> En revanche, on peut exfiltrer une valeur hors de la fonction à l'aide de l'instruction `return`

```python tags=["raises-exception"]
def egg(n):
    m = n**2
    print("m vaut", m)
    return m

r = egg(4)
print("r vaut", r)
```

> Dans ce cas on dit qu'on a **renvoyé** une valeur.
>
> Les fonctions que vous écrivez vous-même peuvent faire tout ce que les fonctions que vous utilisez
> depuis le début de ce cours (`print`, `len`…) font. Voici par exemple une façon de réécrire la
> fonction `len` :

```python
def longueur(seq):
    resultat = 0
    for elem in seq:
        resultat = resultat + 1
    return resultat

print(longueur([1, 2, 3]))
print(longueur([2, 7, 1, 3, 12, 15, 18]))
print(longueur("bonjour"))
```

Pensez à tester vos fonctions !

1\.

1.1 Définir une fonction nommée `bonjour`, qui affiche `"Bonjour"`.

```python
# Coder ici
```

1.2 Définir une fonction nommée `salut`, qui demande la saisie d'un nom, puis affiche une salutation
en fonction, par exemple `"Salut, Morgan !`" si le nom saisi est `"Morgan"`.

```python
# Coder ici
```

2\. Définir une fonction nommée `double`, qui accepte un argument et affiche son double.

```python
# Coder ici
```

3\. Définir une fonction nommée `somme` qui accepte deux arguments et affiche leur somme.

```python
# Coder ici
```

4\. Définir une fonction qui accepte un nombre comme argument et renvoie son double si ce nombre est
positif et son carré s'il est négatif.

```python
# Coder ici
```

5\. Définir une fonction qui accepte une chaîne de caractères comme argument et renvoie la chaîne
mise en majuscule si elle commence par une voyelle, et `False` sinon.

```python
# Coder ici
```

## Compteurs et accumulateurs

> Les **compteurs**, et plus largement les **accumulateurs** sont des recettes très fréquemment
> utilisées en lien avec les boucles.
>
> Le plan est le suivant : on initialise une variable à une valeur de base, puis on parcourt un
> itérable, en mettant à jour la variable en question à chaque itération. Pour un compteur, il
> s'agit de… compter des éléments ou des occurrences.
>
> Voici la version la plus simple d'un compteur : ici la variable `compte` va nous servir à compter
> tous les éléments de la liste `spam`.

```python
spam = [4, "n", 7, 1, "f", 4]
compte = 0
for elem in spam:
    compte = compte + 1
print("Il y a", compte, "éléments dans spam.")
```

> En pratique, on ne compte en général pas tous les éléments, mais seulement ceux qui vérifient une
> certaine condition : ici les chaînes de plus de quatre caractères :

```python
spam = ["manger", "et", "dormir", "c'", "essentiel"]
compte = 0
for elem in spam:
    if len(elem) > 4:
       compte = compte + 1
print(compte)
```

> Les accumulateurs sont une version plus générale où on fait autre chose qu'ajouter $1$
> (*incrémenter*) à la variable. Par exemple ici, on stocke dans `acc` la somme des longueurs des
> mots de la liste :

```python
spam = ["manger", "et", "dormir", "c'", "essentiel"]
acc = 0
for elem in spam:
    acc = acc + len(elem)
print(acc)
```

> Un accumulateur n'est pas nécessairement un nombre : ici par exemple, c'est une liste

```python
spam = ["manger", "et", "dormir", "c'", "essentiel"]
longs_mots = []
for elem in spam:
    if len(elem) > 4:
       longs_mots.append(elem)
print(longs_mots)
```

1\.

1.1 Écrire une fonction qui renvoie le nombre de chaînes de moins de $4$ caractères dans une liste.

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

def compte_4(lst):
    # Coder ici

s = compte_4(paragraphe)
print(s)
```

1.2 Même question pour les mots de plus de $6$ caractères

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

def compte_6(lst):
    # Coder ici

c = compte_6(paragraphe)
print(c)
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

# Coder ici
```

2.2 Écrire une fonction qui prend en argument une liste de nombres et **renvoie** la somme de ces nombres

```python
temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]

def somme(liste):
    # Coder ici

print(somme(temperatures))
```

2.3 Même question que 2.2, mais uniquement pour les températures de plus de $50$.

```python
temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]

def somme_50(liste):
    # Coder ici

print(somme_50(temperatures))
```

3\. Écrire un programme qui compte le nombre de mots commençant par une voyelle dans le paragraphe
suivant, puis affiche ce nombre.

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]

# Coder ici
```

4\. Écrire un programme qui stocke dans une liste `courts` tous les mots de moins de $6$ caractères
de la liste `paragraphe`, puis affiche `courts`.

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

# Coder ici
```

## Dictionnaires

> Les **dictionnaires** (`dict`) sont des structures de données qui partagent avec les listes la
> notion d'accéder à un élément par un identifiant, une **clé**. Dans une liste, la clé d'un
> élément est un nombre entier. C'est son **indice**, sa position :

```python
ma_liste = [1, 6, 2, 5, "hello, world"]
v = ma_liste[4]
print(v)
```

> Dans un dictionnaire, les clés peuvent être (presque) n'importe quoi :

```python
mon_dict = {1: "hello, world", "spam": 18, "c": True}
v = mon_dict["spam"]
print(v)
```

> On crée un dictionnaire comme ci-dessus en donnant entre accolades une série de couples `clé:
> valeur`. On peut aussi modifier les éléments d'un dictionnaire :

```python
mon_dict = {1: "hello, world", "spam": 18, "c": True}
print(mon_dict)
mon_dict["spam"] = "bidule"
print(mon_dict)
```

> Ou en ajouter de nouveaux :

```python
mon_dict = {1: "hello, world", "spam": 18, "c": True}
print(mon_dict)
mon_dict["Apprendre à programmer"] = "Clairement le meilleur cours de la L3"
print(mon_dict)
```

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

# Coder ici
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

# Coder ici
```

> La plupart des opérations sur les listes ont un équivalent pour les dictionnaires :

```python
truc = {1: "hello, world", "spam": 18, "c": True}
# Existence d'une clé
print("spam" in truc)
# Existence d'une valeur
print("hello, world" in truc.values())
# Itérer sur les clés
print("Clés:")
for k in truc:
    print(k)
print("Valeurs:")
# Itérer sur les valeurs
for v in truc.values():
    print(v)
print("-----")
# itérer sur les deux
for cle, val in truc.items():
    print(cle, ":", val)
```

2\.

2.1 Écrire une fonction qui compte le nombre de clés de plus de $5$ caractères dans un dictionnaire
(dont on suppose que les clés sont toutes des chaînes de caractères)

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

def compte_cles_5(dico):
    # Codez ici

complte_clez_5(geriadur)
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

def compte_valeurs_7(dico):
    # Codez ici

compte_valeurs_7(geriadur)
```

3\. Écrire un programme qui crée un dictionnaire `rime` dont les clés sont les mots de la liste
`vocab` et tel que pour chacun de ces mots, `w` `rime[w]` vaut `True` si `w` finit par une voyelle
et `False` sinon.

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

# Coder ici
```

**Indices** :

- Il y a une liste de voyelles plus haut.
- Pensez à utiliser une boucle.
