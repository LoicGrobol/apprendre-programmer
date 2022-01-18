---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
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

2022-01-18
<!-- #endregion -->

Dans ce notebook :

- Introduction à Jupyter.
- Terminologie de base : *fonction*, *argument*, *variable*, *types*…
- Opérations d'entrée/sortie de base : `print` et `input`.
- Types de données de base `str`, `int`, `float`, `bool`.
- Opérations de base sur les chaînes de caractères.

Ce cours est très largement inspiré du cours [*Basic IO, variables, boolean
expressions*](https://github.com/aniellodesanto/Utah_CompLang21/blob/main/01_io_variables_booleans.ipynb)
d'Aniello de Santo, merci infiniment à lui.

## L'environnement Jupyter

Dans ce cours, nous allons utiliser plusieurs environnements en Python. Celui dans lequel vous vous
trouvez s'appelle un *notebook Jupyter*. Leur principal avantage est qu'ils permettent de mélanger
du code, du texte formaté et des objets multimedia.

Pour vous épargner la peine d'installer Jupyter sur vos machines, nous allons travailler dans
Binder. Nous verrons plus tard dans le semestre comment installer Python et Jupyter, mais si vous
êtes pressé⋅es et avez besoin d'aide, dites le moi et je vous expliquerai comment faire.

Point technique : nous utiliserons uniquement Python 3 dans sa version au moins 3.8, quel que soit
l'environnement que vous utilisez, vérifiez que la version de Python est la bonne.

Rentrons dès maintenant dans le vif du sujet : le texte en dessous, dans une police différente est
une cellule de code en Python. Pour l'exécuter, utilisez les boutons de la barre d'outil, le menu,
ou simplement cliquez dedans pour la sélectionner et appuyez sur les touche `ctrl` et `entrée`.

```python
print("Hello, world!")
```

Si vous voyez un message s'afficher, vous avez correctement exécuté la cellule. Si c'est la première
fois que vous exécutez un programme, félicitations ! J'espère que ce sera le premier d'une longue
série d'aventures programmatiques.

### 🥳 Exo 🥳

Stop à l'hégémonie de l'anglais ! Modifiez la cellule de code ci-dessous pour faire afficher un
« bonjour, tout le monde ! » dans la langue de votre choix.

```python
print("Hello, world!")
```

Vous l'avez ? C'est peut-être le premier programme que vous écrivez. Si c'est le cas, encore une
fois, bravo !

## Fonctions

Dans ce qui précède, `print` est un **appel de fonction**, et `"Hello, world!"` est un argument

À ce stade, une **fonction** en Python ressemble au concept de fonction en sémantique, en logique ou
en mathématiques. On ne va pas rentrer dans des détails formels, mais plutôt garder en tête un
exemple : la phrase « Morgan mange une pomme », peut être vue comme l'action d'une **fonction**,
`manger` sur deux **arguments**, `Morgan` et `une pomme`, qu'on écrit `manger(Morgan, une pomme)`.

En Python, on peut penser aux fonctions comme la description d'actions et elles renvoient toutes un
résultat, aussi dire **valeur de retour** :

- Une fonction qui inverse une chaîne de caractères renvoie une chaîne de caractères.
- Une fonction qui additionne deux nombres renvoie leur somme.
- Une fonction qui compte le nombre de caractères renvoie un nombre.

Et `print` ? Elle renvoie la valeur spéciale `None`, « rien ». Je vous laisse réfléchir aux
implications philosophiques d'un tel objet.

Les **arguments** (ou **paramètres**) d'une fonction servent à spécifier les éléments sur lesquels
portent l'action. Il peut y en avoir un, plusieurs ou zéro. Par exemple :

- Une fonction qui inverse une chaîne de caractères a un argument : cette chaîne de caractères.
- Une fonction qui renvoie les $n$ premiers mots d'une phrase a deux arguments : la phrase et $n$.
- Une fonction qui afficher « Bonjour, tout le monde ! » a zéro arguments : son exécution sera la
  même à chaque fois.

**Question** : combien faut-il d'arguments pour une fonction qui dessine un cercle ?

### `print`

La fonction la plus commune (mais pas nécessaireemnt la plus simple) de Python est `print`. Elle
affiche simplement sur l'écran son ou ses argument(s) :

```python
print("L'informatique c'est fantastique !")
```

En d'autres termes, elle affiche ce qu'elle a entre ses parenthèses. Si on lui donne plusieurs
arguments (en les séparant par des virgules), elle les affiche chacun sur une ligne.

```python
print("Morgan", "Alex")
```

### ⬜ Exo ⬜

Écrire dans la cellule ci-dessous un programme qui affiche votre prénom et votre nom de famille,
séparés par une ligne vide, comme ceci :

```text
Loïc

Grobol
```

```python
# À toi de jouer
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

C'est **important**, pensez à le faire judicieusement.

## Types de données élémentaires

Les **types de données** sont des des éléments fondamentaux de la programmation. On va les aborder
en étudiant les types **primitifs** de Python dans la suite. Si vous aimez les vidéos, vous pouvez
aussi regardez celle qui apparaît quand vous exécutez la cellule suivante

```python
from IPython.display import IFrame
IFrame('https://www.youtube.com/embed/A37-3lflh8I', width=700, height=350)
```

Regardez la cellule de code suivante :

```python
print("9", 9, 9.9)
```

Vous pouvez voir que les arguments de `print` sont colorés différemment. C'est parce que la
coloration syntaxique de Jupyter vous indique qu'ils sont de **types** différents.

### Types numériques

- Les *integers* (`int`) représentent des nombres *entiers*. Ainsi, `8`, `0`, `-1` and `-2713` sont
  des `int` mais pas `3.14` ou `-1.333\.
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
qu'ils n'ont pas les mêmes propriétés ni les mêmes usage.

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
# modulo(le reste dans la division euclidienne)
115 % 2
```

```python
# Élévation à une puissance
5 ** 10
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

En général, c'est plus pratique d'utiliser des double quotes, notamment parce que c'est plus
agréable d'y utiliser `'` comme apostrophe

```python
print("J'aime les humanités")
```

On peut le faire aussi avec des simple quotes, mais dans ce cas, il faut le déspécialiser

```python
print('Le TAL, c\'est génial.')
```

Attention, un nombre entre quotes, c'est une chaîne de caractères :

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
"15" + "1"
```

À votre avis, peut-on utiliser les autres opérateurs arithmétiques avec des chaînes de caractères ?
Testez ci-dessous. Vous pouvez aussi créer de nouvelles cellules dans le notebook.

```python

```

Il est fréquent de devoir convertir une variable d'un type à l'autre. Par exemple pour effectuer des
opérations arithmétiques sur un nombre contenu dans une chaîne de caractères. Pour celà, on peut
utiliser les fonction de conversion `int` et `float`.

```python
print("Type d'origine:", type("55"))
print("Nouveau type:", type(int("55")))
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

Qu'on préfère écrire ainsi :

```python
print(f"Le double de 5 est {2*5}. Étonnant, non")
```

Le `f` devant les quotes signales qu'on utilise un *format string* pour une *interpolation*. On en
reparlera.

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

Pour l'instant on a travaillé avec des instructions indépendantes. Mais comment faire si on peut utiliser le résultat d'une instruction dans une instruction qui suit ?


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


Les lignes de la forme `nom_de_variable = <quelque chose>` sont des instructions d'**affectation**, qui *affectent* une valeur à une variable.


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
- Les caractères Unicodes correspondant à des lettres ainsi que quelques autres sont utilisables.

```python
ééééééé = 1
Δ = -0.5
💗 = "Yes"
```

Mais comme ce n'est pas toujours facile à entrer au clavier, on conseille en général d'éviter.


Quelques noms de variables sont interdits car ils correspondent à des mots-clés de Python

```python
def = "nope"
```

Et certains autres comme `print`, `int`, `type` sont *techniquement* utilisables mais on ne le fait pas pour éviter de tout casser.


On peut donc maintenant réutiliser les résultats d'instructions.

```python
large_number = 193425 + 32532513
print(large_number)
```

```python
partenaire1 = "Morgan"
partenaire2 = "Alex"
partenaires = partenaire1 + " et " + partenaire2
print(partenaire)
```


Ça marche aussi avec des interpolations

```python
ship = f"{partenaire1} et {partenaire2}")
print(partenaire)
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
mot = f"{mot}lement"
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

