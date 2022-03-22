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
Cours 8 : Corrections
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-03-22
<!-- #endregion -->

## `zip`

> Est-ce que vous voyez comment simuler `enumerate` en utilisant `zip` ?

Avec `zip` et `range`

```python
l = ["spam", "sausages", "eggs", "ham", "spam"]
for idx, elem in zip(l, range(len(l))):
    print("L'élément en position", idx, "est", elem)
```

## Étude de cas : les codes ISO 639

<!-- TODO: commencer plutôt par un Dict[str, str] et passer aux listes dans un second temps -->

Voici un dictionnaire qui contient une liste de quelques langues indexées par leur code [ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

```python
iso_639 = {
    "ny": ["Chichewa", "Chewa", "Nyanja"], 
    "zh": ["Chinese"], 
    "cs": ["Czech"], 
    "da": ["Danish"], 
    "dv": ["Divehi", "Maldivian"],
}
```

### Accéder aux éléments

On peut accéder aux listes de langues en utilisant leur clé

```python
print("La valeur de 'ny' est", iso_639["ny"])
print("La valeur de 'da' est", iso_639["da"])
```

> **Question** En utilisant ce dictionnaire, modifier la cellule suivante pour afficher la chaîne
> `"Chewa"`

```python
print(iso_639["ny"][1])
```

### Parcourir un dictionnaire

Les dictionnaires sont des **itérables**, et on peut les parcourir dans une boucle `for`.

```python
for language in iso_639:
    print(language)
```

**Attention** : ce sont les **clés** qu'on parcourt

### Entraînement

> Modifier la boucle `for` ci-dessous pour qu'elle affiche la sortie suivante :
>
> ```text
> ny -> ['Chichewa', 'Chewa', 'Nyanja']
> zh -> ['Chinese']
> cs -> ['Czech']
> da -> ['Danish']
> dv -> ['Divehi', 'Maldivian']
> ru -> ['Russian']
> ```

```python
# Coder ici
for language in iso_639:
    print(language, "->", iso_639[language])
```

## Exercices

### Présence et absence

> Voici deux listes.

```python
text = ['a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', 
        'fruit', 'picking', 'there', 'try', 'little', 'around', 'appearances', 'appeared', 'all', 
        'crossed', 'basis', 'improbability', 'their', 'discworld', 'black', 'to', 'death', 'future', 
        'only', 'my', 'robe', 'things', 'for', 'it', 'existed', 'said', 'sake', 'sometimes', 'right', 
        'way', 'that', 'country', 'chessboard', 'quoth', 'well', 'domestic', 'skull', 'wonderful', 
        'hooded', 'or', 'empty', 'bottom', 'mirror', 'himself', 'rather', 'over', 'every', 'triangle', 
        'roses', 'border', 'orbiting', 'was', 'from', 'show', 'be', 'pecked', 'bones', 'just', 'universe', 
        'me', 'triangular', 'gets', 'worth', 'have', 'climbed', 'service', 'fluttered', 'top', 'but', 
        'grey', 'claws', 'at', 'rats', 'creep', 'own', 'pattern', 'point', 'white', 'than', 'dark', 
        'therefore', 'frame', 'this', 'not', 'the', 'could', 'mind', 'turtle', 'scrabble', 'better', 
        'industries', 'looked', 'an', 'cherubs', 'life', 'anything', 'more', 'small', 'and', 'of', 'his', 
        'on', 'skulls', 'elephants', 'in', 'thoughts', 'seen', 'nearest', 'expectantly', 'other', 'side', 
        'shape', 'total', 'so', 'world', 'look', 'sun']

words = ["shape", "linguistics", "every", "even", "world", "chessboard", "water", "sake"]
```

> Créer un dictionnaire dont les clés sont les mots de la liste `words` et les valeurs associées
> sont `True` si le mot est dans `text` et `False` sinon. Vous devriez obtenir quelque chose comme
> 
> ```text
> {'shape': True, 'linguistics': False, 'every': True, 'even': False, 'world': True, 
> 'chessboard': True, 'water': False, 'sake': True}
> ```

```python
res = dict()
for w in words:
    if w in text:
        res[w] = True
    else:
        res[w] = False
```

Ou en plus synthétique

```python
res = dict()
for w in words:
    res[w] = w in words
```

## Encore des bigrammes

> Voici un texte

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

> 1\. Écrire un programme qui génère la liste `unique_words`, qui contient tous les mots du texte,
> sans doublons, et en minuscules. Le résultat devrait être le suivant (l'ordre peut être
> différent) :
>
> ```python
> ['a', 'infinity', 'reflection', 'with', 'like', 'big', 'briefly', 'into', 'children', 'which', > 'fruit', 'picking', 'there', 'try', 'little', 'around', 'appearances', 'appeared', 'all', 'crossed', > 'basis', 'improbability', 'their', 'discworld', 'black', 'to', 'death', 'future', 'only', 'my', > 'robe', 'things', 'for', 'it', 'existed', 'said', 'sake', 'sometimes', 'right', 'way', 'that', > 'country', 'chessboard', 'quoth', 'well', 'domestic', 'skull', 'wonderful', 'hooded', 'or', 'empty', > 'bottom', 'mirror', 'himself', 'rather', 'over', 'every', 'triangle', 'roses', 'border', 'orbiting', > 'was', 'from', 'show', 'be', 'pecked', 'bones', 'just', 'universe', 'me', 'triangular', 'gets', > 'worth', 'have', 'climbed', 'service', 'fluttered', 'top', 'but', 'grey', 'claws', 'at', 'rats', > 'creep', 'own', 'pattern', 'point', 'white', 'than', 'dark', 'therefore', 'frame', 'this', 'not', > 'the', 'could', 'mind', 'turtle', 'scrabble', 'better', 'industries', 'looked', 'an', 'cherubs', > 'life', 'anything', 'more', 'small', 'and', 'of', 'his', 'on', 'skulls', 'elephants', 'in', > 'thoughts', 'seen', 'nearest', 'expectantly', 'other', 'side', 'shape', 'total', 'so', 'world', > 'look', 'sun']
> ```
>
> (évidemment ne faites pas juste un copier-coller)


```python
unique_words = []
for word in text.split():
    word_low = word.lower()
    if word_low not in res:
        unique_words.append(word_low)
print(unique_words)
```

> 2\. Écrire un programme qui extrait à partir de la liste `unique_words` la liste
> `attested_bigrams` des bigrammes de caractères qui apparaissent dans le texte.
>
> **Indice** On a déjà écrit du code pour extraire des bigrammes dans une séance précédente.

En utilisant le code des exercices de la séance 76

```python
attested_bigrams = []
for mot in unique_words:
    for i in range(len(mot)-1):
        b = mot[i:i+2]
        if b not in attested_bigrams:
            attested_bigrams.append(b)
print(attested_bigrams)
print(len(attested_bigrams))
```

> 3\. Voici une liste des lettres de l'alphabet anglais. Utilisez-la pour générer une liste
> `possible_bigrams` de tous les bigrammes de caractères théoriquement possibles en anglais.

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

```python
possible_bigrams = []
for c1 in alphabet:
    for c2 in alphabet:
        possible_bigrams.append(c1+c2)
print(possible_bigrams)
print(len(possible_bigrams))
```

> 4\. Écrire un programme qui génère la liste `unattested_bigrams` des bigrammes de caractères
> non attestés, c'est-à-dire de tous les bigrammes qui sont possibles, mais qu'on ne trouve pas dans
> ce texte.

```python
unattested_bigrams = []
for possible in possible_bigrams:
    if possible not in attested_bigrams:
        unattested_bigrams.append(possible)
print(unattested_bigrams)
print(len(unattested_bigrams))
```
