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
Cours 7 : Compléments sur les boucles et les séquences
======================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-02-22
<!-- #endregion -->

Dans ce notebook, des nouveaux outils pour travailler avec les boucles, les listes et les chaînes
des caractères :

- Itérateurs `range` et `enumerate` pour les itérations sur des nombres et simultanément sur listes
  et nombres.
- Itérateur `zip` pour les itérations simultanées génériques.
- Méthodes de chaînes de caractères `split` et `join` pour segmenter et concaténer des chaînes,
  ainsi que `replace`.

## Boucles `for` : rappels

Les boucles `for` permettent de parcourir une séquence, en considérant dans l'ordre chacun de ses
éléments :

```python
for lettre in "pomme":
    print(lettre)
```

On dit qu'on a **itéré** sur la séquence, ce qui est possible parce qu'une séquence est un
**itérable**.

Il n'y a d'ailleurs pas d'obligation d'utiliser les valeurs des éléments :

```python
for letter in "apple":
    print("hello")
```

C'est assez rare d'avoir à faire ça, mais si on le fait, par **convention**, on utilise souvent
l'underscore `_` comme nom de variable de boucle, avec comme sens implicite « cette valeur ne sera
pas utilisée ».

```python
for _ in "apple":
    print("hello")
```

On peut itérer sur des listes :

```python
indices = [0, 1, -1, -4]
word = "linguistics"

for index in indices:
    print(word[index])
```

Et imbriquer des boucles les unes dans les autres :

```python
cities = ["NYC", "LA", "SF"]

for city in cities:
    print("The current city is", city)
    for ch in city:
        print("\t", ch)
```

## Recette : compteurs

Pour afficher l'**indice** de l'élément courant, on peut utiliser un **compteur** : une variable
dont la valeur initiale sera $0$ et à laquelle on ajoutera $1$ (**incrémenter**) à chaque itération
(« tour de boucle »).

```python
index = 0
for lettre in "linguistique":
    print(lettre, " indice :", index)
    index = index + 1
```

On peut s'en servir pour compter les éléments d'une séquence qui vérifient une certaine condition.
Par exemple :

```python tags=["skip-execution"]
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]
mot = input("Dis-moi un mot : ")

compteur = 0
for lettre in mot:
    if lettre in voyelles:
        compteur = compteur + 1
print(compteur)
```

On peut aussi utiliser un compteur pour garder trace de l'indice de l'élément actuel dans la
séquence sur laquelle on itère :

Voici une liste d'états des États-Unis `states`, une liste des températures moyennes de
ces états `temperatures` (données dans le même ordre), et une liste des états considérés comme
faisant partie de la Nouvelle-Angleterre `new_england`.

```python
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]

new_england = ["Maine", "Vermont", "New Hampshire", "Massachusetts", "Connecticut",
               "Rhode Island"]
```

La cellule ci-dessous calcule et affiche les températures moyennes des états de Nouvelle-Angleterre,
en utilisant la variable `index` pour stocker l'indice de l'état en cours dans la liste `states` et
pouvoir trouver son pendant dans la liste `temperatures` :

```python
index = 0
for state in states:
    if state in new_england:
        print(state+":", temperatures[index])
    index = index + 1
```

### Entraînement : compteurs et accumulateurs

#### .1 Compter les *stop words*

Voici un paragraphe, segmenté en mots :