```python tags=["nbconvert_ignore"]
print("Comment tu t'appelles ?")
nom = input()
print("Salut," nom)
```

`input` donne la main à l'utilisateurice pour saisir une chaîne de caractère (terminée et en
appuyant sur entrée) et renvoie cette chaîne de caractères. On peut aussi préciser un message à
afficher directement à côté de la zone de saisie.

```python tags=["nbconvert_ignore"]
nom = input("Comment tu t'appelles ?")
print(f"Salut, {nom}")
```

## Expressions booléennes

Les **expressions booléennes** sont les expressions qui ont une valeur de vérité, `True` or `False`. Elles peuvent se construire à l'aide d'opérateurs de comparaison :

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

Operators >, >=, < and <= are defined as well.

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

<!-- #region -->
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

```python
(("apple" in "apples") and (1 + 1 == 3)) or (5 < 10)
```
<!-- #endregion -->

**Puis** vérifiez vos réponses

```python

```

Si vous peinez, vous pouvez aller regarder cette vidéo, qui vous donnera peut-être une meilleure
intuition des opérateurs boolées

```python
IFrame('https://www.youtube.com/embed/sdx9dACkvyI', width=700, height=350)
```

Une autre façon de voir les opérateurs booléens est d'y penser en termes de tables de vérité. Si
vous êtes intéressé⋅es, voici une vidéo sur le sujet :

