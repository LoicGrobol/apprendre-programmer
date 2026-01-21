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
Cours 7 : Corrections
======================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-03-15
<!-- #endregion -->

## Entraînement : compteurs et accumulateurs

### 1. Compter les *stop words*

Voici un paragraphe, segmenté en mots :

```python
paragraphe = ["C'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'Il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'Pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique', 'Le', 'terme', "d'", 'informaticien', 'semble', "d'", 'ailleurs', 'recouper', 'une', 'grande', 'diversité', 'de', 'métiers', 'et', "d'", 'occupations', 'réelles', 'allant', 'du', 'technicien', 'à', "l'", 'ingénieur', 'réseau', 'en', 'passant', 'par', 'le', 'webmaître', 'Quant', 'à', 'la', 'nature', 'du', 'travail', 'de', 'ceux', 'qui', 'font', 'de', 'la', 'recherche', 'en', 'informatique', "c'", 'est', 'sans', 'doute', 'à', 'en', 'juger', 'par', 'les', 'réactions', 'auxquelles', "j'", 'ai', 'moi', 'même', 'été', 'confrontée', 'une', 'mystère', 'encore', 'plus', 'épais', 'malgré', 'le', 'prestige', 'un', 'peu', 'mythique', 'que', 'conservent', 'des', 'projets', 'comme', 'ceux', 'de', 'la', 'robotique', 'ou', 'de', "l'", 'intelligence', 'artificielle', 'Ce', 'document', 'se', 'veut', 'en', 'partie', 'une', 'réponse', 'à', 'ceux', 'qui', 'se', 'demandent', 'quels', 'sont', 'les', 'fondements', 'de', "l'", 'informatique', 'Il', "n'", 'est', 'pas', 'conçu', 'pour', 'initier', 'au', 'maniement', 'pratique', 'des', 'ordinateurs', 'ce', "n'", 'est', 'pas', 'une', 'introduction', 'à', 'la', 'bureautique', 'Ce', "n'", 'est', 'pas', 'non', 'plus', 'un', 'manuel', 'technique', 'à', "l'", 'usage', 'de', 'ceux', 'qui', 'souhaitent', 'bricoler', 'leur', 'machine', 'favorite', 'Si', 'au', 'fil', 'des', 'pages', 'des', 'informations', 'utiles', 'à', 'ces', 'deux', 'catégories', "d'", 'utilisateurs', 'ou', 'aux', 'novices', 'pourront', 'être', 'glanées', 'vocabulaire', 'spécialisé', 'typologie', 'de', 'matériels', 'ordre', 'de', 'grandeurs', 'des', 'performances', 'des', 'machines', 'actuelles', 'tel', "n'", 'est', 'pas', 'son', 'objectif', 'premier', "L'", 'informatique', 'dont', 'il', 'sera', 'question', 'ici', 'est', 'une', 'discipline', 'scientifique', 'qui', 'en', 'tant', 'que', 'telle', 'a', 'ses', 'propres', 'questions', 'ses', 'propres', 'problèmes', 'et', 'dispose', 'pour', 'les', 'aborder', "d'", 'outils', 'et', 'de', 'méthodes', 'spécifiques', 'De', 'cette', 'discipline', 'on', 'abordera', 'les', 'fondements', 'théoriques', 'ainsi', 'que', 'quelques', 'réalisations', 'pratiques', 'mais', 'on', 'insistera', 'plus', 'sur', 'les', 'concepts', 'que', 'sur', 'la', 'technique', 'Cette', 'présentation', 'relève', 'donc', 'principalement', "d'", 'une', 'démarche', 'de', 'vulgarisation', 'scientifique', 'destinée', 'à', 'un', 'public', 'de', 'non', 'spécialistes', 'mais', 'qui', 'se', 'place', 'à', 'un', 'niveau', 'non', 'trivial', 'difficilement', 'trouvable', 'dans', 'les', 'manuels', 'habituellement', 'disponibles', "J'", 'ai', 'ici', 'essayé', 'de', 'décrire', 'de', 'façon', 'aussi', 'abordable', 'que', 'possible', 'ce', 'que', 'en', 'tant', "qu'", 'informaticienne', 'je', 'souhaite', 'que', "l'", 'honnête', 'homme', 'du', 'XXIème', 'siècle', 'sache', 'et', 'pense', 'de', 'ma', 'discipline', 'appelée', 'à', 'coup', 'sûr', 'à', 'un', 'grand', 'développement', 'dans', 'les', 'années', 'qui', 'viennent']
```

