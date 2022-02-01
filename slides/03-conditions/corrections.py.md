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
Cours 3 : Corrections
=====================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-01-25
<!-- #endregion -->

## 🐁 Exo 🐁

Pouvez-vous simplifier le code précédent de telle sorte qu'il soit équivalent (c'est-à-dire qu'il
donne les mêmes sorties si on lui donne les mêmes entrées), mais en utilisant moins d'instructions ?

Vous pouvez faire des tests dans la cellule de code ci-dessous :

```python
print("Tu aimes bavarder ?")
answer = input()

talkative = (answer == "oui")

if talkative:
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

```python
print("Tu aimes bavarder ?")
answer = input()

if answer == "oui":
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

Dernière version, un peu **trop** synthétique :

```python
print("Tu aimes bavarder ?")

if input() == "oui":
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

## 🦾 Entraînement 🦾

> Réécrire le code précédent en utilisant `elif` et une expression booléenne complexe, comme dans ce
> qui suit

```python
test = "Le chat est content"

if "chat" in test and "content" in test:
    print("Hello")
else:
    print("bye")
```

```python tags=["nbconvert_ignore"]
user_mood = input("Quelle est ton humeur: ")

if "heureu" in user_mood and "relax" in user_mood:
    print("😄")
    print("😌")
elif"heureu" in user_mood:
    print("😄")
    print("🫂")
else:
    print("💜")
```

## 💬 Entraînement 💬 : un chatbot basique

Demandez à votre utilisateurice si son humeur est bavarde. Si la réponse n'est pas « oui »,
souhaitez-lui une bonne journée. Sinon, demandez lui comment ça va et répondez différemment suivant
que sa réponse contient les mots

- « bien » ou « bon »
- « mal » ou « mauvais » ou « horrible »
- n'importe quoi d'autres

```python tags=["nbconvert_ignore"]
talkative = input("Es-tu d'humeur bavarde ? ")

if talkative.lower() == "oui":
    mood = input("Et de quelle humeur es-tu ? ")
    if "bien" in mood or "bon" in mood:
        print("Ah, top, ça fait plaisir !")
    elif "mal" in mood or "mauvais" in mood:
        print("Oh non, je suis vraiment désolé⋅e !")
    else:
        print("Je ne sais pas ce que ça veut dire, pardon.")
```

## Exercices

### Exercice 1


> Demander à l'utilisateurice d'entrer un nombre minimal de caractères pour qu'un mot soit considéré
> comme long. Puis lui demander de saisir un mot et afficher `"😱"` si le mot est long et `"😌"` > sinon.

```python tags=["nbconvert_ignore"]
long_len = int(input("Long, c'est combien de caractères ? "))
mot = input("Saisir un mot :")
if len(mot) >= long_len:
    print("😱")
else:
    print("😌")
```

### 🐉 Exercice 2 🐉

> Dans le jeu de rôle Donjons et Dragons, les personnages ont un alignement qui les positionne sur
> deux axes : loyal—neutre—chaotique et bon—neutre—mauvais. Le choix d'un alignement détermine les
> classes possibles pour ce personnage :
>
> - Les paladins sont loyal bon
> - Les antipaladins sont chaotiques mauvais
> - Les moines sont de n'importe quel alignement loyal
> - Les roublards sont de n'importe quel alignement qui n'est pas loyal
> - Les druides sont de n'importe quel alignement neutre (sur n'import lequel des deux axes)
> - Les guerriers peuvent être de n'importe quel alignement
>
> Écrire un programme qui demande de choisir un alignement et affiche les classes de personnages
> disponibles. Voici un exemple d'à quoi pourrait ressembler une session d'utilisation de ce
> programme
>
> ```text
> Choisir un alignement parmis loyal—neutre—chaotique: chaotique
> Choisir un alignement parmis bon—neutre—mauvais: bon
>
> Vous êtes chaotique bon. Vous pouvez être :
>
> - Roublard
> - Guerrier
> ```
>
> La liste affichée ne doit pas contenir de doublons. Si un des choix n'existes pas, signalez-le et
> utilisez neutre à la place.
>
> **Conseil** avant de commencer à coder, commencez par dessiner ou écrire sur papier la structure
> qu'aura votre programme
>
> - Combien de branches conditionnelles y aura-t-il ?
> - Quelles conditions dépendent les unes des autres ?
> - Comment vais-je gérer les imbrications ?

```python tags=["nbconvert_ignore"]
law = input("Choisir un alignement parmis loyal—neutre—chaotique : ")
moral = input("Choisir un alignement parmis bon—neutre—mauvais : ")