```python
paragraphe = ["C'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'Il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'Pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique', 'Le', 'terme', "d'", 'informaticien', 'semble', "d'", 'ailleurs', 'recouper', 'une', 'grande', 'diversité', 'de', 'métiers', 'et', "d'", 'occupations', 'réelles', 'allant', 'du', 'technicien', 'à', "l'", 'ingénieur', 'réseau', 'en', 'passant', 'par', 'le', 'webmaître', 'Quant', 'à', 'la', 'nature', 'du', 'travail', 'de', 'ceux', 'qui', 'font', 'de', 'la', 'recherche', 'en', 'informatique', "c'", 'est', 'sans', 'doute', 'à', 'en', 'juger', 'par', 'les', 'réactions', 'auxquelles', "j'", 'ai', 'moi', 'même', 'été', 'confrontée', 'une', 'mystère', 'encore', 'plus', 'épais', 'malgré', 'le', 'prestige', 'un', 'peu', 'mythique', 'que', 'conservent', 'des', 'projets', 'comme', 'ceux', 'de', 'la', 'robotique', 'ou', 'de', "l'", 'intelligence', 'artificielle', 'Ce', 'document', 'se', 'veut', 'en', 'partie', 'une', 'réponse', 'à', 'ceux', 'qui', 'se', 'demandent', 'quels', 'sont', 'les', 'fondements', 'de', "l'", 'informatique', 'Il', "n'", 'est', 'pas', 'conçu', 'pour', 'initier', 'au', 'maniement', 'pratique', 'des', 'ordinateurs', 'ce', "n'", 'est', 'pas', 'une', 'introduction', 'à', 'la', 'bureautique', 'Ce', "n'", 'est', 'pas', 'non', 'plus', 'un', 'manuel', 'technique', 'à', "l'", 'usage', 'de', 'ceux', 'qui', 'souhaitent', 'bricoler', 'leur', 'machine', 'favorite', 'Si', 'au', 'fil', 'des', 'pages', 'des', 'informations', 'utiles', 'à', 'ces', 'deux', 'catégories', "d'", 'utilisateurs', 'ou', 'aux', 'novices', 'pourront', 'être', 'glanées', 'vocabulaire', 'spécialisé', 'typologie', 'de', 'matériels', 'ordre', 'de', 'grandeurs', 'des', 'performances', 'des', 'machines', 'actuelles', 'tel', "n'", 'est', 'pas', 'son', 'objectif', 'premier', "L'", 'informatique', 'dont', 'il', 'sera', 'question', 'ici', 'est', 'une', 'discipline', 'scientifique', 'qui', 'en', 'tant', 'que', 'telle', 'a', 'ses', 'propres', 'questions', 'ses', 'propres', 'problèmes', 'et', 'dispose', 'pour', 'les', 'aborder', "d'", 'outils', 'et', 'de', 'méthodes', 'spécifiques', 'De', 'cette', 'discipline', 'on', 'abordera', 'les', 'fondements', 'théoriques', 'ainsi', 'que', 'quelques', 'réalisations', 'pratiques', 'mais', 'on', 'insistera', 'plus', 'sur', 'les', 'concepts', 'que', 'sur', 'la', 'technique', 'Cette', 'présentation', 'relève', 'donc', 'principalement', "d'", 'une', 'démarche', 'de', 'vulgarisation', 'scientifique', 'destinée', 'à', 'un', 'public', 'de', 'non', 'spécialistes', 'mais', 'qui', 'se', 'place', 'à', 'un', 'niveau', 'non', 'trivial', 'difficilement', 'trouvable', 'dans', 'les', 'manuels', 'habituellement', 'disponibles', "J'", 'ai', 'ici', 'essayé', 'de', 'décrire', 'de', 'façon', 'aussi', 'abordable', 'que', 'possible', 'ce', 'que', 'en', 'tant', "qu'", 'informaticienne', 'je', 'souhaite', 'que', "l'", 'honnête', 'homme', 'du', 'XXIème', 'siècle', 'sache', 'et', 'pense', 'de', 'ma', 'discipline', 'appelée', 'à', 'coup', 'sûr', 'à', 'un', 'grand', 'développement', 'dans', 'les', 'années', 'qui', 'viennent']
```

À l'aide d'une boucle et d'un compteur, déterminer le nombre de mots de ce paragraphe qui
appartiennent à la liste `stop_words` suivante.

```python
stop_words = ["le", "la", "les", "l'", "un", "une", "des", "de", "d'", "à"]
# Codez ici
```