À l'aide d'une boucle et d'un compteur, déterminer le nombre de mots de ce paragraphe qui
appartiennent à la liste `stop_words` suivante.

```python
stop_words = ["le", "la", "les", "l'", "un", "une", "des", "de", "d'", "à"]
compte = 0
for mot in paragraphe:
    if mot in stop_words:
        compte = compte + 1
print("Il y a", compte, "mots vides dans ce paragraphe")
```

### 2. Accumulateurs

Voici une liste de nombres

```python
numb3rs = [2, 3, 6, 3, 8, 2, 10, 2, 8, 3, 7, 7, 3, 5, 2, 7, 7, 3, 7, 2, 7, 4, 3, 6, 3, 4, 10, 2, 4, 7, 3, 7, 7, 2, 3, 4, 1, 2, 7, 2, 8, 5, 2, 11, 2, 2, 3, 8, 8, 2, 12, 3, 7, 8, 2, 10, 3, 4, 7, 4, 8, 3, 6, 2, 5, 10, 2, 2, 3, 7, 2, 5, 2, 13, 6, 2, 8, 8, 3, 6, 9, 2, 7, 2, 2, 11, 7, 6, 2, 10, 1, 2, 9, 6, 2, 7, 3, 2, 9, 5, 1, 2, 6, 2, 7, 2, 4, 3, 4, 2, 2, 9, 2, 12, 2, 3, 4, 5, 1, 2, 5, 3, 3, 9, 10, 2, 2, 3, 4, 3, 10, 3, 7, 6, 4, 5, 6, 2, 8, 2, 3, 8, 3, 10, 3, 7, 5, 4, 2, 2, 9, 2, 2, 2, 12, 12, 2, 8, 2, 4, 2, 6, 3, 7, 1, 4, 3, 2, 9, 5, 4, 3, 10, 2, 2, 12, 2, 2, 3, 3, 5, 4, 7, 2, 9, 8, 3, 11, 2, 2, 3, 3, 3, 12, 1, 2, 11, 2, 2, 3, 3, 3, 4, 2, 6, 9, 1, 2, 5, 2, 4, 3, 10, 8, 4, 7, 8, 2, 2, 3, 3, 5, 3, 12, 6, 1, 3, 4, 10, 2, 12, 2, 3, 7, 8, 4, 7, 11, 10, 9, 2, 9, 5, 2, 9, 3, 12, 3, 8, 9, 3, 2, 3, 3, 3, 8, 7, 2, 12, 4, 2, 4, 8, 3, 3, 3, 10, 12, 3, 2, 4, 3, 5, 1, 3, 7, 9, 3, 7, 9, 2, 7, 4, 3, 7, 2, 6, 2, 2, 8, 11, 2, 5, 10, 2, 8, 3, 10, 10, 5, 3, 8, 12, 9, 4, 2, 9, 4, 3, 3, 8, 3, 3, 2, 9, 5, 12, 6, 4, 14, 2, 3, 8, 2, 13, 12, 8, 1, 2, 6, 2, 3, 12, 4, 3, 2, 5, 1, 2, 6, 3, 7, 13, 9, 4, 3, 7, 14, 11, 2, 2, 3, 6, 2, 7, 2, 5, 5, 9, 3, 8, 2, 3, 2, 4, 3, 15, 2, 8, 3, 2, 7, 5, 2, 6, 6, 5, 2, 5, 2, 2, 10, 7, 1, 4, 3, 1, 2, 5, 13, 4, 3, 6, 3, 8]
```

À l'aide d'une boucle, calculer et afficher leur somme et leur moyenne

```python
somme = 0
for nombre in numb3rs:
    somme = somme + nombre
print(somme)
print(somme/len(numb3rs))
```

### 3. Max

Voici la même liste de nombres