print("Vous êtes", law, moral, "Vous pouvez être :")

print("- Guerrier")

if law == "loyal":
    if moral == "bon":
        print("- Paladin")
    print("- Moine")
else:
    print("- Roublard⋅e")

# On aurait pû imbriquer ceci dans le `else` précédent mais ça n'apporte pas grand chose
if law == "chaotique" and moral == "mauvais":
    print("- Antipaladin")

# Imbriquer ceci dans les tests précédents nous obligerait à dupliquer du code
if law == "neutre" or moral == "neutre":
    print("- Druide")
```


### 📅 Exercice 3 📅

> Une année est bissextile si son numéro est divisible par $4$, sauf si c'est la dernière d'un siècle
> (i.e. elle est divisible par $100$, par exemple 1900), auquel cas, elle est bissextile
> seulement si son numéro est divisible par $400$.
> 
> Écrire un programme qui indique si une année entrée par l'utilisateurice est bissextile ou non.
> 
> **Indice** l'opérateur modulo `%`, qu'on a vu dans le cours 1 peut vous être utile. En particulier,
> un nombre $a$ est divisible par un nombre $b$ si et seulement si `a % b == 0`.


```python tags=["nbconvert_ignore"]
year = int(input("On parle de quelle année ? "))

divisible_par_4 = (year % 4 == 0)

if divisible_par_4:
    divisible_par_100 = (year % 100 == 0)
    if divisible_par_100:
        divisible_par_400 = (year % 400 == 0)
        if divisible_par_400:
            print("Bissextile !")
        else:
            print("Non-bissextile")
    else:
        print("Bissextile !")
else:
    print("Non-bissextile")
```

On peut faire plus compact sans les variables

```python tags=["nbconvert_ignore"]
year = int(input("On parle de quelle année ? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Bissextile !")
        else:
            print("Non-bissextile")
    else:
        print("Bissextile !")
else:
    print("Non-bissextile")
```

On peut aussi combiner les conditions

```python tags=["nbconvert_ignore"]
year = int(input("On parle de quelle année ? "))

divisible_par_4 = (year % 4 == 0)
divisible_par_100 = (year % 100 == 0)
divisible_par_400 = (year % 400 == 0)

if divisible_par_4 and (not divisible_par_100 or divisible_par_400):
    print("Bissextile !")
else:
    print("Non-bissextile")
```

et resupprimer les variables

```python tags=["nbconvert_ignore"]
year = int(input("On parle de quelle année ? "))

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print("Bissextile !")
else:
    print("Non-bissextile")
```

voire même exploiter le fait que `0` est le seul entier `False`, mais ça devient vraiment
désagréable

```python tags=["nbconvert_ignore"]
year = int(input("On parle de quelle année ? "))

if not year % 4 and (year % 100 or not year % 400):
    print("Bissextile !")
else:
    print("Non-bissextile")
```

## Retour sur vos rendus

En général :

- Un certain nombre d'entre vous n'a rien rendu.
  - En soi ce n'est pas dramatique : les exercices ne sont pas obligatoires, mais s'astreindre à
    rendre quelque chose devrait vous aider à revenir sur le cours et à vous entraîner.
  - Tous les rendus, même partiels, sont utiles.
  - Vous n'avez rien à perdre à rendre quelque chose : au pire ça ne compte pas, mais si vous
    réussissez des exercices, vous validez des compétences, ce qui peut permettre de rattraper un
    raté sur le projet ou le partiel.
- Pensez à bien remplir la partie réflexion à la fin des exercices !
- Si des consignes vous paraissent peu claires, ou si vous ne comprenez pas quelque chose, n'héistez
  **vraiment** pas à m'écrire.
- Attention au format et au nom des fichiers : je vous refais en cours une démonstration de comment
  bien exporter vos travaux.

En particulier :

- Les exercices qui ont été rendus ont été dans l'ensemble bien réussis (ou l'inverse)
- Pour l'exercice 2, on pouvait certes faire par force brute, et c'est tout à fait correct, mais il
  y avait plus simple.