```python
IFrame('https://www.youtube.com/embed/jbete3iXbdM', width=700, height=350)
```

## Méthodes des chaînes de caractères

Un concept important en TAL est celui de « sac de mots ». Il s'agit d'un modèle sémantique très
simple où on fait l'hypothèse que le sens d'un texte peut être représenté par la liste des mots
qu'il contient et leurs nombres d'occurrence. Intuitivement, si un texte par d'animaux de compagnie,
on s'attend à rencontre plus souvent les mots *chat* ou *chien* que s'il s'agit d'un texte sur la
politique française.

Certains mots, cependant, apparaissent à peu près avec la même fréquence dans tous les types de
textes : *et*, *un*, *la*… On les appelle parfois « mots vides » ou « *stop words* », puisqu'ils
n'apportent pas d'information pour ce modèle, et on commence en général par les enlever des textes à
représenter.

De même, pour beaucoup d'applications en lingusitique, la casse (majuscules et minuscules) n'est pas
informative. Par exemple pour enelver les *stop words* d'un texte, on veut les enlever peu importe
leur casse (*Un*, *un*, *UN*…). Cependant pour Python, *Un* et *un* des chaînes de caractères
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

Une autre fonction utile est `len`. Pouvez-vous deviner ce qu'elle fait …

```python
len("Hello world!")
```


```python
len("computational linguistics")
```

```python
len(25)
```

## 🦾 Exercices 🦾

Répondre à ces exercices directement dans le notebook, le sauvegarder sous un nom de la forme
`01_io_variables_chaines_Loic_Grobol.ipynb` et me l'envoyer avant le prochain cours à
`<lgrobol@parisnanterre.fr>`.

### Exercice 1

Étant donné le paragraphe suivant

```python
texte = "Toi dont le trône étincelle, ô immortelle" \
        "Aphrodite, fille de Zeus, ourdisseuse de" \
        "trames, je t'implore : ne laisse pas, ô" \
        "souveraine, dégoûts ou chagrins affliger" \
        "mon âme," \
        "Mais viens ici, si jamais autrefois" \
        "entendant de loin ma voix, tu m'as" \
        "écoutée, quand, quittant la demeure" \
        "dorée de ton père tu venais, Après avoir" \
        "attelé ton char," \
        "de beaux passereaux rapides" \
        "t'entraînaient autour de la terre" \
        "sombre,secouant leurs ailes serrées et du" \
        "haut du ciel tirant droit à travers l'éther."
```

Écrire un programme qui demande à l'utilisateurice de saisir un mot, puis vérifie si ce mot est dans
le texte.

### Exercice 2

Écrire un programme qui vérifie si le mot *banane* est contenue dans une entrée récupérée avec
`input`, en quelle que soit la casse.

### Exercice 3

Écrire un programme qui demande à son utilisateurice son année de naissance et affiche l'âge qu'aura
cette personne en 2022.

Indice : `int`

### Exercice 4

Demander à l'utilisateurice d'entrer un nombre minimal de caractères pour qu'un mot soit considéré
comme long. Puis lui demander de saisir un mot et lui afficher `"😱"` si ce mot est long.

### Réflexion

Quelques points auxquels réfléchir

- Combien de temps avez-vous passé à faire ces exercices ?
- Qu'est-ce qui vous a paru le plus compliqué ?
- À votre avis, pourquoi ?