```python
numb3rs = [2, 3, 6, 3, 8, 2, 10, 2, 8, 3, 7, 7, 3, 5, 2, 7, 7, 3, 7, 2, 7, 4, 3, 6, 3, 4, 10, 2, 4, 7, 3, 7, 7, 2, 3, 4, 1, 2, 7, 2, 8, 5, 2, 11, 2, 2, 3, 8, 8, 2, 12, 3, 7, 8, 2, 10, 3, 4, 7, 4, 8, 3, 6, 2, 5, 10, 2, 2, 3, 7, 2, 5, 2, 13, 6, 2, 8, 8, 3, 6, 9, 2, 7, 2, 2, 11, 7, 6, 2, 10, 1, 2, 9, 6, 2, 7, 3, 2, 9, 5, 1, 2, 6, 2, 7, 2, 4, 3, 4, 2, 2, 9, 2, 12, 2, 3, 4, 5, 1, 2, 5, 3, 3, 9, 10, 2, 2, 3, 4, 3, 10, 3, 7, 6, 4, 5, 6, 2, 8, 2, 3, 8, 3, 10, 3, 7, 5, 4, 2, 2, 9, 2, 2, 2, 12, 12, 2, 8, 2, 4, 2, 6, 3, 7, 1, 4, 3, 2, 9, 5, 4, 3, 10, 2, 2, 12, 2, 2, 3, 3, 5, 4, 7, 2, 9, 8, 3, 11, 2, 2, 3, 3, 3, 12, 1, 2, 11, 2, 2, 3, 3, 3, 4, 2, 6, 9, 1, 2, 5, 2, 4, 3, 10, 8, 4, 7, 8, 2, 2, 3, 3, 5, 3, 12, 6, 1, 3, 4, 10, 2, 12, 2, 3, 7, 8, 4, 7, 11, 10, 9, 2, 9, 5, 2, 9, 3, 12, 3, 8, 9, 3, 2, 3, 3, 3, 8, 7, 2, 12, 4, 2, 4, 8, 3, 3, 3, 10, 12, 3, 2, 4, 3, 5, 1, 3, 7, 9, 3, 7, 9, 2, 7, 4, 3, 7, 2, 6, 2, 2, 8, 11, 2, 5, 10, 2, 8, 3, 10, 10, 5, 3, 8, 12, 9, 4, 2, 9, 4, 3, 3, 8, 3, 3, 2, 9, 5, 12, 6, 4, 14, 2, 3, 8, 2, 13, 12, 8, 1, 2, 6, 2, 3, 12, 4, 3, 2, 5, 1, 2, 6, 3, 7, 13, 9, 4, 3, 7, 14, 11, 2, 2, 3, 6, 2, 7, 2, 5, 5, 9, 3, 8, 2, 3, 2, 4, 3, 15, 2, 8, 3, 2, 7, 5, 2, 6, 6, 5, 2, 5, 2, 2, 10, 7, 1, 4, 3, 1, 2, 5, 13, 4, 3, 6, 3, 8]
```

À l'aide d'une boucle, déterminer le nombre le plus grand (le maximum) de cette liste

```python
maximum = numb3rs[0]
for nombre in numb3rs:
    if nombre > maximum:
        maximum = nombre
print(maximum)
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

- La fonction `max` renvoie le plus grand élément d'un itérable.
- La fonction `max` renvoie le plus petit élément d'un itérable.
- La fonction `sum` renvoie la somme des éléments d'un itérable.

#### 5. Min

> Voici une liste de noms

```python
names = ['Nicole-Reine Lepaute', 'Ada Lovelace', 'Maria Mitchell', 'Anna Winlock', 'Henrietta Swan Leavitt', 'Beatrice Mabel Cave-Browne-Cave', 'Mary Clem', 'Edith Clarke', 'Grete Hermann', 'Johanna Piesch', 'Mavis Batey', 'Gertrude Blanch', 'Ruth Leach Amonette', 'Marlyn Meltzer', 'Jean Bartik', 'Irma Wyman', 'Kathleen Booth', 'Dorothy Vaughan', 'Grace Hopper', 'Evelyn Boyd Granville', 'Ida Rhodes', 'Kathleen Booth', 'Betty Holberton', 'Klára Dán von Neumann', 'Thelma Estrin', 'Annie Easley', 'Kateryna Iouchtchenko', 'Marguerite Frank', 'Grace Hopper', 'Kathleen Booth', 'Alice Recoque', 'Mary K. Hawes', 'Marion Créhange', 'Jean E. Sammet', 'Stephanie Shirley', 'Joan Ball', 'Sharla Boehm', 'Mary Allen Wilkes', 'Mary Kenneth Keller', 'Vera Molnár', 'Jean E. Sammet', 'Margaret Hamilton', 'Alexandra Illmer Forsythe', 'Drude Berntsen', 'Erna Schneider Hoover', 'Adele Goldberg', 'Karen Spärck Jones', 'Susan Nycum', 'Phyllis Fox', 'Elizabeth J. Feinler', 'Rózsa Péter', 'Carol Shaw', 'Sophie Wilson', 'Christiane Floyd', 'Lynn Conway', 'Carol Shaw', 'Ruzena Bajcsy', 'Ruth M. Davis', 'Roberta Williams', 'Lorinda Cherry', 'Roberta Williams', 'Susan Kare', 'Radia Perlman', 'Irma Wyman', 'Nancy Hafkin', 'Monica S. Lam', 'Anita Borg', 'Joëlle Coutaz', 'Rena Tangens', 'Éva Tardos', 'Frances Allen', 'Frances Brazier', 'Ruzena Bajcsy', 'Carol Bartz', 'Shafi Goldwasser', 'Barbara Liskov', 'Carolyn Gruyer', 'Mary Lou Jepsen', 'Xiaoyuan Tu', 'Anita Borg', 'Chieko Asakawa', 'Manuela M. Veloso', 'Meg Whitman', 'Marissa Mayer', 'Carly Fiorina', 'Sun Yafang', 'Noriko H. Arai', 'Ellen Spertus', 'Margaret Hamilton', 'Susan Elizabeth Black', 'Jeri Ellsworth', 'Safra Catz', 'Audrey Tang', 'Mary Lou Jepsen', 'Facebook', 'Xiaoyun Wang', 'Maria Klawe', 'Joanna Rutkowska', 'Frances Allen', 'Anne-Marie Kermarrec', 'Barbara Liskov', 'Carol Bartz', 'Farida Bedwei', 'Meg Whitman', 'Noriko H. Arai', 'Shikoh Gitau', 'Shafi Goldwasser', 'Ginni Rometty', 'Éva Tardos', 'Regina Honu', 'Christine Paulin-Mohring', 'Coraline Ada Ehmke', 'Kesha Shah', 'Audrey Tang', 'Kate Devlin', 'Michelle Simmons', 'Regina Honu', 'Gladys West']
```

> 1\. À l'aide d'une boucle, déterminer la longueur du nom le plus court de cette liste

```python
plus_court = len(names[0])
for nom in names:
    if len(nom) < plus_court:
        plus_court = len(nom)
