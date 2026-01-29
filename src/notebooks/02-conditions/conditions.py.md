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
    display_name: apprendre-programmer-site (3.14.0)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 2 : Instructions conditionnelles
======================================

**L. Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

<!-- #endregion -->

Dans ce notebook , on présente les instructions conditionnelles `if`, `elif` et `else` et comment
elles permettent de changer l'exécution d'un programme avec des expressions booléennes.

Ce cours est inspiré du cours [*Control flow and
indexing*](https://github.com/aniellodesanto/Utah_CompLang21/blob/main/02_control_flow_and_indexing.ipynb)
d'Aniello de Santo, merci infiniment à lui.


---

Pour l'instant, nos programmes fonctionnent **séquentiellement** et de façon **déterministe** : les
instructions sont exécutées ligne de code par ligne de code, dans l'ordre où elles ont été écrite.

Pour la plupart des applications, c'est trop limité et on aimerait pouvoir n'exécuter certaines
instructions que si une certaine condition est remplie. Par exemple, un assistant vocal ne s'active
que quand une certaine phrase (« Ok, Google », « Dit, Siri »…).

## Instruction `if`

### Principe général

En Python, l'opérateur conditionnel `if` (« si »), introduit un **bloc de code** qui sera exécuté si
et seulement si une condition est remplie. En pseudo-code

```text
Instruction 0
if condition:
    Instruction 1
    Instruction 2
Instruction 3
```

Ici, si la condition est vérifiée, les instructions 0, 1, 2 et 3 seront exécutées ; mais si elle ne
l'est pas, alors seules les instructions 0 et 3 le seront.

Notez les points suivants :

- L'ordre dans lequel les instructions sont effectuées est le même dans les deux cas. Simplement,
  certaines ne sont pas toujours exécutées.
- Notez l'alinéa : les quatre espaces avant `Instruction 1` et `Instruction 2` sont ce qui indique à
  Python quelles instructions sont concernées par `if`.
  - On définit ainsi un bloc de code, on en verra d'autres dans ce cours

Voici un exemple concret

```python
user_1_age = 99
user_2_age = 30

print("Salut !")

if user_1_age > 90:
    print("Tu n'es plus tout jeune , numéro 1!")

if user_2_age > 90:
    print("Tu n'es plus tout jeune , numéro 2!")

print("Ciao")
```

**Rappel** : en Python, les lignes vides sont ignorées et ne servent qu'à rendre votre code plus
lisible. Écrire

```python
user_1_age = 99
user_2_age = 30
print("Salut !")
if user_1_age > 90:
    print("Tu n'es plus tout jeune , numéro 1!")
if user_2_age > 90:
    print("Tu n'es plus tout jeune , numéro 2!")
print("Ciao !")
```

est donc exactement équivalent pour Python.

```python
talkative = True
#talkative = False

if talkative:
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

Dans l'exemple ci-dessus, la variable `talkative` est utilisée comme un *flag* (on ne parle pas
vraiment de *drapeau*). On peut le faire dépendre d'une entrée de l'utilisateurice, ou d'une autre
partie du code

```python tags=["skip-execution"]
talkative = False

print("Tu aimes bavarder ?")
answer = input()

if answer == "oui":
    talkative = True

if talkative:
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

Le code ci-dessus est un peu redondant : il y a plus d'instruction que ce qui est strictement
nécessaire, mais il devrait vous montrer clairement comment faire dépendre l'exécution du code d'une
entrée.

### 🐁 Entraînement 🐁

Pouvez-vous simplifier le code précédent de telle sorte qu'il soit équivalent (c'est-à-dire qu'il
donne les mêmes sorties si on lui donne les mêmes entrées), mais en utilisant moins d'instructions ?

Vous pouvez faire des tests dans la cellule de code ci-dessous :

```python
talkative = False

print("Tu aimes bavarder ?")
answer = input()

if answer == "oui":
    talkative = True

if talkative:
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

<!-- #region slideshow={"slide_type": "slide"} -->
<details>
<summary>Solutions</summary>

En éliminant le premier test :

```python
print("Tu aimes bavarder ?")
answer = input()

