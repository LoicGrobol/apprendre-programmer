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

## Fonctions

Dans ce qui précède, `print` est un **appel de fonction**, et `"Hello, world!"` est son argument
<!-- 
À ce stade, une **fonction** en Python ressemble au concept de fonction en sémantique, en logique ou
en mathématiques. On ne va pas rentrer dans des détails formels, mais plutôt garder en tête un
exemple : la phrase « Morgan mange une pomme », peut être vue comme l'action d'une **fonction**,
`manger` sur deux **arguments**, `Morgan` et `une pomme`, qu'on écrit `manger(Morgan, une pomme)`. -->

En Python, on peut penser aux fonctions comme la description d'actions qu'on demande à la machine
d'effectuer : ici « affiche le message que je te donne en argument ».

<!-- - Une fonction qui inverse une chaîne de caractères renvoie une chaîne de caractères.
- Une fonction qui additionne deux nombres renvoie leur somme.
- Une fonction qui compte le nombre de caractères renvoie un nombre.

Et `print` ? Elle renvoie la valeur spéciale `None`, « rien ». Je vous laisse réfléchir aux
implications philosophiques d'un tel objet. -->

Les **arguments** (ou **paramètres**) d'une fonction servent à spécifier les éléments sur lesquels
portent l'action. Il peut y en avoir un, plusieurs ou zéro.

<!-- Par exemple :

- Une fonction qui inverse une chaîne de caractères a un argument : cette chaîne de caractères.
- Une fonction qui renvoie les $n$ premiers mots d'une phrase a deux arguments : la phrase et $n$.
- Une fonction qui affiche « Bonjour, tout le monde ! » a zéro arguments : son exécution sera la
  même à chaque fois.

**Question** : combien faut-il d'arguments pour une fonction qui dessine un cercle ? -->