### 2. Accumulateurs

Voici une liste de nombres

```python
numb3rs = [2, 3, 6, 3, 8, 2, 10, 2, 8, 3, 7, 7, 3, 5, 2, 7, 7, 3, 7, 2, 7, 4, 3, 6, 3, 4, 10, 2, 4, 7, 3, 7, 7, 2, 3, 4, 1, 2, 7, 2, 8, 5, 2, 11, 2, 2, 3, 8, 8, 2, 12, 3, 7, 8, 2, 10, 3, 4, 7, 4, 8, 3, 6, 2, 5, 10, 2, 2, 3, 7, 2, 5, 2, 13, 6, 2, 8, 8, 3, 6, 9, 2, 7, 2, 2, 11, 7, 6, 2, 10, 1, 2, 9, 6, 2, 7, 3, 2, 9, 5, 1, 2, 6, 2, 7, 2, 4, 3, 4, 2, 2, 9, 2, 12, 2, 3, 4, 5, 1, 2, 5, 3, 3, 9, 10, 2, 2, 3, 4, 3, 10, 3, 7, 6, 4, 5, 6, 2, 8, 2, 3, 8, 3, 10, 3, 7, 5, 4, 2, 2, 9, 2, 2, 2, 12, 12, 2, 8, 2, 4, 2, 6, 3, 7, 1, 4, 3, 2, 9, 5, 4, 3, 10, 2, 2, 12, 2, 2, 3, 3, 5, 4, 7, 2, 9, 8, 3, 11, 2, 2, 3, 3, 3, 12, 1, 2, 11, 2, 2, 3, 3, 3, 4, 2, 6, 9, 1, 2, 5, 2, 4, 3, 10, 8, 4, 7, 8, 2, 2, 3, 3, 5, 3, 12, 6, 1, 3, 4, 10, 2, 12, 2, 3, 7, 8, 4, 7, 11, 10, 9, 2, 9, 5, 2, 9, 3, 12, 3, 8, 9, 3, 2, 3, 3, 3, 8, 7, 2, 12, 4, 2, 4, 8, 3, 3, 3, 10, 12, 3, 2, 4, 3, 5, 1, 3, 7, 9, 3, 7, 9, 2, 7, 4, 3, 7, 2, 6, 2, 2, 8, 11, 2, 5, 10, 2, 8, 3, 10, 10, 5, 3, 8, 12, 9, 4, 2, 9, 4, 3, 3, 8, 3, 3, 2, 9, 5, 12, 6, 4, 14, 2, 3, 8, 2, 13, 12, 8, 1, 2, 6, 2, 3, 12, 4, 3, 2, 5, 1, 2, 6, 3, 7, 13, 9, 4, 3, 7, 14, 11, 2, 2, 3, 6, 2, 7, 2, 5, 5, 9, 3, 8, 2, 3, 2, 4, 3, 15, 2, 8, 3, 2, 7, 5, 2, 6, 6, 5, 2, 5, 2, 2, 10, 7, 1, 4, 3, 1, 2, 5, 13, 4, 3, 6, 3, 8]
```

À l'aide d'une boucle, calculer et afficher leur somme et leur moyenne

```python

```

### 3. Max

Voici la même liste de nombres

