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
Cours 1 : corrections
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-01-25
<!-- #endregion -->

## ⬜ Exo ⬜

> Écrire dans la cellule ci-dessous un programme qui affiche votre prénom et votre nom de famille,
> séparés par une ligne vide, comme ceci :
> 
> ```text
> Loïc
> 
> Grobol
> ```

```python
print("Loïc")
print("")
print("Grobol")
```

```python
print("Loïc")
print()
print("Grobol")
```

```python
print("Loïc\n\nGrobol")
```

<!-- #region -->
## 🦾 Exercices 🦾


### Exercice 1

> Étant donné le paragraphe suivant
<!-- #endregion -->

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

> Écrire un programme qui demande à l'utilisateurice de saisir un mot, puis vérifie si ce mot est
> dans le texte.

```python tags=["nbconvert_ignore"]
mot = input("Saisir un mot : ")
print(mot in texte)
```

### Exercice 2

> Écrire un programme qui vérifie si le mot *banane* est contenue dans une entrée récupérée avec
> `input`, en quelle que soit la casse.

```python tags=["nbconvert_ignore"]
texte = input("Saisir un texte : ")
print("banane" in texte.lower())
```

### Exercice 3

> Écrire un programme qui demande à son utilisateurice son année de naissance et affiche l'âge
> qu'aura cette personne en 2022.
>
> Indice : `int`

```python tags=["nbconvert_ignore"]
annee_str = input("Tu es né⋅e quand ? ")
annee_int = int(annee_str)
age_2022 = 2022 - annee_int
print("En 2022 tu auras", age_2022, "ans")
```

ou encore

```python tags=["nbconvert_ignore"]
annee_str = input("Tu es né⋅e quand ? ")
annee_int = int(annee_str)
age_2022 = 2022 - annee_int
print("En 2022 tu auras " + str(age_2022) + " ans")
```

ou mieux

```python tags=["nbconvert_ignore"]
annee_str = input("Tu es né⋅e quand ? ")
annee_int = int(annee_str)
age_2022 = 2022 - annee_int
print(f"En 2022 tu auras {age_2022} ans")
```

### Exercice 4

> Demander à l'utilisateurice d'entrer un nombre minimal de caractères pour qu'un mot soit considéré
> comme long. Puis lui demander de saisir un mot et lui afficher `True` si le mot est long et
> `False` sinon.

```python tags=["nbconvert_ignore"]
long_len = int(input("Long, c'est combien de caractères ? "))
mot = input("Saisir un mot :")
print(len(mot) >= long_len)
```

> Bonus : alternativement, afficher `"😱"` si le mot est long et ne rien afficher sinon.

```python tags=["nbconvert_ignore"]
long_len = int(input("Long, c'est combien de caractères ? "))
mot = input("Saisir un mot :")
print("😱" * (len(mot) >= long_len))
```

Jeu : pourquoi ça marche ?

**Ne faites pas ça dans du vrai code**, on va voir dans le cours 3 comment faire mieux.
