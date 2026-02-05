---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 3 : Solutions
=========================================

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

## 🔭 Entraînement 🔭

> Demandez un mot et un indice `i` à l'utilisateurice. Si le mot a un `i`-ème caractère, affichez ce
> caractère, sinon affichez un message d'erreur.
>
> **Indice** : vous savez déterminer la longueur d'une chaîne de caractères.


```python tags=["skip-execution"]
mot = input("Dis-moi un mot : ")
position = int(input("Dis-moi un nombre : "))

if position >= len(mot) or position < 0:
    print("Indice", position, "incorrect pour un mot de longueur", len(mot))
else:
    print(mot[position])
```

## 🛠️ Entraînement 🛠️

> Voici une liste de lettres :

```python
letters = ["d", "b", "c", "n"]
```

> Insérez `"x"` en position `3`, puis retirez `"c"`, ajoutez `"e"` à la fin, supprimez l'élément
> d'indice `2`, et, finalement remplacez l'élément en position `1` par `"o"`. Puis affichez le
> contenu de la liste

```python
letters = ["d", "b", "c", "n"]
letters.insert(3, "x")
print(letters)
letters.remove("c")
print(letters)
letters.append("e")
print(letters)
letters.pop(2)
print(letters)
letters[1] = "o"
print(letters)
```

## Exercices

## Exercice 1

> Voici deux listes

```python
cities = ["NYC", "LA", "SF"]
small_cities = ["Stony Brook", "Provo"]

# Codez ici
```

> Modifiez la cellule de sorte à modifier `cities` pour que son contenu soit `["NYC", "LA",
> "Stony Brook", "Provo", "SF"]`

```python
cities = ["NYC", "LA", "SF"]
small_cities = ["Stony Brook", "Provo"]

cities.pop()
cities.extend(small_cities)
cities.append("SF")
print(cities)
```

Il y a beaucoup d'autres solutions, par exemple :

```python
cities = ["NYC", "LA", "SF"]
small_cities = ["Stony Brook", "Provo"]

cities.insert(2, "Stony Brook")
cities.insert(3, "Provo")
print(cities)
```

Y compris des trop sophistiquées :

```python
cities = ["NYC", "LA", "SF"]
small_cities = ["Stony Brook", "Provo"]

for s in small_cities[::-1]:
    cities.insert(2, s)

print(cities)
```

## Exercice 2

> Voici une liste

```python
villes = ["Paris", "Nanterre", "Orléans", "Uppsala"]
```

> En utilisant cette liste, écrivez un programme qui affiche la sortie suivante
>
> ```text
> Paris Paris
> Paris Nanterre
> Paris Orléans
> Paris Uppsala
> Nanterre Paris
> Nanterre Nanterre
> Nanterre Orléans
> Nanterre Uppsala
> Orléans Paris
> Orléans Nanterre
> Orléans Orléans
> Orléans Uppsala
> Uppsala Paris
> Uppsala Nanterre
> Uppsala Orléans
> Uppsala Uppsala
> ```

```python
for v in villes:
    for w in villes:
        print(v, w)
```

### Exercice 3

> Voici quelques mots de la [Liste Swadesh](https://fr.wikipedia.org/wiki/Liste_Swadesh).

```python
words = ["soleil", "lune", "terre", "eau", "nouriture", "ciel"]
```

> Imaginez que vous êtes un⋅e linguiste de terrain en train de collecter du vocabulaire pour
> documenter une langue :
> 
> - Créez une liste vide dans une variable `traduction`.
> - Pour chacun des mots de la liste `words`, demandez à l'utilisateurice d'entrer sa traduction et
>   sauvegardez cette entrée dans `traductions`.
> - Une fois que vous avez terminé, affichez la valeur de `traductions`.

```python tags=["skip-execution"]
traductions = []
for mot in words:
    trad = input(f"Traduction de {mot}: ")
    traductions.append(trad)
print(traductions)
```

## Retours sur vos rendus

En général :

- Plus de rendus cette fois, c'est bien !
- La séance de la semaine dernière était dense, mais vous vous en sortez plutôt bien.
  - Beaucoup de réponses créatives pour l'exercice 2 en particulier, ce qui est une **bonne** chose.
- Plusieurs demandes de plus d'exos : c'est le programme pour cette semaine et je mettrai plus
  d'exos d'application directe dans les prochaines séances.

Exercice 1 :

- Attention à la différence entre ces listes :

```python
['NYC', 'LA', ['Stony Brook', 'Provo'], 'SF'] != ['NYC', 'LA', 'Stony Brook', 'Provo', 'SF']
```

  Ici, c'est la deuxième qu'il fallait obtenir.

Exercice 2 :

- Rappelez-vous qu'on peut imbriquer des boucles.

Exercice 3 :

- Oui, on peut mettre un `input` dans une boucle :-)
