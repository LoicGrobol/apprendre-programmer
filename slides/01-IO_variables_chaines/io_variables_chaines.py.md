---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.3
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
`'Bonjour, tout le monde !' ou `"supercalifragillisticexpialidocious"`. Elles sont notées entre
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

En général, c'est plus pratique d'utiliser des double quotes, notamment parce que c'est plus agréable d'y utiliser `'` comme apostrophe

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

À votre avis, peut-on utiliser les autres opérateurs arithmétiques avec des chaînes de caractères ? Testez ci-dessous. Vous pouvez aussi créer de nouvelles cellules dans le notebook.

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

Le `f` devant les quotes signales qu'on utilise un *format string* pour une *interpolation*. On en reparlera.

On peut aussi, convertir des `int` en `float`

```python
float(2713)
```

Et vice-versa, mais qu'est-ce que ça va donner d'après vous ?

```python
int(7.9)
```

### Booléens

Un dernier type : les **booléens** (*boolean*, `bool`), qui ne peuvent prendre que deux valeurs `True` (vrai) et `False` (faux).


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