talkative = (answer == "oui")

if talkative:
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

Sans créer de variable intermédiaire :

```python
print("Tu aimes bavarder ?")
answer = input()

if answer == "oui":
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

En mettant directement `input()` dans le test :

```python
print("Tu aimes bavarder ?")

if input() == "oui":
    print("On discute ?")
    
print("Ravie de te connaître en tout cas.")
```

</details>

<!-- #endregion -->

### Des blocs plus longs

On a dit qu'on pouvait inclure plusieurs instructions dans le bloc de code qui suit `if`. Voici ce
que ça donne :

```python
# Avant d'exécuter cette cellule, essayer de deviner les résultats en fonction des entrées

answer = input("Tu aimes bavarder ?")

if answer == "oui":
    print("Top ! On discute, alors ?")
    print("Moi j'aime le chocolat")
    print("Et le calcul ! Tu savais que 2713 est un nombre premier ?")

print("Ciao !")
```

Et même des `if`s imbriqués

```python tags=["skip-execution"]
# Avant d'exécuter cette cellule, essayer de deviner les résultats en fonction des entrées

answer = input("Tu aimes bavarder ?")

if answer == "oui":
    print("Top ! On discute, alors ?")
    print("Tu aimes le chocolat ? oui/non")
    answer2 = input()
    if answer2 == "non":
        print("Monstre !")
        print("Adieu !")
print("Ciao !")
```

Comment Python sait-il à quel bloc appartient chaque instruction ? Avec la longueur des alinéas !
L'**indentation** joue un rôle très important en Python (on y reviendra. Plusieurs fois.).

### 🔎 Entraînement 🔎

Essayez d'exécuter le programme précédent avec différentes combinaisons d'entrée. Assurez-vous de
bien comprendre à quelles conditions chacune des instructions est exécutée.

---

Est-ce qu'il est possible d'avoir une instruction `if` sans condition ? Un `if` qui ne serait pas
suivi par un bloc ? Essayez ces différentes options dans la cellule suivante.

```python

```

## `else`

Considérez le programme suivant

```python
print("Bonjour !")
s = input("C'est quoi ton fruit préféré ?")

if "banane" in s:
    print("Oh moi aussi !")

print("Salut !")
```

Comment faire pour afficher quelque chose uniquement dans le cas où la condition `if "banane" in s` n'est pas vérifiée ?

On peut faire comme ça :

```python tags=["skip-execution"]
print("Bonjour !")
s = input("C'est quoi ton fruit préféré ?")

if "banane" in s:
    print("Oh moi aussi !")

if not ("banane" in s):
    print("Oh ! Moi c'est les bananes !")

print("Salut !")

```

Ou encore (rappellez vous de la séance précédente) :

```python
print("Bonjour !")
s = input("C'est quoi ton fruit préféré ?")

if "banane" in s:
    print("Oh moi aussi !")

if "banane" not in s:
    print("Oh ! Moi c'est les bananes !")

print("Salut !")

```

Mais c'est un peu redondant : on a besoin de refaire un test dont on connaît déjà le résultat. Il nous faudrait plutôt une façon de compléter notre premier « si » par un « sinon ».

Python nous propose pour ça l'instruction `else`. Voici comment on l'utilise. D'abord en pseudo-code

```text
if condition:
    code à exécuter si la condition est vraie
else:
    code à exécuter si la condition est fausse
```

Et en Python

```python
print("Bonjour !")
s = input("C'est quoi ton fruit préféré ?")

if "banane" in s:
    print("Oh moi aussi !")
else:
    print("Oh ! Moi c'est les bananes !")

print("Salut !")

```

`else` est liée au `if` qui le précède et ne permet pas d'ajouter une condition. On peut donc avoir
un `if` sans `else`, mais pas l'inverse.


```python tags=["raises-exception"]
sentence = "Les idées vertes incolores dorment furieusemen"

else:
    print("machin")
```

**Attention**, `else` est lié **seulement** au `if` précédent

```python
sentence = "Les idées vertes incolores dorment furieusement"

if "rouge" in sentence:
    print("Rouge !")

