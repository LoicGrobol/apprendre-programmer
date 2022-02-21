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

2022-02-21
<!-- #endregion -->

## 🔄 Exo 🔄

Voici une liste

```python
fruits = ["pomme", "poire", "kiwi", "maracuja"]
```

Demandez à l'utilisateurice un nom de fruit et affichez `"😋"` s'il est dans la liste et `"🤨"` sinon.

```python
reponse = input("Quel fruit ? ")

if reponse in fruits:
    print("😋")
else:
    print("🤨")
```

## Blockly games

→ Voir par exemple les solutions sur
<https://s4scoding.com/googles-blockly-games-maze-1-10-solutions>.

## Power of Thor

> [Power of Thor E01](https://www.codingame.com/training/easy/power-of-thor-episode-1)

<!-- #region -->

On peut penser à une première version basique : on cherche d'abord à avoir la bonne abscisse, puis
la bonne ordonnée :

```python
# Code original pour réupérer les positions
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# **AJOUTS** on garde en mémoire la position actuelle
current_tx = initial_tx
current_ty = initial_ty

while True:
    # À conserver pour faire plaisir à CodinGame
    remaining_turns = int(input())

    if light_x > current_tx:
        print("E")
        current_tx = current_tx + 1
    elif light_x < current_tx:
        print("W")
        current_tx = current_tx - 1
    # Attention : les ordonnées vont de haut en bas
    elif light_y > current_ty:
        print("S")
        current_ty = current_ty + 1
    else:
        print("N")
        current_ty = current_ty - 1
```

Problème, ça ne marche pas pour le test 4 « *optimal angle* ». Ce qui cloche c'est qu'on utilise pas
les diagonales, ce qui nous fait perdre du temps. On peut arranger ça en combinant les cas quand on
doit changer à la fois d'abscisse et d'ordonnée :

```python
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_tx = initial_tx
current_ty = initial_ty

while True:
    remaining_turns = int(input())

    if light_x > current_tx:
        if light_y > current_ty:
            print("SE")
            current_ty = current_ty + 1
        elif light_y < current_ty:
            print("NE")
            current_ty = current_ty - 1
        else:
            print("E")
        current_tx = current_tx + 1
    elif light_x < current_tx:
        if light_y > current_ty:
            print("SW")
            current_ty = current_ty + 1
        elif light_y < current_ty:
            print("NW")
            current_ty = current_ty - 1
        else:
            print("W")
        current_tx = current_tx - 1
    elif light_y > current_ty:
        print("S")
        current_ty = current_ty + 1
    else:
        print("N")
        current_ty = current_ty - 1
```

Ce coup-ci ça marche, par contre, c'est très verbeux : on se répète beaucoup. Voici une solution
plus compacte en déterminant indépendamment les déplacements sur chacun des axes et en combinant les
résultats à la fin :

```python
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_tx = initial_tx
current_ty = initial_ty

while True:
    remaining_turns = int(input())
    
    if light_x > current_tx:
        direction_ew = "E"
        current_tx = current_tx + 1
    elif light_x < current_tx:
        direction_ew = "W"
        current_tx = current_tx - 1
    else:
        direction_ew = ""
    
    if light_y > current_ty:
        direction_sw = "S"
        current_ty = current_ty + 1
    elif light_y < current_ty
        direction_sw = "N"
        current_ty = current_ty - 1
    else:
        direction_sw = ""

    print(direction_sw + direction_ew)
```

Comme d'habitude, il y a beaucoup d'autres solutions et en particulier des beaucoup plus compactes. C'est un bon entraînement de chercher la façon de résoudre ce problème en un minimum de caractères, on dit qu'on fait du *Code Golf*.

<!-- #endregion -->

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
