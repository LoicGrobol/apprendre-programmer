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
Cours 5 : Corrections
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

## 🔄 Exo 🔄

Voici une liste

```python
fruits = ["pomme", "poire", "kiwi", "maracuja"]
```

Demandez à l'utilisateurice un nom de fruit et affichez `"😋"` s'il est dans la liste et `"🤨"`
sinon.

```python tags=["skip-execution"]
reponse = input("Quel fruit ? ")

if reponse in fruits:
    print("😋")
else:
    print("🤨")
```

## Blockly games

→ Voir par exemple les solutions sur
<https://s4scoding.com/googles-blockly-games-maze-1-10-solutions>.

## 🤔 Exo 🤔

> On peut obtenir un entier aléatoire en utilisant la fonction `randint` du module `random` :

```python
import random
```

```python
random.randint(4, 8)
```

> Écrivez un programme qui :

> - Choisit aléatoirement un nombre entre $1$ et $10$
> - Demande à l'utilisateurice de deviner le nombre en lui proposant de réessayer tant que le nombre
>   n'a pas été trouvé.
>
> Exemple de sortie :
>
> ```text
> J'ai choisi un nombre entre 1 et 10. Essaie de le deviner !
> Fais ton choix: 1
> Essaie encore: 5
> Essaie encore: 7
> Essaie encore: 2
> Bravo! C'était bien 2
> ```

```python tags=["skip-execution"]
nombre_secret = random.randint(1, 10)
print("J'ai choisi un nombre entre 1 et 10. Essaie de le deviner !")
essai = int(input("Fais ton choix: "))
while essai != nombre_secret:
    essai = int(input("Essaie encore:"))
print("Bravo! C'était bien", nombre_secret)
```
