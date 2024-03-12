---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.4
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
<!-- #endregion -->

Dans ce notebook, des nouveaux outils pour travailler avec les boucles : les compteurs, les
accumulateurs et la fonction `range`.

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

#### 1. Compter les *stop words*

Voici un paragraphe, segmenté en mots :

```python
paragraphe = ["C'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'Il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'Pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique', 'Le', 'terme', "d'", 'informaticien', 'semble', "d'", 'ailleurs', 'recouper', 'une', 'grande', 'diversité', 'de', 'métiers', 'et', "d'", 'occupations', 'réelles', 'allant', 'du', 'technicien', 'à', "l'", 'ingénieur', 'réseau', 'en', 'passant', 'par', 'le', 'webmaître', 'Quant', 'à', 'la', 'nature', 'du', 'travail', 'de', 'ceux', 'qui', 'font', 'de', 'la', 'recherche', 'en', 'informatique', "c'", 'est', 'sans', 'doute', 'à', 'en', 'juger', 'par', 'les', 'réactions', 'auxquelles', "j'", 'ai', 'moi', 'même', 'été', 'confrontée', 'une', 'mystère', 'encore', 'plus', 'épais', 'malgré', 'le', 'prestige', 'un', 'peu', 'mythique', 'que', 'conservent', 'des', 'projets', 'comme', 'ceux', 'de', 'la', 'robotique', 'ou', 'de', "l'", 'intelligence', 'artificielle', 'Ce', 'document', 'se', 'veut', 'en', 'partie', 'une', 'réponse', 'à', 'ceux', 'qui', 'se', 'demandent', 'quels', 'sont', 'les', 'fondements', 'de', "l'", 'informatique', 'Il', "n'", 'est', 'pas', 'conçu', 'pour', 'initier', 'au', 'maniement', 'pratique', 'des', 'ordinateurs', 'ce', "n'", 'est', 'pas', 'une', 'introduction', 'à', 'la', 'bureautique', 'Ce', "n'", 'est', 'pas', 'non', 'plus', 'un', 'manuel', 'technique', 'à', "l'", 'usage', 'de', 'ceux', 'qui', 'souhaitent', 'bricoler', 'leur', 'machine', 'favorite', 'Si', 'au', 'fil', 'des', 'pages', 'des', 'informations', 'utiles', 'à', 'ces', 'deux', 'catégories', "d'", 'utilisateurs', 'ou', 'aux', 'novices', 'pourront', 'être', 'glanées', 'vocabulaire', 'spécialisé', 'typologie', 'de', 'matériels', 'ordre', 'de', 'grandeurs', 'des', 'performances', 'des', 'machines', 'actuelles', 'tel', "n'", 'est', 'pas', 'son', 'objectif', 'premier', "L'", 'informatique', 'dont', 'il', 'sera', 'question', 'ici', 'est', 'une', 'discipline', 'scientifique', 'qui', 'en', 'tant', 'que', 'telle', 'a', 'ses', 'propres', 'questions', 'ses', 'propres', 'problèmes', 'et', 'dispose', 'pour', 'les', 'aborder', "d'", 'outils', 'et', 'de', 'méthodes', 'spécifiques', 'De', 'cette', 'discipline', 'on', 'abordera', 'les', 'fondements', 'théoriques', 'ainsi', 'que', 'quelques', 'réalisations', 'pratiques', 'mais', 'on', 'insistera', 'plus', 'sur', 'les', 'concepts', 'que', 'sur', 'la', 'technique', 'Cette', 'présentation', 'relève', 'donc', 'principalement', "d'", 'une', 'démarche', 'de', 'vulgarisation', 'scientifique', 'destinée', 'à', 'un', 'public', 'de', 'non', 'spécialistes', 'mais', 'qui', 'se', 'place', 'à', 'un', 'niveau', 'non', 'trivial', 'difficilement', 'trouvable', 'dans', 'les', 'manuels', 'habituellement', 'disponibles', "J'", 'ai', 'ici', 'essayé', 'de', 'décrire', 'de', 'façon', 'aussi', 'abordable', 'que', 'possible', 'ce', 'que', 'en', 'tant', "qu'", 'informaticienne', 'je', 'souhaite', 'que', "l'", 'honnête', 'homme', 'du', 'XXIème', 'siècle', 'sache', 'et', 'pense', 'de', 'ma', 'discipline', 'appelée', 'à', 'coup', 'sûr', 'à', 'un', 'grand', 'développement', 'dans', 'les', 'années', 'qui', 'viennent']
print(" ".join(paragraphe))
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
total = 0
for num in numb3rs:
    total = total + num
print("Somme:", total)
print("Moyenne:", total/len(numb3rs))
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

Les objets de type `range` ne sont donc pas des **séquences**. En revanche on peut itérer dessus, ce sont donc des
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

On peut convertir un `range` en liste en utilisant la fonction `list` :

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
for index in range(len(mot)):
    print(mot[index], " indice :", index)
```

