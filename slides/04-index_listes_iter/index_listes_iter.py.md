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
Cours 3 : Séquences et boucles
==============================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

Dans ce notebook, on introduit les concepts suivants :

- L'opération *index* et les types de données indicés
- Le type de donnée `list`
- La boucle de parcours `for`

Ce cours est inspiré des cours [*Control flow and
indexing*](https://github.com/aniellodesanto/Utah_CompLang21/blob/main/02_control_flow_and_indexing.ipynb)
et [*Lists and for
loops*](https://github.com/aniellodesanto/Utah_CompLang21/blob/main/03_lists_and_for_loops.ipynb)
d'Aniello de Santo, merci infiniment à lui.

## Index

```python
"Bonjour"[0]
```

```python
"Bonjour"[3]
```


```python
print("Bonjour"[4])
```

<!-- #region -->
D'après vous, qu'afficherait le programme suivant ?

```python
print("Bonjour"[2])
```
<!-- #endregion -->

Testez en exécutant la cellule suivante

```python
print("Bonjour"[2])
```

### Principe de base

L'opération notée par des crochets, qu'on appelle en anglais _**indexing**_ (en français *indexer*,
mais c'est un peu moche), permet d'extraire des parties d'objets composites.

En l'occurrence, une chaîne de caractère est bien un objet **composite** : c'est une suite de
caractères. Elle possède également un **ordre** : `"bestial"` et `"baliste"`, ce n'est pas la même
chose :

```python
"bestial" != "baliste"
```

Ces deux propriétés font qu'il est possible d'accéder à n'importe lequel des caractères d'une chaîne
de caractère via sa **position** : `"Bonjour"[i]` renvoie le `i`-ème caractère de la chaîne, le
caractère dont l'**indice** (ou *index*) est `i`.

On dit que les chaînes de caractères sont des **séquences**, ou encore que ce sont des types (ou
structures) de données **indicées**.

Les entiers, les flottants et les booléens ne sont pas des séquences :

```python tags=["raises-exception"]
1964[2]
```

On peut bien sûr indexer dans une variable contenant une chaîne de caractères :

```python
ma_chaine = "Je reconnais l'existence du kiwi."
print(ma_chaine[0])
print(ma_chaine[1])
print(ma_chaine[2])
print(ma_chaine[3])
print(ma_chaine[4])
```

Et on peut utiliser une variable ou une expression comme indice :

```python
ma_chaine = "Je reconnais l'existence du kiwi."
position = 11
print(ma_chaine[position])
print(ma_chaine[position-1])
```

Dernier point : **en Python, les indices commencent à `0`**.

Ce n'est pas forcément intuitif, et d'ailleurs ce n'est pas le cas de tous les langages de
programmation. Tout le monde se plante de temps en temps, mais il faut le retenir.


### 🔭 Entraînement 🔭

Demandez un mot et un indice `i` à l'utilisateurice. Si le mot a un `i`-ème caractère, affichez ce caractère,
sinon affichez un message d'erreur.

**Indice** : vous savez déterminer la longueur d'une chaîne de caractères.

```python tags=["skip-execution"]
```

### *Slices*

À votre avis, que va afficher la cellule suivante ? Essayez de deviner avant de tester.

```python
print("Bonjour"[2:5])
```

Et celle-ci ?

```python
print("Université Paris Nanterre"[5:10])
```

À votre avis que signifie cette syntaxe ?

---

L'opération dite _**slice**_ (*tranche*) est une extension de l'indexage : au lieu d'extraire un
élément de la séquence, on en extrait une plage, un intervalle, une **sous-séquence**. Précisément :

`ma_chaine[start:end]`, c'est la sous-chaine composée des caractères de `ma_chaine` dont les indices
sont compris entre `start` (inclus) et `end` (exclus).

```python
print("Merveilleux"[3:8])
```

Si `start` vaut `0`, ou que `end` est supérieur ou égal à la longueur de la chaîne, on peut les
omettre :

```python
print("Merveilleux"[:8])
```

```python
print("Merveilleux"[0:8])
```

```python
print("Merveilleux"[3:])
```

### Indices négatifs

Python autorise aussi les indices négatifs. Pouvez-vous en deviner le sens et dire ce que va
afficher la cellule suivante ?

```python
print("Pomme"[-1])
```

On peut également faire des tranches avec des indices négatifs, Même si ça devient rapidement prise
de tête :

```python
print("Pomme"[-4:-1])
print("Pomme"[1:4])
```

En revanche, ceci est fréquent

```python
print("supercallifragilisticexpialidocious"[-3:])
```

### *Step*

En plus des paramètres `start` et `end`, il y a aussi un paramètre optionnel `step` (le *pas*) qui
permet de sélectionner des sous-chaînes discontinues.

```python
"Merveilleux"[2:5:3]
```

```python
"Merveilleux"[::3]
```

Ce pas peut être négatif, auquel cas on parcourt la chaîne à l'envers :

```python
"Merveilleux"[8:2:-3]
```

Est-ce que vous pouvez en déduire une façon d'inverser une chaîne en utilisant que la syntaxe de
*slice* ?

```python
# À vous de jouer
```

(C'est en vérité de loin l'usage le plus fréquent de `step`).

### La méthode `find`

La fonction `str.find(chaine, sous_chaine)` renvoie l'indice de départ de `sous_chaine` dans
`chaine` ou `-1` si on ne l'y trouve pas.

```python
str.find("Une pomme", "n")
```

```python
str.find("Une pomme", "omm")
```

```python
str.find("Une pomme", "poi")
```

Si la sous-chaîne est présente plusieurs fois, seule la première sera prise en compte :

```python
str.find("rock and roll", "ro")
```

**Note** Les fonctions comme `find`, `upper`… sont plus précisément des **méthodes**, c'est-à-dire
des fonctions attachées à un type d'objet en particulier (ici les chaînes de caractères). On peut
les appeler via leur type (`str`) ou via un objet :

```python
"Une pomme".find("pom")
```

On reviendra plus en détails sur ces notions plus tard dans le cours.

## Listes

On a vu qu'une chaîne de caractères était une **séquence** de caractères.

Il existe d'autres types de séquences en Python. Le plus élémentaire est la **liste**, un objet du
type `list`.

Il s'agit d'un conteneur générique qui peut contenir des séquences de n'importe quel type d'objets.

On crée une liste avec la syntaxe suivante (oui, encore des crochets)

```python
a = [1, 2, 3]
print(a)
```

```python
type(a)
```

```python
a = [0.1, 12.5, 13.0]
print(a)
print(type(a))
```

```python
a = ["Je", "reconnais", "l'", "existence", "du", "kiwi"]
print(a)
print(type(a))
```

On peut également mélanger les types

```python
l = [1, "machin", True, 0.000001]
print(l)
print(type(l))
```

Et les éléments peuvent eux-aussi être des listes. Dans l'exemple suivant, `l` est une liste de
trois éléments, le dernier se trouvant être une liste lui-même.

```python
l = [1, "machin", [0, 2]]
print(l)
print(type(l))
```

Comme les chaînes de caractères, les listes sont **ordonnées**

```python
[1, 2, 3] == [3, 1, 2]
```

Elles sont donc également indicées :

```python
ma_liste= ["Je", "reconnais", "l'", "existence", "du", "kiwi"]

print(ma_liste[0])
print(ma_liste[1])
print(ma_liste[-1])
print(ma_liste[1:4])
```

Et on peut obtenir leur longueur

```python
ma_liste= ["J'", "aime", "les", "épinards"]
len(ma_liste)
```

Et donc vérifier que je n'ai pas menti

```python
len([1, "machin", [0, 2]])
```

À votre avis, qu'affiche la cellule suivante ?

```python
ma_liste = [1, "machin", [9, 2]]
print(ma_liste[2][0])
```

Enfin, une liste peut avoir un seul élément

```python
une_autre_liste = ["tout seul"]
```

voire être vide

```python
une_autre_liste = []
```

Attention donc à bien identifier les éléments : qu'affiche la cellule suivante ?

```python
ma_liste= ["J', aime, les, épinards"]
print(len(ma_liste))
```

### Modifier des listes

Les listes sont **mutables**, on peut les modifier avec les méthodes suivantes

#### `append`

`append` ajoute un nouvel élément à une liste existante :

```python
ma_liste = [1, 2, 3]
ma_liste.append("un de plus")         
print(ma_liste)
```


```python
one_list = [1, 2, 3]
another_list = [True, "linguistique"]
one_list.append(another_list)
print(one_list)
```

Combien d'éléments a `one_list` ?

```python
print(one_list, "a", len(one_list), "éléments")
```

#### `extend`

`extend` ajoute à une liste tous les éléments d'une autre liste :

```python
one_list = [1, 2, 3]
another_list = [True, "linguistique"]
one_list.extend(another_list)
print(one_list)
```

est donc équivalent à

```python
one_list = [1, 2, 3]
another_list = [True, "linguistique"]
one_list.append(another_list[0])
one_list.append(another_list[1])
print(one_list)
```

#### `insert`

Enfin, `insert` permet d'insérer des éléments à une position arbitraire dans une liste

```python
states = ["California", "New York", "Arizona"]
states.insert(1, "Colorado")
print(states)
```

```python
states = ["California", "New York", "Arizona"]
states.insert(2, 12)
print(states)
```

On évite en général de s'en servir quand on peut utiliser `append` à la place.

#### `remove` et `pop`

`remove` ôte la première occurrence d'un élément

```python
states = ["California", "New York", "Arizona"]
states.remove("Arizona")
print(states)
```

Mais **seulement** la première :

```python
states = ["California", "New York", "Arizona", "New York"]
states.remove("New York")
print(states)
states.remove("New York")
print(states)
```

Pour supprimer le dernier élément de la liste, quelle que soit la valeur de cet élément, on utilise
`pop` :

```python
states = ["California", "New York", "Arizona", "New York"]
print(states)
states.pop()
print(states)
```

On peut aussi modifier la valeur d'un élément par position de la façon suivante :

```python
cities = ["NYC", "LA"]
print(cities)
cities[0] = "SF"
print(cities)
```

### `in`

```python
34 in [1, 2, 34, 54, 'abc']
```

```python
"truc" in [1, 2, 34, 54, 'abc']
```

### 🛠️ Entraînement 🛠️

Voici une liste de lettres :

```python
letters = ["d", "b", "c", "n"]
```

Insérez `"x"` en position `3`, puis retirez `"c"`, ajoutez `"e"` à la fin, supprimez l'élément
d'indice `2`, et, finalement remplacez l'élément en position `1` par `"o"`. Puis affichez le contenu
de la liste

```python

```

## Boucle `for`

Nous disposons à présent de **séquences** : les chaînes de caractères et les listes. Il nous manque
un outil pour pouvoir faire des choses vraiment intéressantes avec.

Observez les cellules suivantes

```python
for char in "Chocolat":
    print(char)  
```

```python
for el in ["a", "e", "i", 1, True]:
    print(el)
```

Pouvez-vous en déduire ce qu'affichent les cellules suivantes ?

```python
for c in "Seitan":
    print(c)
```

```python
for i in [1, 2, 3, 4, 5]:
    print(i)
```

Et la cellule suivante ?

```python
for i in [1, 2, 3, 4, 5]:
    j = 2*i
    print(j)
print("hello")
```

---

Le mot-clé `for` permet de définir une **boucle** (spécifiquement une boucle d'itérateur) : un bloc
de code qui sera exécuté pour chacun des éléments d'une séquence, et dans lequel on a accès à la
valeur de cet élément.

Il s'agit comme pour les blocs `if`-`elif`-`else` d'une **structure de contrôle**.

Le bloc de code qui est répété (le **corps de la boucle**) est marqué là encore par des alinéas.

La syntaxe formelle exacte est

```text
for <nom-de-variable> in <sequence>:
    Instruction 1
    Instruction 2
    …
```

Notez bien les `:` à la fin de la ligne `for`. Là encore, c'est comme pour `if`.


On peut combiner boucles et tests

```python
voyelles = ["a", "e", "i", "o", "u"]
for char in "linguistique":
    if char in voyelles:
        print("J'ai trouvé une voyelle :", char)
```

Et les boucles peuvent être imbriquées :


```python
cities = ["NYC", "LA", "SF"]

for city in cities:
    print("La ville est", city)
    print("Ses lettres sont :")

    for letter in city:
        print(letter)
```

## Exercices

## Exercice 1

Voici deux listes

```python
cities = ["NYC", "LA", "SF"]
small_cities = ["Stony Brook", "Provo"]

# Codez ici
```

**Ajoutez** des instructions à la cellule suivante de sorte à modifier `cities` pour que son contenu
soit

1. `["NYC", "LA", "SF", "Stony Brook", "Provo"]`.
2. `["NYC", "LA", "Stony Brook", "Provo", "SF"]`.

## Exercice 2

Voici une liste

```python
villes = ["Paris", "Nanterre", "Orléans", "Uppsala"]
```

En utilisant cette liste, écrivez un programme qui affiche la sortie suivante

```text
Paris Paris
Paris Nanterre
Paris Orléans
Paris Uppsala
Nanterre Paris
Nanterre Nanterre
Nanterre Orléans
Nanterre Uppsala
Orléans Paris
Orléans Nanterre
Orléans Orléans
Orléans Uppsala
Uppsala Paris
Uppsala Nanterre
Uppsala Orléans
Uppsala Uppsala
```

```python
# codez ici
```

### Exercice 3

Voici quelques mots de la [Liste Swadesh](https://fr.wikipedia.org/wiki/Liste_Swadesh).

```python
words = ["soleil", "lune", "terre", "eau", "nourriture", "ciel"]
```

Imaginez que vous êtes un⋅e linguiste de terrain en train de collecter du vocabulaire pour
documenter une langue :

- Créez une liste vide dans une variable `traduction`.
- Pour chacun des mots de la liste `words`, demandez à l'utilisateurice d'entrer sa traduction et
  sauvegardez cette entrée dans `traductions`.
- Une fois que vous avez terminé, affichez la valeur de `traductions`.

```python
# Codez ici
```

### Réflexion

Quelques questions sur votre travail :

- Combien de temps avez-vous passé à faire ces exercices ?
- Combien de temps avez-vous passé à relire le cours (ou les cours précédents) ?
- Avez-vous l'impression d'avoir bien mémorisé les concepts et les techniques vus jusqu'ici ?
- Qu'est-ce qui vous paraît le plus compliqué ?
- À votre avis, pourquoi ?

Merci de bien répondre à chacune de ces questions : elles me permettent d'ajuster le cours en
fonction de vos besoins, avec un peu de chance, elles devraient également vous aider à guider votre
travail et à apprécier votre progression.
