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
Cours 2 : Solutions
=====================

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

## 🐁 Exo 🐁

Pouvez-vous simplifier le code précédent de telle sorte qu'il soit équivalent (c'est-à-dire qu'il
donne les mêmes sorties si on lui donne les mêmes entrées), mais en utilisant moins d'instructions ?

Vous pouvez faire des tests dans la cellule de code ci-dessous :

```python tags=["skip-execution"]
print("Tu aimes bavarder ?")
answer = input()

talkative = (answer == "oui")

if talkative:
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

```python tags=["skip-execution"]
print("Tu aimes bavarder ?")
answer = input()

if answer == "oui":
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

Dernière version, un peu **trop** synthétique :

```python tags=["skip-execution"]
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

```python tags=["skip-execution"]
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

## Exercices

### Exercice 1


> Demander à l'utilisateurice d'entrer de saisir un mot, puis afficher `"😱"` si le mot fait plus de
10 caractères et afficher `"😌"` sinon.

```python tags=["skip-execution"]
mot = input("Saisir un mot :")
if len(mot) >= 10:
    print("😱")
else:
    print("😌")
```

## 💬 Exercice 2 💬 : un chatbot basique

> Demandez à votre utilisateurice si son humeur est bavarde. Si la réponse n'est pas « oui »,
> souhaitez-lui une bonne journée. Sinon, demandez lui comment ça va et répondez différemment
> suivant que sa réponse contient les mots
> 
> - « bien » ou « bon »
> - « mal » ou « mauvais » ou « horrible »
> - n'importe quoi d'autres

```python tags=["skip-execution"]
talkative = input("Es-tu d'humeur bavarde ? ")

if talkative == "oui":
    mood = input("Et de quelle humeur es-tu ? ")
    if "bien" in mood or "bon" in mood:
        print("Ah, top, ça fait plaisir !")
    elif "mal" in mood or "mauvais" in mood:
        print("Oh non, je suis vraiment désolé⋅e !")
    else:
        print("Je ne sais pas ce que ça veut dire, pardon.")
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
> La liste affichée ne doit pas contenir de doublons.
>
> **Conseil** avant de commencer à coder, commencez par dessiner ou écrire sur papier la structure
> qu'aura votre programme
>
> - Combien de branches conditionnelles y aura-t-il ?
> - Quelles conditions dépendent les unes des autres ?
> - Comment vais-je gérer les imbrications ?

```python tags=["skip-execution"]
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