```python
numb3rs = [2, 3, 6, 3, 8, 2, 10, 2, 8, 3, 7, 7, 3, 5, 2, 7, 7, 3, 7, 2, 7, 4, 3, 6, 3, 4, 10, 2, 4, 7, 3, 7, 7, 2, 3, 4, 1, 2, 7, 2, 8, 5, 2, 11, 2, 2, 3, 8, 8, 2, 12, 3, 7, 8, 2, 10, 3, 4, 7, 4, 8, 3, 6, 2, 5, 10, 2, 2, 3, 7, 2, 5, 2, 13, 6, 2, 8, 8, 3, 6, 9, 2, 7, 2, 2, 11, 7, 6, 2, 10, 1, 2, 9, 6, 2, 7, 3, 2, 9, 5, 1, 2, 6, 2, 7, 2, 4, 3, 4, 2, 2, 9, 2, 12, 2, 3, 4, 5, 1, 2, 5, 3, 3, 9, 10, 2, 2, 3, 4, 3, 10, 3, 7, 6, 4, 5, 6, 2, 8, 2, 3, 8, 3, 10, 3, 7, 5, 4, 2, 2, 9, 2, 2, 2, 12, 12, 2, 8, 2, 4, 2, 6, 3, 7, 1, 4, 3, 2, 9, 5, 4, 3, 10, 2, 2, 12, 2, 2, 3, 3, 5, 4, 7, 2, 9, 8, 3, 11, 2, 2, 3, 3, 3, 12, 1, 2, 11, 2, 2, 3, 3, 3, 4, 2, 6, 9, 1, 2, 5, 2, 4, 3, 10, 8, 4, 7, 8, 2, 2, 3, 3, 5, 3, 12, 6, 1, 3, 4, 10, 2, 12, 2, 3, 7, 8, 4, 7, 11, 10, 9, 2, 9, 5, 2, 9, 3, 12, 3, 8, 9, 3, 2, 3, 3, 3, 8, 7, 2, 12, 4, 2, 4, 8, 3, 3, 3, 10, 12, 3, 2, 4, 3, 5, 1, 3, 7, 9, 3, 7, 9, 2, 7, 4, 3, 7, 2, 6, 2, 2, 8, 11, 2, 5, 10, 2, 8, 3, 10, 10, 5, 3, 8, 12, 9, 4, 2, 9, 4, 3, 3, 8, 3, 3, 2, 9, 5, 12, 6, 4, 14, 2, 3, 8, 2, 13, 12, 8, 1, 2, 6, 2, 3, 12, 4, 3, 2, 5, 1, 2, 6, 3, 7, 13, 9, 4, 3, 7, 14, 11, 2, 2, 3, 6, 2, 7, 2, 5, 5, 9, 3, 8, 2, 3, 2, 4, 3, 15, 2, 8, 3, 2, 7, 5, 2, 6, 6, 5, 2, 5, 2, 2, 10, 7, 1, 4, 3, 1, 2, 5, 13, 4, 3, 6, 3, 8]
```

À l'aide d'une boucle, déterminer le nombre le plus grand (le maximum) de cette liste

```python

```

### 4. Le pot aux roses

Voici quelques fonctions bien utiles :

```python
lst = [3, 6, 5, 12, -4]
print(max(lst))
print(min(lst))
print(sum(lst))
```

Pouvez-vous expliquer ce qu'elles font ?




#### 5. Min

Voici une liste de noms