if "vert" in sentence:
    print("Vert !")
else:
    print("Aucune couleur n'a été trouvée")
```

On peut avoir des `else` dans un bloc conditionnel :

```python
answer = input("Tu aimes bavarder ?")

if answer == "Oui":
    print("Top ! On discute, alors ?")
    print("Tu aimes le chocolat ? Oui/Non")
    answer2 = input()
    if answer2 == "Non":
        print("Monstre !")
        print("Adieu !")
    else:
        print("Bravo")

print("Ciao !")
```

Ici le `else` est au même niveau d'indentation que le premier `if`, c'est donc à ce dernier qu'il est lié :

```python tags=["skip-execution"]
answer = input("Tu aimes bavarder ?")

if answer == "Oui":
    print("Top ! On discute, alors ?")
    print("Tu aimes le chocolat ? Oui/Non")
    answer2 = input()
    if answer2 == "Non":
        print("Monstre !")
        print("Adieu !")
else:
    print("Dommage")

print("Ciao !")
```

## `elif`

Comme on l'a vu précédemment, des `if` peuvent être imbriqués. Que fait alors la cellule suivante ?

```python
sentence = "Les idées vertes incolores dorment furieusement"

if "rouge" in sentence:
    print("Rouge !")
else:
    if "vert" in sentence:
        print("Vert !")
    else:
        if "incolore" in sentence:
            print("Incolore !")

print("Finito")
```

Il est assez fréquent de rencontrer ce type de structures, et même plus profondément imbriquées, ce
qui rend le code plus difficile à lire.

```python
sentence = "Les idées vertes incolores dorment furieusement"

if "rouge" in sentence:
    print("Rouge !")
else:
    if "vert" in sentence:
        print("Vert !")
    else:
        if "bleu" in sentence:
            print("Bleu !")
        else:
            if "violet" in sentence:
                print("Violet !")
            else:
                if "incolore" in sentence:
                    print("Incolore !")
```


Il y a cependant une alternative : `elif` (« sinon, si »), qui nous permet de réécrire le code
précédent plus lisiblement :

```python
sentence = "Les idées vertes incolores dorment furieusement"

if "rouge" in sentence:
    print("Rouge !")
elif "vert" in sentence:
    print("Vert !")
elif "incolore" in sentence:
    print("Incolore !")
```

`elif` vérifie à la fois qu'une condition est vraie, et que toutes les conditions précédentes sont
fausses. En pseudo-code

```text
if condition1:
    code exécuté si la condition 1 est vraie
elif condition2:
    code exécuté si la condition 1 est fausse et la condition 2 est vraie
elif condition3:
    code exécuté si les condition 1 et 2 sont fausses et la condition 3 est vraie
⋮
```

En revanche attention : si vous voulez tester indépendamment lesquels de ces mots apparaissent dans
la phrase, il faut des blocs `if` différents . Comparez avec la cellule suivante :

```python
sentence = "Les idées vertes incolores dorment furieusement"

if "rouge" in sentence:
    print("Rouge !")

if "vert" in sentence:
    print("Vert !")

if "incolore" in sentence:
    print("Incolore !")
```

Enfin, on peut ajouter un `else` à la fin d'une suite de `elif`, pour indiquer du code à exécuter si
aucune des conditions n'est remplie


```python
sentence = "Les idées vertes incolores dorment furieusement"

if "rouge" in sentence:
    print("Rouge !")
elif "violet" in sentence:
    print("Violet !")
elif "indigo" in sentence:
    print("Indigo!")
else:
    print("😠")
```

Et on peut continuer à imbriquer des blocs arbitrairement.

### 🦾 Entraînement 🦾

```python tags=["skip-execution"]
user_mood = input("Quelle est ton humeur: ")

if "heureu" in user_mood:
    print("😄")
    if "relax" in user_mood:
        print("😌")
    else:
        print("🫂")
else:
    print("💜")
```

Réécrire le code précédent en utilisant `elif` et une expression booléenne complexe, comme dans ce
qui suit

```python
test = "Le chat est content"

if "chat" in test and "content" in test:
    print("Hello")
