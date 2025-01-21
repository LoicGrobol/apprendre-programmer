---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 1 : Entrée/Sortie, variables et manipulations de chaînes de caractères
===========================================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

Dans ce notebook :

- Terminologie de base : *fonction*, *argument*, *variable*, *types*…
- Opérations d'entrée/sortie de base : `print` et `input`.
- Types de données de base `str`, `int`, `float`, `bool`.
- Opérations de base sur les chaînes de caractères.

Ce cours est très largement inspiré du cours [*Basic IO, variables, boolean
expressions*](https://github.com/aniellodesanto/Utah_CompLang21/blob/main/01_io_variables_booleans.ipynb)
d'Aniello de Santo, merci infiniment à lui.


Le texte en dessous, dans une police différente est une cellule de code en Python. Exécutez-la. Si
vous avez oublié comment, retournez voir [le tutoriel Jupyter
notebook](../00-introduction/notebooks.py.md)

```python
print("Hello, world!")
```

Si vous voyez s'afficher quelque chose sous la cellule, bravo ! C'est un genre de tradition de
commencer à apprendre à programmer en faisant afficher ce message.

## 🥳 Exo 🥳

Stop à l'hégémonie de l'anglais ! Modifiez la cellule de code ci-dessous pour faire afficher un
« bonjour, tout le monde ! » dans la langue de votre choix.

```python
print("Hello, world")
```

## Fonctions

Dans ce qui précède, `print` est un **appel de fonction**, et `"Hello, world!"` est son argument


En Python, on peut penser aux fonctions comme la description d'actions qu'on demande à la machine
d'effectuer : ici « affiche le message que je te donne en argument ».


Les **arguments** (ou **paramètres**) d'une fonction servent à spécifier les éléments sur lesquels
portent l'action. Il peut y en avoir un, plusieurs ou zéro.


### `print`

La fonction la plus commune (mais pas nécessairement la plus simple) de Python est `print`. Elle
affiche simplement sur l'écran son ou ses argument(s) :

```python
print("L'informatique c'est fantastique !")
```

En d'autres termes, elle affiche ce qu'elle a entre ses parenthèses. Si on lui donne plusieurs
arguments (en les séparant par des virgules), elle les affiche à la suite

```python
print("Morgan", "Alex")
```

Et voici ce que donne une suite de plusieurs `print`

```python
print("Morgan")
print("Alex")
```

### ⬜ Exo ⬜

Écrire dans la cellule ci-dessous un programme qui affiche votre prénom et votre nom de famille,
séparés par une ligne vide, comme ceci :

```text
Loïc

Grobol
```

### Commentaires

```python
# Un affichage simple
print("Salut les copaines !")
```

Si vous exécutez la cellule précédente, vous devriez observer que la première ligne ne semble avoir
aucun effet. Elle a de plus une couleur différente dans l'éditeur. Et pour cause : elle commence par
un `#`, ce qui en fait un **commentaire**. Un morceau de code que Python n'essaie pas d'interpréter.

À quoi ça sert ?

Essentiellement à annoter votre code, afin d'en expliquer les points délicats à d'autres personnes
(y compris votre vous futur), ou à noter les choses à faire plus tard.

```python
# TODO: mettre des accents et des majuscules
print("c'etait a megara, faubourg de carthage")
```

Pensez à le faire judicieusement.

## Types de données élémentaires

Les **types de données** sont des éléments fondamentaux de la programmation. On va les aborder
en étudiant les types **primitifs** de Python dans la suite. Si vous aimez les vidéos, vous pouvez
aussi regardez celle qui apparaît quand vous exécutez la cellule suivante

```python
from IPython.display import IFrame
IFrame('https://www.youtube.com/embed/A37-3lflh8I', width=700, height=350)
```

Regardez la cellule de code suivante :

```python
print("9", 9, 9.0, 9.9)
```

Vous pouvez voir que les arguments de `print` sont colorés différemment. C'est parce que la
coloration syntaxique de Jupyter vous indique qu'ils sont de **types** différents.

### Types numériques

- Les *integers* (`int`) représentent des nombres *entiers*. Ainsi, `8`, `0`, `-1` and `-2713` sont
  des `int` mais pas `3.14`, `2.0` ou `-1.333`.
- Les *floating point numbers* (`float`), « nombres en virgule flottante » représentent des nombres
  avec une partie entière et une partie fractionnaire.

La distinction entre les deux est importante : ils sont stockés différemments dans la mémoire de
votre machine. Ainsi, en utilisant la fonction `type`, qui renvoie le type de son argument, on peut
constater que `8` est un `int` et `8.5` un `float` :

```python
type(8)
```

```python
type(8.5)
```

Attention :

```python
type(8.0)
```

`8` et `8.0` sont deux représentations du nombre $8$, dans deux types de données, dont on verra
qu'ils n'ont pas les mêmes propriétés ni les mêmes usages.

On peut utiliser en Python les opérations arithmétiques classiques avec `int`s et `float`s :

```python
# addition
6 + 9
```

```python
# soustraction
99 - 0.5
```

```python
# multiplication
5 * 2
```

```python
# division
115 / 2
```

```python
# division entière (le quotient dans la division euclidienne)
115 // 2
```

```python
# modulo (le reste dans la division euclidienne)
115 % 2
```

```python
# Élévation à une puissance
5 ** 10
```

```python
5 * (3+2)
```

### Affichage

Vous avez remarqué ?


Dans les cellules précédentes.


On a pas utilisé `print`.


Mais on a quand même un affichage.


🤔


Il s'agit d'une particularité de l'environnement Jupyter : le résultat de la dernière opération
s'affiche à l'écran. À votre avis que se passe-t-il donc si on exécute la cellule suivante ?

```python
5 + 8
9 + 2
```


Le résultat est-il celui que vous attendiez ?


Ça nous montre que *seulement* la dernière opération donne un affichage automatique. Si on veut
afficher autre chose, il faut le demander explicitement avec `print`.

```python
print(5 + 8)
print(9 + 2)
```

### Chaînes de caractères

Revenons aux types, avec le type le plus important pour nous, linguistes, TAListes et humanistes.


Les *chaînes de caractères* (`str`, *strings*) sont… des séquences de caractères, comme `"machin"`,
`'Bonjour, tout le monde !'` ou `"supercalifragillisticexpialidocious"`. Elles sont notées entre
simple quotes `'` ou double quotes `"`. Vous pouvez choisir l'une ou l'autre option.

```python
type("La linguistique est fantastique.")
```

```python
type('Tout le monde déteste les polices de caractères')
```

Que se passe-t-il si on mélange les deux ?

```python
type("My phone number is 123.')
```

En général, c'est plus pratique d'utiliser des *double quotes*, notamment parce que c'est plus
agréable d'y utiliser `'` comme apostrophe

```python
print("J'aime les humanités")
```

On peut le faire aussi avec des *simple quotes*, mais dans ce cas, il faut le **déspécialiser** avec
un `\` (pour indiquer à Python qu'il ne s'agit de *données* et pas d'un morceau de programme).

```python
print('Le TAL, c\'est génial.')
```

À l'inverse, si on veut utiliser des *doubles quotes* dans la chaîne, on peut la délimiter avec des
simples.

```python
print('"Apprendre à programmer" est mon cours préféré')
```

Attention, un nombre entre *quotes*, c'est une chaîne de caractères :

```python
print(type(5))
print(type("5"))
```


Dans la cellule précédente, quand on note `print(type(5))` ça signifie « passer comme argument à
`print` la valeur de retour de `type` appliquée à `5` : on peut ainsi enchaîner des appels de
fonctions.

Pour les chaînes des caractères, `+` désigne la concaténation

```python
"artificiel" + "le"
```

À votre avis, quel est le résultat de la cellule suivante ?

```python
"13" + "11"
```

À votre avis, peut-on utiliser les autres opérateurs arithmétiques avec des chaînes de caractères ?
Testez ci-dessous. Vous pouvez aussi créer de nouvelles cellules dans le notebook.

```python

```

```python
"ab" - "b"
```

```python
"aaaaa" / "a"
```

```python
"a" % "b"
```

```python
"abx"*4
```

Il est fréquent de devoir convertir des données d'un type à l'autre. Par exemple pour effectuer des
opérations arithmétiques sur un nombre contenu dans une chaîne de caractères. Pour cela, on peut
utiliser les fonctions de conversion `int` et `float`.

```python
print("Type d'origine:", type("55"))
print("Nouveau type:", type(int("55")))
```

```python
int("55")
```

```python
int("55") - 5
```

L'opération inverse — convertir un nombre en chaîne de caractères — se fait avec `str`

```python
print("Type d'origine:", type(55))
print("Nouveau type:", type(str(55)))
```

On peut ainsi intégrer le résultat d'un calcul dans un message

```python
print("Le double de 5 est " + str(2*5) + ". Étonnant, non")
```

On peut aussi, convertir des `int` en `float`

```python
float(2713)
```

Et vice-versa, mais qu'est-ce que ça va donner d'après vous ?

```python
int(7.9)
```

### Booléens

Un dernier type : les **booléens** (*boolean*, `bool`), qui ne peuvent prendre que deux valeurs
`True` (vrai) et `False` (faux).


(Pourquoi « booléen », d'ailleurs ?)

```python
print(type(True))
print(type(False))
print(type("False"))
```

Les booléens sont les réponses aux questions comme

- « Est-ce que cette phrase contient le mot *linguistique* ? »
- « Est-ce que la somme de ces deux nombres est plus grande que 420 ? »
- « Est-ce que j'ai déjà entendu cette phrase ? »

Nous verrons bientôt à quoi ils peuvent servir.


## Variables

Pour l'instant on a travaillé avec des instructions indépendantes. Mais comment faire si on peut
utiliser le résultat d'une instruction dans une instruction qui suit ?


On a vu

```python
print(type(8))
```

Mais ça va devenir très pénible très vite. Ça serait bien d'avoir un moyen de stocker des données en
mémoire et de les récupérer plus tard.


Ce moyen, ce sont les **variables** qui vont nous les donner. Une variable, c'est un emplacement
qu'on réserve dans la mémoire de la machine, avec un nom qui nous permet de la réutiliser. Comme
ceci :

```python
nom = "Loïc"
print("Salut, ", nom)
```

Une variable peut être de n'importe lequel des types qu'on a vu jusqu'à présent :

```python
fruit = "banane"
un_nombre = 9
un_autre_nombre = 0.2
machin = True
un_hotel = "Trivago"

print("Le type de fruit est", type(fruit))
print("Le type de un_nombre est", type(un_nombre))
print("Le type de un_autre_nombre est", type(un_autre_nombre))
print("Le type de machin est", type(machin))
```


Les lignes de la forme `nom_de_variable = <quelque chose>` sont des instructions d'**affectation**,
qui *affectent* une valeur à une variable.


Si on affecte plusieurs valeurs successivement à une variable, elle change de valeur à chaque fois.

```python
nom = "Loïc"
print(nom)
nom = "Alex"
print(nom)
nom = "Morgan"
print(nom)
```

### Noms de variables

Les règles à retenir

- Les noms de variables ne sont pas des chaînes de caractères : pas de quotes autour !
- Les noms de variables ne peuvent pas commencer par un chiffre.
- Les noms de variables ne contiennent pas d'espaces (utilisez `_` à la place) ni certains symboles
  comme `$`, `!`, `+`…
- Les caractères Unicodes correspondant à des lettres sont utilisables.

```python
ééééééé = 1
Δ = -0.5
```

Mais comme ce n'est pas toujours facile à entrer au clavier, on conseille en général d'éviter.


Quelques noms de variables sont interdits car ils correspondent à des mots-clés de Python

```python
def = "nope"
```

Et certains autres comme `print`, `int`, `type` sont *techniquement* utilisables comme noms de
variables, mais c'est plutôt une mauvaise idée. À votre avis pourquoi ?


On peut donc maintenant réutiliser les résultats d'instructions.

```python
large_number = 193425 + 32532513
print(large_number)
```

```python
partenaire1 = "Morgan"
partenaire2 = "Alex"
partenaires = partenaire1 + " et " + partenaire2
print(partenaires)
```


```python
a = 5
b = a + 1
print(b)
```

```python
a = 5
b = a
print(b)
```

On peut redéfinir une variable en faisant référence à sa valeur actuelle

```python
compteur = 0
print("Première valeur", compteur)
compteur = compteur + 1
print("Deuxième valeur", compteur)
```

```python
mot = "machinal"
print(mot)
mot = mot + "lement"
print(mot)
```

### Cellules et exécutions

À présent qu'on travaille avec des variables, vous allez de plus en plus écrire du code dans une
cellule qui utilise des variables définies dans une autre cellule. Faites attention à l'ordre dans
lequel vous les exécutez.

Regardez par exemple les deux cellules suivantes : que se passe-t-il si on exécute la deuxième sans
exécuter la première

```python
un_nombre = 5
```

```python
un_autre_nombre = 8
un_troisieme_nombre = un_nombre + un_autre_nombre
print(un_troisieme_nombre)
```

## Entrées et sorties de base

On a vu comment afficher des valeurs à l'écran avec `print`. Mais pour beaucoup d'applications
(pensez à un chatbot par exemple), il est utile de demander à un⋅e utilisateurice une entrée. En
Python, on fait ça avec `input`.

```python tags=["skip-execution"]
print("Comment tu t'appelles ?")
nom = input()
print("Salut, ", nom)
```

`input` donne la main à l'utilisateurice pour saisir une chaîne de caractère (terminée en
appuyant sur entrée) et renvoie cette chaîne de caractères.

## Expressions booléennes

Les **expressions booléennes** sont les expressions qui ont une valeur de vérité, `True` or `False`.
Elles peuvent se construire à l'aide d'opérateurs de comparaison :

`==` est vrai si et seulement si ses termes gauches et droits sont égaux

```python
10 + 5 == 15
```

```python
10 == 15
```

```python
"Apple" == "apple"
```

```python
(10 + 5 == 20) == False
```

**Attention** il y a bien **deux** signes « égal », pour le différencier de l'opérateur d'affectation

L'opérateur inverse, qui vérifie la différence, est `!=` (≠ en ASCII art quoi)

```python
1 != 10
```

Les opérateurs `<`, `>`, `<=` et `>=` fonctionnent comme vous imaginez

```python
7 < 9
```

```python
8 >= 8
```

L'opérateur `in` vérifie l'inclusion

```python
"world" in "Hello world!"
```

```python
"Apple" in "I love apples"
```

Et `not in` vérifie la non-inclusion

```python
"peach" not in "I love apples"
```

L'opérateur `not` inverse la polarité d'un booléen

```python
not True
```

```python
not False
```

```python
not (10 + 5 == 15)
```

On peut donc aussi écrire

```python
not ("peach" in "I love apples")
```

Mais c'est plus laid et moins efficace que d'utiliser `not in`.

On peut également combiner des expressions booléennes avec les opérateurs logiques `and` et `or`

- `A and B` est vrai si `A` et `B` sont vraies toutes les deux.
- `A or B` est vrai si au moins une des deux expressions `A` et `B` est vraie.

### 🤷🏻 Exo 🤷🏻

Déterminer sans les exécuter les valeurs de retour de ces instructions :

```python
True and True
```

```python
True and False
```

```python
False or False
```

```python
(False and True) or True
```

```python
False and (True or True)
```

```python
("apple" in "apples") and (1 + 1 == 2)
```

```python
("apple" in "apples") or (1 + 1 == 5)
```

**Puis** vérifiez vos réponses

```python

```

Si vous peinez, vous pouvez aller regarder cette vidéo, qui vous donnera peut-être une meilleure
intuition des opérateurs booléens

```python
IFrame('https://www.youtube.com/embed/sdx9dACkvyI', width=700, height=350)
```

Une autre façon de voir les opérateurs booléens est d'y penser en termes de tables de vérité. Si
vous êtes intéressé⋅es, voici une vidéo sur le sujet :

```python
IFrame('https://www.youtube.com/embed/jbete3iXbdM', width=700, height=350)
```

## 🦾 Exercices 🦾

Répondre à ces exercices directement dans le notebook, le sauvegarder sous un nom de la forme
`01_io_variables_chaines_PRENOM_NOM.ipynb` (pour Morgan Lefeuvre par exemple, ce serait
`01_io_variables_chaines_Morgan_Lefeuvre.ipynb`) et le déposer sur Cours en Ligne;

**Assurez-vous bien que l'extension du fichier est `ipynb`.**

### Exercice 1

Étant donné le paragraphe suivant

```python
texte = "Toi dont le trône étincelle, ô immortelle " \
        "Aphrodite, fille de Zeus, ourdisseuse de " \
        "trames, je t'implore : ne laisse pas, ô " \
        "souveraine, dégoûts ou chagrins affliger " \
        "mon âme, " \
        "Mais viens ici, si jamais autrefois " \
        "entendant de loin ma voix, tu m'as " \
        "écoutée, quand, quittant la demeure " \
        "dorée de ton père tu venais, après avoir " \
        "attelé ton char, " \
        "de beaux passereaux rapides " \
        "t'entraînaient autour de la terre " \
        "sombre, secouant leurs ailes serrées et du " \
        "haut du ciel tirant droit à travers l'éther."
```

Écrire un programme qui demande à l'utilisateurice de saisir un mot, puis affiche `True` si le mot
est dans le texte (autrement dit s'il est inclus dans la variable `texte`) et `False` sinon.

```python

```

### Exercice 2

Écrire un programme qui vérifie si le mot *banane* est contenue dans une entrée récupérée avec
`input`.

```python

```

### Exercice 3

Dans une nouvelle cellule ci-dessous, écrire un programme qui demande à son utilisateurice son année
de naissance et affiche l'âge qu'aura cette personne en 2048.

Indice : `int`


### Réflexion

Quelques points auxquels réfléchir

- Combien de temps avez-vous passé à faire ces exercices ?
- Qu'est-ce qui vous a paru le plus compliqué ?
- À votre avis, pourquoi ?

Merci d'ajouter vos réponses à cette cellule, elles m'aideront à améliorer les prochains cours.