qui est plus compact, et un peu plus agréable (on a plus à gérer manuellement le compteur).

Attention, ce n'est pas optimal et on verra mieux plus tard, mais pour l'instant on va s'en
servir pour s'entraîner à manipuler des `range`.

## Exercices

Répondre à ces exercices directement dans le notebook, le sauvegarder sous un nom de la forme
`07_boucles_sequences_PRENOM_NOM.ipynb` (pour Morgan Lefeuvre par exemple, ce serait
`07_boucles_sequences_Morgan_Lefeuvre.ipynb`) et me le transmettre avant dimanche 2023-02-26 au soir.

- De préférence via [Cours en Ligne](https://coursenligne.parisnanterre.fr/course/view.php?id=7694)
  (clé d'inscription `rossum`)
- À défaut, par mail, à `<lgrobol@parisnanterre.fr>`

Attention : **l'extension doit être `.ipynb`**.

N'hésitez pas à revenir sur les cours et les corrigés précédents pour trouver des idées.

### Consonnes

Voici une liste de voyelles

```python
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]
```

Écrire un programme qui demande la saisie d'un mot et affiche le nombre de consonnes (donc de lettre
qui ne sont pas de voyelles) dans ce mot.

```python

```

### 🍄 Accumuler dans une liste 🍄

Écrire un programme qui demande à l'utilisateurice de saisir les uns après les autres ses cinq
aliments préférés. Stocker ces réponses dans une liste, puis affichez les éléments de cette liste,
chacun sur une ligne.

```python

```

### ⚒️ N-grammes ⚒️

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

1\. Écrire un programme qui demande la saisie d'un mot et affiche tous les bigrammes de caractères
de ce mot. Il vous faudra utiliser une boucle `for`, et probablement des outils parmi ceux qu'on a
vu dans cette séance.

```python

```

2\. Écrire un programme qui demande la saisie d'un mot et d'un entier `n`, puis affiche la liste des
n-grammes de caractères de ce mot.

Indices :

- Attention aux cas particuliers : que faire des `n` premiers et derniers caractères du mot ? Que
  faire si le mot fait moins de n caractères…

```python

```

### Réflexion

Quelques questions sur votre travail :

- Combien de temps avez-vous passé à faire ces exercices ?
- Combien de temps avez-vous passé à relire le cours (ou les cours précédents) ?
- Avez-vous l'impression d'avoir bien mémorisé les concepts et les techniques vus jusqu'ici ?
- Qu'est-ce qui vous paraît le plus compliqué ?
- À votre avis, pourquoi ?

Merci de bien répondre à chacune de ces questions dans la cellule de texte ci-dessous (n'oubliez pas
de l'exécuter avant de sauvegarder) : elles me permettent d'ajuster le cours en fonction de vos
besoins, avec un peu de chance, elles devraient également vous aider à guider votre travail et à
apprécier votre progression.