print(plus_court)
```

> 2\. À l'aide d'une boucle, déterminer le nom le plus court de cette liste

```python
plus_court = names[0]
for nom in names:
    if len(nom) < len(plus_court):
        plus_court = nom
print(plus_court)
```

## Exercices

### Consonnes

> Voici une liste de voyelles

```python
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]
```

> Écrire un programme qui demande la saisie d'un mot et affiche le nombre de consonnes (donc de
> lettre qui ne sont pas de voyelles) dans ce mot.

```python tags=["skip-execution"]
mot = input("Dis-moi un mot: ")
nombre_consonnes = 0
for caractere in mot:
    if caractere not in voyelles:
        nombre_consonnes = nombre_consonnes + 1
print("Il y a", nombre_consonnes, "consonnes dans ton mot !")
```

### 🍄 Accumuler dans une liste 🍄

> Écrire un programme qui demande à l'utilisateurice de saisir les uns après les autres ses cinq
> aliments préférés. Stocker ces réponses dans une liste, puis affichez les éléments de cette liste,
> chacun sur une ligne.

```python tags=["skip-execution"]
pref = []
for _ in range(5):
    m = input("Dis-moi un de tes aliments préférés: ")
    pref.append(m)

for aliment in pref:
    print(aliment)
```

### ⚒️ N-grammes ⚒️

> Le concept de **n-gramme** est fondamental en TAL. Un n-gramme, c'est une suite de $n$ symboles.
> Par exemple dans le mot « banane », les 2-grammes (bigrammes) de caractères sont :
>
> - ba
> - an
> - na
> - ne
>
> Et dans le mot « linguiste », les 3-grammes (trigrammes) de caractères sont :
>
> - lin
> - ing
> - ngu
> - gui
> - uis
> - ist
> - ste
>
> 1\. Écrire un programme qui demande la saisie d'un mot et affiche tous les bigrammes de caractères
> de ce mot. Il vous faudra utiliser une boucle `for`, et probablement des outils parmi ceux qu'on a
> vu dans cette séance.

```python tags=["skip-execution"]
mot = input("Saisir un mot : ")
bigrams = []
for i in range(len(mot)-1):
    b = mot[i:i+2]
    if b not in bigrams:
        bigrams.append(b)
print(bigrams)
```

2\. Écrire un programme qui demande la saisie d'un mot et d'un entier `n`, puis affiche la liste des
n-grammes de caractères de ce mot.

Indices :

- Attention aux cas particuliers : que faire des `n` premiers et derniers caractères du mot ? Que
  faire si le mot fait moins de n caractères…

```python tags=["skip-execution"]
mot = input("Saisir un mot : ")
n = int(input("Saisir n : "))
ngrams = []
for i in range(len(mot)-n+1):
    g = mot[i:i+n+1]
    if g not in ngrams:
        ngrams.append(g)
print(ngrams)
```