```python
names = ['Nicole-Reine Lepaute', 'Ada Lovelace', 'Maria Mitchell', 'Anna Winlock', 'Henrietta Swan Leavitt', 'Beatrice Mabel Cave-Browne-Cave', 'Mary Clem', 'Edith Clarke', 'Grete Hermann', 'Johanna Piesch', 'Mavis Batey', 'Gertrude Blanch', 'Ruth Leach Amonette', 'Marlyn Meltzer', 'Jean Bartik', 'Irma Wyman', 'Kathleen Booth', 'Dorothy Vaughan', 'Grace Hopper', 'Evelyn Boyd Granville', 'Ida Rhodes', 'Kathleen Booth', 'Betty Holberton', 'Klára Dán von Neumann', 'Thelma Estrin', 'Annie Easley', 'Kateryna Iouchtchenko', 'Marguerite Frank', 'Grace Hopper', 'Kathleen Booth', 'Alice Recoque', 'Mary K. Hawes', 'Marion Créhange', 'Jean E. Sammet', 'Stephanie Shirley', 'Joan Ball', 'Sharla Boehm', 'Mary Allen Wilkes', 'Mary Kenneth Keller', 'Vera Molnár', 'Jean E. Sammet', 'Margaret Hamilton', 'Alexandra Illmer Forsythe', 'Drude Berntsen', 'Erna Schneider Hoover', 'Adele Goldberg', 'Karen Spärck Jones', 'Susan Nycum', 'Phyllis Fox', 'Elizabeth J. Feinler', 'Rózsa Péter', 'Carol Shaw', 'Sophie Wilson', 'Christiane Floyd', 'Lynn Conway', 'Carol Shaw', 'Ruzena Bajcsy', 'Ruth M. Davis', 'Roberta Williams', 'Lorinda Cherry', 'Roberta Williams', 'Susan Kare', 'Radia Perlman', 'Irma Wyman', 'Nancy Hafkin', 'Monica S. Lam', 'Anita Borg', 'Joëlle Coutaz', 'Rena Tangens', 'Éva Tardos', 'Frances Allen', 'Frances Brazier', 'Ruzena Bajcsy', 'Carol Bartz', 'Shafi Goldwasser', 'Barbara Liskov', 'Carolyn Gruyer', 'Mary Lou Jepsen', 'Xiaoyuan Tu', 'Anita Borg', 'Chieko Asakawa', 'Manuela M. Veloso', 'Meg Whitman', 'Marissa Mayer', 'Carly Fiorina', 'Sun Yafang', 'Noriko H. Arai', 'Ellen Spertus', 'Margaret Hamilton', 'Susan Elizabeth Black', 'Jeri Ellsworth', 'Safra Catz', 'Audrey Tang', 'Mary Lou Jepsen', 'Facebook', 'Xiaoyun Wang', 'Maria Klawe', 'Joanna Rutkowska', 'Frances Allen', 'Anne-Marie Kermarrec', 'Barbara Liskov', 'Carol Bartz', 'Farida Bedwei', 'Meg Whitman', 'Noriko H. Arai', 'Shikoh Gitau', 'Shafi Goldwasser', 'Ginni Rometty', 'Éva Tardos', 'Regina Honu', 'Christine Paulin-Mohring', 'Coraline Ada Ehmke', 'Kesha Shah', 'Audrey Tang', 'Kate Devlin', 'Michelle Simmons', 'Regina Honu', 'Gladys West']
```

1\. À l'aide d'une boucle, déterminer la longueur du nom le plus court de cette liste

```python

```

2\. À l'aide d'une boucle, déterminer le nom le plus court de cette liste

```python

```

## `range` : les intervalles entiers

Comment faire pour afficher dix fois « Bonjour » ?

Il y a une réponse simpliste : « je copie-colle `print("Hello")` dix fois ».

Mais ce n'est pas très satisfaisant, non ?

Une solution avec la boucle `for` :

```python
for _ in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Bonjour")
```

Mais ce n'est toujours pas très pratique d'écrire cette liste. Surtout pour ne rien en faire.
Heureusement, il y a un outil pour nous faciliter la vie : la fonction `range` :

```python
for _ in range(10):
    print("Bonjour")
```

Pas mal, non ?

```python
for i in range(10):
    print(i)
```

Vous devinez ce que renvoie `range(10)` ? À votre avis que renverrait `range(16)` ?

On teste ?

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)
```

```python
print(range(10))
```

Ah

Ce n'est pas très informatif. Dans les temps anciens de la version 2 de Python, `range(n)` renvoyait
la liste des entiers de $0$ à $n$. Depuis, les temps ont changé et `range` renvoie simplement un
objet de type `range`.

```python
print(type(range(10)))
```

Vous pouvez itérer dessus :

```python
for i in range(16):
    print(i)
```

Pourquoi `range` ne renvoie pas une liste ? Parce que ça ne servirait pas à grand-chose : vous
connaissez déjà les valeurs des éléments d'un `range`, pas besoin d'indexer. En plus, ça permet
d'éviter de stocker tous les éléments de la liste en mémoire, ça prend moins de place, votre machine
est contente.

Les objets de type `range` sont donc des objets pour lesquels il n'y pas d'opérations d'indexation,
ce ne sont donc pas des **séquences**. En revanche on peut itérer dessus, ce sont donc des
**itérables**.

En plus de la borne supérieure, on peut aussi spécifier la borne inférieure :

```python
for i in range(-2, 16):
    print(i)
