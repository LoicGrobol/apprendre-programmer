---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.8
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 11 : TD récapitulatif 2
============================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-04-12
<!-- #endregion -->

Dans ce notebook

- Des exercices.
- Encore des exercices.
- Toujours des exercices.
- Basiquement la suite du [premier récapitulatif](../06-recapitulatif/recapitulatif.py.md)

Il y a des rappels pour chacune des notions, mais n'hésitez pas à aller relire les cours précédents
et les corrections des exercices.

**Si vous révisez en autonomie : commencez par refaire [le premier
récapitulatif](../06-recapitulatif/recapitulatif.py.md) et à revoir [sa
correction](../06-recapitulatif/corrections.py.md).** En particulier sa section « utiliser un
notebook » si vous avez des doutes.

## Compteurs et accumulateurs

> Les **compteurs**, et plus largement les **accumulateurs** sont des recettes très fréquemment
> utilisées en lien avec les boucles.
>
> Le plan est le suivant : on initialise une variable à une valeur de base, puis on parcourt un
> itérable, en mettant à jour la variable en question à chaque itération. Pour un compteur, il
> s'agit de… compter des éléments ou des occurrences.
>
> Voici la version la plus simple d'un compteur : ici la variable `compte` va nous servir à compter
> tous les éléments de la liste `spam`.

```python
spam = [4, "n", 7, 1, "f", 4]
compte = 0
for elem in spam:
    compte = compte + 1
print("Il y a", compte, "éléments dans spam.")
```

> En pratique, on ne compte en général pas tous les éléments, mais seulement ceux qui vérifient une
> certaine condition : ici les chaînes de plus de quatre caractères :

```python
spam = ["manger", "et", "dormir", "c'", "essentiel"]
compte = 0
for elem in spam:
    if len(elem) > 4:
       compte = compte + 1
print(compte)
```

> Les accumulateurs sont une version plus générale où on fait autre chose qu'ajouter $1$
> (*incrémenter*) à la variable. Par exemple ici, on stocke dans `acc` la somme des longueurs des
> mots de la liste :

```python
spam = ["manger", "et", "dormir", "c'", "essentiel"]
acc = 0
for elem in spam:
    acc = acc + len(elem)
print(acc)
```

> Un accumulateur n'est pas nécessairement un nombre : ici par exemple, c'est une liste

```python
spam = ["manger", "et", "dormir", "c'", "essentiel"]
longs_mots = []
for elem in spam:
    if len(elem) > 4:
       longs_mots.append(elem)
print(longs_mots)
```

1\.

1.1 Écrire un programme qui compte le nombre de mots de moins de $4$ lettres dans la liste suivante,
puis affiche ce nombre

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

# Coder ici
```

1.2 Même question pour les mots de plus de $6$ lettres

```python
paragraphe = ["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']

# Coder ici
```

2\. Écrire un programme qui compte le nombre de températures supérieures à $50$ dans la liste
`temperatures`, puis affiche ce nombre.

```python
temperatures = [62.8, 26.6, 60.3, 60.4, 59.4, 45.1, 49, 55.3, 70.7, 63.5,
                70, 44.4, 51.8, 51.7, 47.8, 54.3, 55.6, 66.4, 41, 54.2, 
                47.9, 44.4, 41.2, 63.4, 54.5, 42.7, 48.8, 49.9, 43.8, 52.7, 
                53.4, 45.4, 59, 40.4, 50.7, 59.6, 48.4, 48.8, 50.1, 62.4, 
                45.2, 57.6, 64.8, 48.6, 42.9, 55.1, 48.3, 51.8, 43.1, 42]
# Coder ici
```

3\. Écrire un programme qui compte le nombre de mots commençant par une voyelle dans le paragraphe
suivant, puis affiche ce nombre.

```python
["c'", 'est', 'devenu', 'une', 'banalité', "l'", 'ordinateur', "s'", 'accapare', 'nos', 'bureaux', 'modifie', 'nos', 'modes', 'de', 'travail', 'envahit', 'nos', 'maisons', "s'", 'intègre', 'dans', 'les', 'objets', 'les', 'plus', 'quotidiens', 'et', 'nous', 'propose', 'des', 'loisirs', 'inédits', 'il', 'est', 'même', 'à', "l'", 'origine', 'de', 'nouveaux', 'modes', 'de', 'sociabilité', 'et', "d'", 'une', 'nouvelle', 'économie', "l'", 'informatique', 'est', 'partout', 'pourtant', "l'", 'ordinateur', 'lui', 'même', 'demeure', 'pour', 'beaucoup', 'une', 'énigme', 'un', 'objet', 'mystérieux', 'et', 'un', 'peu', 'magique']
voyelles = ["a","e","o","i","u", "y", "à", "â", "é", "è", "ê", "ë", "î", "ï", "ô", "ù", "ü", "ÿ"]
# Coder ici
```
