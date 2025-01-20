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
Cours 1 : Solutions
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

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
texte = "Toi dont le trône étincelle, ô immortelle " \
        "Aphrodite, fille de Zeus, ourdisseuse de " \
        "trames, je t'implore : ne laisse pas, ô souveraine, " \
        "dégoûts ou chagrins affliger mon âme, " \
        "Mais viens ici, si jamais autrefois " \
        "entendant de loin ma voix, tu as " \
        "écoutée, quand, quittant la demeure " \
        "dorée de ton père tu venais, après avoir " \
        "attelé ton char,"
```

> Écrire un programme qui demande à l'utilisateurice de saisir un mot, puis affiche `True` si le mot
> est dans le texte (autrement dit s'il est inclus dans la variable `texte`) et `False` sinon.

Voici une solution qui marche presque (et ça me suffit pour cette fois !)

```python tags=["skip-execution"]
mot = input("Saisir un mot : ")
print(mot in texte)
```

Pourquoi « presque » ? Essayez avec « mortel ». Vous voyez le problème ?

Voici une solution plus compliquée, mais qui marche complètement

```python tags=["skip-execution"]
mot = input("Saisir un mot : ")
print(
  " " + mot + " "  in texte
  or " " + mot + "," in texte
  or mot == "Toi"
)
```

### Exercice 2

> Écrire un programme qui vérifie si le mot *banane* est contenue dans une entrée récupérée avec
> `input`

```python tags=["skip-execution"]
texte = input("Saisir un texte : ")
print("banane" in texte)
```

### Exercice 3

> Écrire un programme qui demande à son utilisateurice son année de naissance et affiche l'âge
> qu'aura cette personne en 2048.
>
> Indice : `int`

```python tags=["skip-execution"]
annee_str = input("Tu es né⋅e quand ? ")
annee_int = int(annee_str)
age = 2048 - annee_int
print("En 2048 tu auras", age, "ans")
```

ou encore

```python tags=["skip-execution"]
annee_str = input("Tu es né⋅e quand ? ")
annee_int = int(annee_str)
age = 2048 - annee_int
print("En 2048 tu auras " + str(age) + " ans")
```

ou mieux

```python tags=["skip-execution"]
annee_str = input("Tu es né⋅e quand ? ")
annee_int = int(annee_str)
age = 2048 - annee_int
print(f"En 2048 tu auras {age} ans")
```

## Retour sur vos rendus

Attention à ne pas confondre les rôles de `print` et `input`

- `print` pour **afficher** du texte
- `input` pour **récupérer** du texte

---

Si une question vous paraît difficile, pensez à vous poser avec du papier et un crayon. Noter les
entrées et les sorties du programme (sans détailler comment est fait le traitement) peut vous aider.

---

Pensez à utiliser des variables pour stocker des résultats intermédiaires ou des entrées. Ne faites
pas :

```python tags=["skip-execution"]
texte = input()
print("banane" in "J'aime les bananes")
```

Mais plutôt

```python tags=["skip-execution"]
texte = input()
print("banane" in texte)
```

---

Quelques points de style

- Pas d'espace entre le nom d'une fonction et les parenthèses : `print("Salut")` et non `print
  ("Salut")`, `int("2713")` et pas `int ("2713")`.
- Quand la question demande un affichage, utilisez plutôt `print` que de simplement laisser Jupyter
  afficher le dernier résultat.
- On peut terminer une chaîne de caractère par une espace :

```python
nom = "Loïc"
print("Je m'appelle " + nom)
```