```

Les règles sont toujours les mêmes en Python : la borne inférieure est incluse, la borne supérieure
est exclue.

```python
for value in range(512, 1024):
    print(value)
```

Bon, mais si on veut **vraiment** la liste de ces nombres ?

On peut l'obtenir en utilisant la fonction `list` :

```python
print("L'objet range:", range(10))
print("La liste qui correspond:", list(range(10)))
```

Enfin, on peut également (mais c'est plus rarement utile) préciser le pas :

```python
for value in range(1, 10, 2):
    print(value)
```

Un des usages très répandu de `range` est de permettre de parcourir à la fois une séquence et ses
indices : au lieu de ça :

```python
mot = "linguistique"
index = 0
for lettre in mot:
    print(lettre, " indice :", index)
    index = index + 1
```

on peut écrire ça :

```python
mot = "linguistique"
for i in range(len(mot)):
    print(mot[i], " indice :", i)
```

qui est plus compact, et un peu plus agréable (on a plus à gérer manuellement le compteur).

Attention, ce n'est pas optimale et on verra mieux plus tard, mais pour l'instant on va s'en
servir pour s'entraîner à manipuler des `range`.

## 🍄 Exo 🍄

Écrire un programme qui demande à l'utilisateurice de saisir les uns après les autres ses cinq
aliments préférés. Stocker ces réponses dans une liste, puis affichez les éléments de cette liste,
chacun sur une ligne.

```python

```

## ⚒️ Exo : n-grammes ⚒️

Le concept de **n-gramme** est fondamental en TAL. Un n-gramme, c'st une suite de $n$ symboles. Par
exemple dans le mot « banane », les 2-grammes (bigrammes) de caractères sont :

- ba
- an
- na
- ne

Et dans le mot « linguiste », les 3-grammes (trigrammes) de caractères sont :

- lin
- ing
- ngu
- gui
- uis
- ist
- ste

Écrire un programme qui demande la saisie d'un mot et affiche tous les bigrammes de caractères de ce
mot. Il vous faudra utiliser une boucle `for`, et probablement des outils parmi ceux qu'on a vu dans
cette séance.

## D'autres façons d'itérer

Deux nouvelles fonctions qu'on utilise très souvent en Python. On ne va pas y passer beaucoup de
temps tout de suite, mais sachez que ça existe, on les rencontrera d'autres fois.

### `enumerate`

```python
liste = ["le", "petit", "chat", "est", "content"]
for truc in enumerate(liste):
    print(truc)
```

La fonction `enumerate`, appliqué à une séquence renvoie une **itérable** (comme `range`) dont les
éléments sont des couples `(indice, élément)` composés des éléments de la séquence. Ça permet de
remplacer ceci :

```python
mot = "linguistique"
for i in range(len(mot)):
    print(mot[i], " indice :", i)
```

par ceci

```python
mot = "linguistique"
for couple in enumerate(mot):
    print(couple[1], " indice :", couple[0])
```

qui est *un peu* plus lisible. On peut aussi utiliser la syntaxe suivante, dont on reparlera plus
tard :

```python
mot = "linguistique"
for idx, lettre in enumerate(mot):
    print(lettre, " indice :", idx)
```

c'est encore plus lisible et c'est le style recommandé en Python (pour plusieurs raisons, là aussi
on en reparlera).

### `zip`

```python
villes = ["Orléans", "Tours", "Nanterre"]
cp = ["45000", "37000", "92000"]
for truc in zip(villes, cp):
    print(truc)