else:
    print("bye")
```

```python
# Coder ici
```

<!-- #region -->
<details>
<summary>Solution</summary>

```python
user_mood = input("Quelle est ton humeur: ")

if "heureu" in user_mood and "relax" in user_mood:
    print("😄")
    print("😌")
elif "heureu" in user_mood:
    print("😄")
    print("🫂")
else:
    print("💜")
```

</details>
<!-- #endregion -->

## Des conditions inattendues

Essayez d'expliquer les résultats des cellules suivantes

```python
if "spam":
    print("machin")
else:
    print("bidule")
```

```python
if "":
    print("machin")
else:
    print("bidule")
```

```python
if 2713:
    print("machin")
else:
    print("bidule")
```

```python
if -1:
    print("machin")
else:
    print("bidule")
```

```python
if 0:
    print("machin")
else:
    print("bidule")
```

Outre les booléens `True` et `False`, la plupart des objets en Python ont une *véracité*
(*truthiness*). La plupart sont vrais, ceux qui sont faux sont en général d'une façon ou d'une
autre vides, nuls… Nous verrons d'autres exemples.

```python
print(bool("abc"))
```

Je vous recommande plutôt de faire les tests explicitement :

```python
s = "spam"

if len(s) > 0:  # len() renvoie la longueur de la chaîne
    print("machin")
else:
    print("bidule")
```

```python
print(len("spam"))
```

```python
i = 2

if i != 0:
    print("Vrai!")
else:
    print("Faux")
```

## Exercices

Répondre à ces exercices directement dans le notebook, le sauvegarder sous un nom de la forme
`02_conditions_PRENOM_NOM.ipynb` (pour Morgan Lefeuvre par exemple, ce serait
`02_conditions_Morgan_Lefeuvre.ipynb`) et me le transmettre avant dimanche soir prochain via Cours en Ligne.

### 😱 Exercice 1 😱


Demander à l'utilisateurice d'entrer de saisir un mot, puis afficher `"😱"` si le mot fait plus de
10 caractères et afficher `"😌"` sinon.

### 💬 Exercice 2 💬 : un chatbot basique

Demandez à votre utilisateurice si son humeur est bavarde. Si la réponse n'est pas « oui »,
souhaitez-lui une bonne journée. Sinon, demandez lui comment ça va et répondez différemment suivant
que sa réponse contient les mots

- « bien » ou « bon »
- « mal » ou « mauvais » ou « horrible »
- n'importe quoi d'autre

```python

```

### 🐉 Exercice 3 🐉

Dans le jeu de rôle Donjons et Dragons, les personnages ont un alignement qui les positionne sur
deux axes : loyal—neutre—chaotique et bon—neutre—mauvais. Le choix d'un alignement détermine les
classes possibles pour ce personnage :

- Les paladins sont loyal bon
- Les antipaladins sont chaotiques mauvais
- Les moines sont de n'importe quel alignement loyal
- Les roublards sont de n'importe quel alignement qui n'est pas loyal
- Les druides sont de n'importe quel alignement neutre (sur n'importe lequel des deux axes)
- Les guerriers peuvent être de n'importe quel alignement

Écrire un programme qui demande de choisir un alignement et affiche les classes de personnages
disponibles. Voici un exemple d'à quoi pourrait ressembler une session d'utilisation de ce programme

```text
Choisir un alignement parmis loyal—neutre—chaotique: chaotique
Choisir un alignement parmis bon—neutre—mauvais: bon

Vous êtes chaotique bon. Vous pouvez être :

- Roublard
- Guerrier
```

La liste affichée ne doit pas contenir de doublons.

**Conseil** avant de commencer à coder, commencez par dessiner ou écrire sur papier la structure
qu'aura votre programme

- Combien de branches conditionnelles y aura-t-il ?
- Quelles conditions dépendent les unes des autres ?
- Comment vais-je gérer les imbrications ?


### Réflexion

Quelques points auxquels réfléchir

- Combien de temps avez-vous passé à faire ces exercices ?
- Qu'est-ce qui vous a paru le plus compliqué ?
- À votre avis, pourquoi ?