```

`zip` permet d'itérer sur plusieurs séquences en parallèle

```python
villes = ["Orléans", "Tours", "Nanterre"]
cp = ["45000", "37000", "92000"]
appreciation = ["cool", "génial", "super"]
for truc in zip(villes, cp, appreciation):
    print(truc)
```

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021"]
appreciation = ["cool", "génial", "super"]
for truc in zip(villes, annee, appreciation):
    print("Où:", truc[0], "Quand:", truc[1], "Comment:", truc[2])
```

Là aussi on peut utiliser cette nouvelle syntaxe pour que ce soit plus lisible :

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021"]
appreciation = ["cool", "génial", "super"]
for ou, quand, comment in zip(villes, annee, appreciation):
    print("Où:", ou, "Quand:", quand, "Comment:", comment)
```

Est-ce que vous voyez comment simuler `enumerate` en utilisant `zip` ?


Un dernier point : c'est quoi exactement ces éléments que renvoient `zip` et `enumerate`, ça ressemble à des listes mais avec des parenthèses ?

```python
villes = ["Orléans", "Tours", "Nanterre"]
annee = ["1991", "2014", "2021"]
appreciation = ["cool", "génial", "super"]
for truc in zip(villes, annee, appreciation):
    print(type(truc))
```

Ce sont es `tuple`s, effectivement ça ressemble à des listes mais pas tout à fait. On les retrouvera plus tard !

## Encore des manipulations de chaînes 😤

Quelques nouvelles méthodes de manipulations de chaînes de caractères. Là aussi on les rencontrera
dans le futur :

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

### `split`

`split` découpe, tronçonne, une chaîne de caractères

```python
texte = "You ever have that feeling, where you’re not sure if you’re awake or still dreaming?"
tokens = str.split(texte)
print(tokens)
```

C'est une façon rapide et simple (simpliste ?) de découper un texte en tokens.

Vous pouvez aussi utiliser un autre séparateur que les espaces :

```python
texte = "bleu,rouge,indigo,vert"
colours = str.split(texte, ",")
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
print(texte)
```


```python
letters = ['P', 'y', 't', 'h', 'o', 'n']
print(str.join("", letters))
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

## Exercices

Répondre à ces exercices directement dans le notebook, le sauvegarder sous un nom de la forme
`07_boucles_sequences_PRENOM_NOM.ipynb` (pour Morgan Lefeuvre par exemple, ce serait
`07_boucles_sequences_Morgan_Lefeuvre.ipynb`) et me le transmettre avant dimanche 2022-03-06 au soir.
(2022-02-06).

- De préférence via [Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7694)
  (clé d'inscription `rossum`)
- À défaut, par mail, à `<lgrobol@parisnanterre.fr>`

Attention : **l'extension doit être `.ipynb`**.

Cette fois-ci ils sont assez longs, ne vous y prenez pas au dernier moment et n'hésitez pas à
revenir sur les cours et les corrigés précédents pour trouver des idées.

### Consonnes

Voici une liste de voyelles

```python
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]
```

Écrire un programme qui demande la saisie d'un mot et affiche le nombre de consonnes (donc de lettre
qui ne sont pas de voyelles) dans ce mot.

```python

```

### N-grammes

Écrire un programme qui demande la saisie d'un mot et d'un entier `n`, puis affiche la liste des
n-grammes de caractères de ce mot.

Indices :

- Partez d'un programme qui affiche la liste des bigrammes, puis essayez de généraliser à un n
  arbitraire
- Attention aux cas particuliers : que faire des n premiers et derniers caractères du mot ? Que
  faire si le mot fait moins de n caractères…

```python

```

## Encore des bigrammes

Voici un texte

```python
text = "It was dark, like the bottom of a well. There was a pattern of skulls and bones around \
the frame, for the sake of appearances; Death could not look himself in the skull in a mirror \
with cherubs and roses around it. The Death of Rats climbed the frame in a scrabble of claws and \
looked at Death expectantly from the top. Quoth fluttered over and pecked briefly at his own \
reflection, on the basis that anything was worth a try. Show me, said Death, show me my thoughts. \
A chessboard appeared, but it was triangular, and so big that only the nearest point could be seen. \
Right on this point was the world - turtle, elephants, the little orbiting sun and all. It was the \
Discworld, which existed only just this side of total improbability and, therefore, in border country. \
In border country the border gets crossed, and sometimes things creep into the universe that have \
rather more on their mind than a better life for their children and a wonderful future in the \
fruit picking and domestic service industries. On every other black or white triangle of the \
chessboard, all the way to infinity, was a small grey shape, rather like an empty hooded robe."
```

<!-- #region -->
1\. Écrire un programme qui génère la liste `unique_words`, qui contient tous les mots du texte,
sans doublons, et en minuscules. Le résultat devrait être le suivant (l'ordre peut être différent) :

```python
['a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', 'fruit', 'picking', 'there', 'try', 'little', 'around', 'appearances', 'appeared', 'all', 'crossed', 'basis', 'improbability', 'their', 'discworld', 'black', 'to', 'death', 'future', 'only', 'my', 'robe', 'things', 'for', 'it', 'existed', 'said', 'sake', 'sometimes', 'right', 'way', 'that', 'country', 'chessboard', 'quoth', 'well', 'domestic', 'skull', 'wonderful', 'hooded', 'or', 'empty', 'bottom', 'mirror', 'himself', 'rather', 'over', 'every', 'triangle', 'roses', 'border', 'orbiting', 'was', 'from', 'show', 'be', 'pecked', 'bones', 'just', 'universe', 'me', 'triangular', 'gets', 'worth', 'have', 'climbed', 'service', 'fluttered', 'top', 'but', 'grey', 'claws', 'at', 'rats', 'creep', 'own', 'pattern', 'point', 'white', 'than', 'dark', 'therefore', 'frame', 'this', 'not', 'the', 'could', 'mind', 'turtle', 'scrabble', 'better', 'industries', 'looked', 'an', 'cherubs', 'life', 'anything', 'more', 'small', 'and', 'of', 'his', 'on', 'skulls', 'elephants', 'in', 'thoughts', 'seen', 'nearest', 'expectantly', 'other', 'side', 'shape', 'total', 'so', 'world', 'look', 'sun']
```

(évidemment ne faites pas juste un copier-coller)

<!-- #endregion -->

```python

```

2\. Écrire un programme qui extrait à partir de la liste `unique_words` la liste `attested_bigrams`
des bigrammes de caractères qui apparaissent dans le texte.

**Indice** Vous pouvez utiliser le code de l'exercice précédent, que vous appliquerez successivement
à chacun des mots de `unique_words`, en agrégeant les résultats dans une seule liste, et en vous
assurant de ne pas créer de doublons.


```python

```

3\. Voici une liste des lettres de l'alphabet anglais. Utilisez-la pour générer une liste
`possible_bigrams` de tous les bigrammes de caractères théoriquement possibles en anglais.


```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

4\. Écrire un programme qui génère la liste `unattested_bigrams` des bigrammes de caractères
non attestés, c'est-à-dire de tous les bigrammes qui sont possibles, mais qu'on ne trouve pas dans
ce texte.

```python

```

### Réflexion

Quelques questions sur votre travail :

- Combien de temps avez-vous passé à faire ces exercices ?
- Combien de temps avez-vous passé à relire le cours (ou les cours précédents) ?
- Avez-vous l'impression d'avoir bien mémorisé les concepts et les techniques vus jusqu'ici ?
- Qu'est-ce qui vous paraît le plus compliqué ?
- À votre avis, pourquoi ?

Merci de bien répondre à chacune de ces questions dans la cellule de texte ci-dessous (n'oubliez pas de l'exécuter avant de saubegarder) : elles me permettent d'ajuster le cours en
fonction de vos besoins, avec un peu de chance, elles devraient également vous aider à guider votre
travail et à apprécier votre progression.







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
