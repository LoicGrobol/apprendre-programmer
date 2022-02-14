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
Cours 6 : TD récapitulatif
==========================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)

2022-02-15
<!-- #endregion -->

Dans ce notebook

- Des exercices.
- Encore des exercices.
- Toujours des exercices.
- Non vraiment rien d'autre que des exercices.

Il y a des rappels pour chacune des notions, mais n'hésitez pas à aller relire les cours précédents
et les corrections des exercices.

## Rappel : usage du notebook

Si vous avez suivi le bon lien, ce document est un *notebook interactif*, il contient des cellules
de texte et des cellules de code exécutable. Exécuter la  cellule courante (celle en surbrillance)
se fait en utilisant « execute » dans le menu « cell », en utilisant le bouton ▶️ de la barre
d'outils ou en appuyant simultanément sur les touches <kbd>ctrl</kbd> (ou
<kbd>cmd</kbd>/<kbd>⌘</kbd> pour les Macs) et <kbd>entrée</kbd>/<kbd>↲</kbd> de votre clavier.

Testez : cliquez sur le texte écrit dans une police différente ci-dessous et exécutez-la avec
chacune des méthodes proposées

```python
print("Salut à toi !")
```

Si rien ne se passe, vous n'êtes probablement pas dans le bon environnement : cliquez sur le bouton
suivant : [![Launch in Binder
badge](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LoicGrobol/apprendre-programmer/main?urlpath=tree/slides/06-recapitulatif/recapitulatif.py.md).


En cliquant sur les cellules de code, vous pouvez également modifier leur valeur : remplacez le
point d'exclamation par un point d'interrogation dans la cellule suivante et exécutez-la pour voir
ce qui se passe

```python
print("Salut à toi !")
```

Vous pouvez aussi créer de nouvelles cellules, supprimer des cellules existantes et changer leur
type (texte ou code) avec le menu « *edit* ».

Les cellules de texte sont écrites en
[Markdown](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html),
ce qui vous permet de les formatter. N'oubliez pas de sauvegarder vos modifications en les exécutant
(comme les cellules de code).


## Sorties

> **Rappel** : la fonction `print` permet d'afficher des choses sur une nouvelle ligne. On utilise
> une fonction en écrivant son nom, suivi d'un *argument* entre parenthèses :

```python
print("Bonjour, tout le monde !")
```

> `print` peut aussi recevoir plusieurs arguments, auquel cas ils seront affichées sur la même
> ligne, séparés par des espaces :

```python
print("Hello,", "world")
```

1\. Écrire dans la cellule ci-dessous un programme qui affiche votre nom complet, comme ceci :

```text
Loïc Grobol
```

```python

```

2\. Écrire dans la cellule ci-dessous un programme qui affiche votre année et votre lieu de
naissance, séparés par une ligne vide, comme ceci :

```text
1991

Orléans
```

```python

```

> **Note** : les espaces sont en général ignorées par Python, les lignes suivantes sont donc équivalentes :

```python
print("hello", "world")
print("hello","world")
print ("hello", "world")
print        (   "hello"  ,                                 "world"  )
```

> Par souci de lisibilité, on préfère la première forme. Attention en revanche, dans une chaîne de
> caractères, une espace est une espace

```python
print("hello             world")
```

## Types de base et opérations

> **Rappel** : les données manipulées par Python sont **typée**. Vous pouvez déterminer le type
> d'une donnée avec la fonction `type`

```python
type("spam")
```

> Les types de base (en tout cas pour ce cours) sont :
>
> - Les nombres entiers (`int`) écrits avec des chiffres

```python
print(1)
print(-2)
print(0)
print(2713)
```

> - Les nombres à virgule flottant (`float`), écrits avec des chiffres et le séparateur décimal `.`

```python
print(3.14)
print(-0.7)
print(1.0)
```


> - Les chaînes de caractères (`str`), écrites comme des suites caractères (unicode !) entre double
>   quotes `"` ou simple quotes `'`. Certains caractères doivent être écrits en utilisant une
>   séquence d'échappement, par exemple, le retour à la ligne se note `\n`. [La
>   doc](https://docs.python.org/fr/3/reference/lexical_analysis.html#string-and-bytes-literals)
>   vous donne la liste complète.

```python
print("Hello")
print("Python, je préférais quand c'était un 🐍")
print("1")
```

> - Les booléens (`bool`), qui ne sont que deux, `True` et `False`

```python
print(True)
print(False)
```

> - Pour les nombres, les opérations utilisables sont `+`, `-`, `*` (multiplication), `/`, `//`
>   (quotient), `%` (reste) et `**` (puissance) ; ainsi que les opérateurs de comparaison `<`, `>`,
>   `<=` et `>=`, qui renvoient des booléens.
> - Pour les chaînes de caractères, seules `+` (concaténation) et `*` (multiplication par un entier)
>   sont définies, ainsi que les opérateurs `in` et `not in` qui testent respectivement l'inclusion
>   d'une chaîne dans une autre et son contraire (et renvoient un booléen).
> - Pour les booléens, les opérateurs logiques `and`, `or` et `not`.
> - Les opérateurs `==` et `!=` qui testent respectivement l'égalité et la différence de deux
>   valeurs sont définis pour tous les types en renvoient des booléens.

```python
1 == 1
```

```python
-3.0 != 4.2
```

```python
"hello" != "Hello"
```

> - Partout en Python, on peut utiliser des parenthèses `(` `)` pour indiquer la priorité des
>   opérations.

```python
(3-2)*4
```

```python
3-2*4
```

> Partout où vous pouvez écrire une valeur littérale (comme `3`), vous pouvez également écrire une
> expression contenant des opérateurs :

```python
print(3)
print((2*6)/4)
print("Hello, world!")
print("Hello, " + "world")
```

1\. Affichez les résultats des calculs suivants : $2713+4096$, $\frac{12-75}{3}$, $2^10$,
$(-1)^{45+766}$ et $(512-256)\times\left(-\frac{3}{2}\right)$.

```python

```

2\. Construire et afficher une chaîne de caractères composée de $4096$ répétition de la séquence
`UPX>*`.

```python

```

3\. Construire et afficher une chaîne de caractères contenant `This is fine` suivie de $1024$ fois
`🔥`.

```python

```

4\. Déterminer sans les exécuter les valeurs de retour des instructions suivantes, écrivez les
résultats dans la cellule de texte en-dessous.



1. 

   ```python
   True or True
   ```

2. 

   ```python
   True or False
   ```

3. 

   ```python
   False and False
   ```

4. 

   ```python
   (False or True) and True
   ```

5. 

   ```python
   False or (True and True)
   ```

6. 

   ```python
   ("machin" in "truc") and (1 + 1 == 2)
   ```

7. 

   ```python
   ("a" in "apples") or (1 + 1 == 5)
   ```

8. 

   ```python
   ("apples" in "a") or (1 + 1 == 5)
   ```

9. 

   ```python
   (("apple" in "apples") and (1 + 1 == 3)) or (5 < 10)
   ```




1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 


(N'oubliez pas de valider votre saisie avec <kbd>ctrl</kbd>/<kbd>cmd</kbd>+<kbd>entrée</kbd>)

## Opérations sur les chaînes de caractères

> **Rappel** : Plusieurs méthodes de manipulations de chaînes de caractères sont disponible sous la
> forme `str.méthode`. Notamment les méthodes de manipulation de casse (majuscules et minuscules)
> `str.lower` (mettre en minuscules), `str.upper` (mettre en majuscules) et `str.title` (mettre en
> casse de titre).

```python
print(str.upper("hElLo"))
print(str.lower("hElLo"))
print(str.title("hElLo"))
```


1\. Mettre en minuscules la chaine de caractères `"ILliil1ILiiIILLL!1lIÎï"` et afficher le résultat.

```python

```

2\. Mettre en casse de titre la chaîne de caractères `Les maîtres de l'ombre` et afficher le
résultat.

```python

```

## Variables

> **Rappel** : une **variable** est un nom donné à une valeur. On crée une variable avec l'opérateur
> d'affectation `=`

```python
nom = "Loïc"
```

> une variable peut être utilisée partout où on peut utiliser une valeur littérale :

```python
print(nom)
```

> on peut ainsi utiliser une variable à chaque fois qu'on veut stocker une valeur (qui peut être le
> résultat d'une expression) pour l'utiliser plus tard :

```python
nombre = 1024 * 256
print(nombre)
```

```python
message = "This is fine."
fire = "🔥" * 1024
affiche = fire + message + fire
print(affiche)
```

> on peut également redéfinir une variable en affectant une deuxième fois au même nom

```python
nom = "Université Paris X"
nom = "Université Paris Ouest"
nom = "Université Paris Nanterre"
print(nom)
```

1\. Compléter la cellule suivante afin d'afficher la valeur de la variable `spam`

```python
spam = "spam, spam, lovely spam"
# Remplacer cette ligne (pas celle du dessus) par votre code
```

2\. Créer une variable contenant la chaîne de caractère `"Bonjour, tout le monde"`

```python

```

3\. Stocker le résultat du calcul suivant dans une variable et afficher son résultat : $\frac{36}{5}$

4\. Stocker $86$ dans une variable et $33$ dans une autre.

1. Stocker la somme dans une autre variable et afficher le résultat.
2. Afficher le type de la somme.

5\. Même chose que 4., mais avec les valeurs `"py"` et `"thon"`.

## Entrées

> **Rappel** : la fonction `input` permet de demander d'entrer une valeur au clavier, la saisie
> étant terminée en appuyant sur <kbd>entrée</kbd>. Essayez avec la cellule suivante. Attention,
> tant que vous n'appuyez pas sur <kbd>entrée</kbd> pour terminer la saisie, vous ne pourrez pas
> exécuter d'autres cellules.

```python tags=["skip-execution"]
input()
```

> En général, on stocke cette entrée dans une variable pour en faire quelque chose

```python tags=["skip-execution"]
print("Comment tu t'appelles ?")
nom = input()
print("Salut, ", nom)
```

> Attention, le résultat de `input` est toujours une chaîne de caractères. Si vous voulez la
> convertir en nombre, il faut le faire explicitement. Ainsi, ceci ne marche pas :

```python tags=["skip-execution"]
print("Dis-moi un nombre")
nombre = input()
print("Le double de ton nombre est ", 2*nombre)
```

Mais cela oui :

```python tags=["skip-execution"]
print("Dis-moi un nombre")
nombre = int(input())
print("Le double de ton nombre est ", 2*nombre)
```

> On peut aussi donner une chaîne de caractères comme argument à `input` pour ajouter un message à
> la saisie :

```python tags=["skip-execution"]
nom = input("Comment tu t'appelles ?")
print("Salut, ", nom)
```

1\. Demander la saisie d'un nombre et afficher son triple.

```python

```

2\. Demander la saisie d'une chaîne de caractères et l'afficher tout en majuscules.

```python

```

3\. Demander la saisie d'une chaîne de caractères. Afficher `True` si elle contient `spam` et
`False` sinon.

```python

```

4\. Écrire un programme qui demande à son utilisateurice son année de naissance et affiche l'âge
qu'aura cette personne en 2050.

```python

```

## Instruction conditionnelle `if`

> **Rappel** : l'instruction `if` permet de n'exécuter certaines instructions que si une si une
> condition (un booléen) est vraie (`True`) :

```python
if 1+1 == 2:
   print("Ceci est exécuté")

if 1+1 == 3:
   print("Mais pas cela")
```

> La condition peut-être n'import quelle expression dont le résultat est un booléen

```python
if "apple" not in "spam":
   print("Ceci est exécuté")

if True:
   print("Ceci est exécuté, mais ce n'est pas très intéressant.")

a = 2

if 2*a != 6:
   print("Ceci est exécuté et c'est plutôt classe.")
```

> Les instructions qui sont exécutées conditionnellement sont celles du bloc qui suit `if`,
> matérialisé par l'indentation (les lignes commençant par quatre espaces, que vous pouvez entrer
> avec la touche <kbd>tab</kbd>/<kbd>⇄</kbd>) :

```python
if 2+2 != 4:
   print("Ceci n'est pas exécuté")
   print("Cela non plus")
```

> On peut imbriquer les conditions les unes dans les autres, en augmentant l'indentation de quatre
> espaces supplémentaires pour chaque niveau :

```python
if 2+2 == 4:
   print("Ceci est exécuté")
   if 13 != 12:
      print("Ceci également")
      if "justice" in "partout":
         print("Mais pas ceci")
```

> L'instruction `elif` permet de tester des conditions supplémentaires si les précédentes ne sont
> pas remplies

```python
if 2+1 != 3:
   print("Non")
elif 3+2 == 12:
   print("Toujours pas")
elif "p" in "apples":
   print("Oui !")
```

> Et seulement si elles ne sont pas remplies :

```python
if 2+1 == 3:
   print("Oui")
elif "p" in "apples":
   print("Oui, mais trop tard")
```

> Enfin, `else` permet d'indiquer des instructions à exécuter si aucune des conditions précédentes
> n'a été remplie :

```python
if 2+1 != 3:
   print("Non")
elif 3+2 == 12:
   print("Toujours pas")
elif "p" in "APPLES":
   print("Non !")
else:
   print("Bon, ben tant pis")
```

> Dans ces exercices on va souvent écrire des conditions qui portent sur une entrée de
> l'utilisateurice (ce qui est plus intéressant que des conditions qui ne changent pas).
> Rappelez-vous que vous pouvez utiliser `input` :

```python
saisie = input("Dis-moi quelque chose")
if saisie == "Le TAL, c'est génial":
   print("Incroyable, tu lis dans mes pensées !")
else:
   print("ok,,,")
```

1\. Écrire un programme qui affiche `trop petit` si le résultat du calcul $2^11/3$ est plus petit 
que $1000$ sans jamais afficher le résultat du calcul lui-même.

2\. Demander la saisie d'une chaîne de caractères. Afficher `a` si la saisie est `voyelle`, `b` si
la saisie est `consonne`. N'affichez rien pour toute autre saisie.

```python

```

3\. Demander la saisie d'une chaîne de caractères contenant un nombre. Afficher `🥶` si ce nombre
est inférieur à $5$, $😌$ s'il est entre $5$ et $16$ et $🥵$ sinon.

```python

```

4\. Demandez à votre utilisateurice de saisir sa couleur préférée :

- Si la réponse contient `rouge`, affichez `🟥!`.
- Si la réponse contient `vert`, affichez `🟩!`.
- Si la réponse contient `violet` ou `indigo`, affichez `💜!`.
- Si la réponse est n'importe quoi d'autre, demandez `Tu penses avoir bon goût ?`.
  - Si la réponse à cette deuxième question est `oui`, affichez `😂`
  - Sinon, affichez `👉👉`

Utilisez `str.lower` pour comparer des chaînes sans tenir compte de la casse, comme ici :

```python
mot = "hELLo"

if str.lower(mot) == "hello":
   print("Ceci s'affiche")
```

## Séquences et listes

> **Rappel** : les chaînes de caractères sont composées de **caractères**, chacun ayant une
> position. L'opération d'indexation permet d'accéder à la valeur de ces caractères en connaissant
> leurs positions (en partant de `0`) :

```python
chn = "Bonjour"
print(chn[0])
print(chn[1])
print(chn[2])
print(chn[3])
print(chn[4])
print(chn[5])
```

> Cette propriété fait des chaînes de caractères des **séquences**. Il existe d'autres types de
> séquences en Python, notamment les listes, qui contiennent des suites de valeurs de n'importe quel
> type.

```python
lst = [1, 3, 5, "hello", True, 3.14]
print(lst[0])
print(lst[4])
print(lst[5])
```

> « n'importe quel type » signifie en particulier qu'une liste peut contenir une autre liste :

```python
lst = [1, 2, ["hello", "world"], True, 12]
lst[2]
```

> ce qui n'empêche pas d'accéder aux éléments des listes internes :

```python
lst = [1, 2, ["hello", "world"], True, 12]
sublst = lst[2]
print(sublst[0])

# Ou en plus compact

print(lst[2][0])
```

> Pour se faciliter la vie, quand on a une séquence on peut également accéder aux éléments en
> partant de la fin :

```python
lst = [1, 2, ["hello", "world"], True, 12]
print(lst[-1])
print("Hello, world!"[-2])
```

> Enfin, on peut extraire des sous-séquences :

```python
lst = ["a", "b", "c", "d", "e", "f", "g"]
print(lst[2])
print(lst[5])
print(lst[2:5])
```

1\. En utilisant uniquement les chaînes de caractères déjà définies dans la cellule-ci dessous,
modifiez cette cellule pour afficher `le nouveau monde tarde à apparaître`

```python
lst = ["le", "nouveau", "monde", "tarde", "à", "apparaître"]
print()
```

2\. Même question

```python
lst = ["le", "nouveau", ["monde", "tarde", "à"], "apparaître"]
print()
```

3\. Même question

```python
lst = ["le", "nouveau", ["monde", ["tarde"], "à"], "apparaître"]
print()
```

4\. Même question

```python
lst = ["le", "nouveau", "apparaître monde tarde à"]
print()
```

5\. Même question

```python
lst = ["le", [[[["nouveau"]]]], "apparaître monde tarde à"]
print()
```

6\. Même question en utilisant que des nombres négatifs ou nuls

```python
lst = ["le", "nouveau", ["monde", "tarde", "à"], "apparaître"]
print()
```

Bonus : en utilisant que des nombres strictement négatifs.

## Édition de listes

> **Rappel** : à la différence des chaînes de caractères, les listes sont **mutables**. C'est-à-dire
> qu'on peut modifier leurs éléments, en ajouter et en enlever :

```python
lst = ["le", "nouveau", "monde", "tarde", "à", "apparaître"]
print(lst)
lst[0] = "Le"
print(lst)
lst.append("naissent")
print(lst)
lst.extend(["Antonio Gramsci", "des monstre"])
print(lst)
lst.insert(6, "et dans ce clair-obscur")
print(lst)
lst.pop(-2)
print(lst)
```

1\. Modifiez la liste suivante à l'aide des instructions ci-dessus pour former l'alphabet latin

```python
lst = ["a", "b", "c", "g", "g", "g", "h", "i", "j", "spam", "k", "l", 1, "m", "n", "o", "p", "q", "r", "s", "t", "v"]
```

## Boucles d'itération

> **Rappel** la structure de contrôle `for` permet de répéter l'exécution d'un bloc de code (c'est
> donc une **boucle**) pour chacun des éléments d'une séquence (liste ou chaîne de caractères) :

```python
for elem in [1, 3, 1, 2]:
   print(elem)
   print(2*elem)
```

> Comme les autres structures de contrôle, les boucles peuvent être imbriquées :

```python
for i in [1, 2, 3, 4]:
   print(i)
   for w in ["tous", "les", "chats", "sont", "mignons"]:
      print(w)
```

> Une recette courante est de remplir une liste avec des saisies

```python tags=["skip-execution"]
couleurs = ["noire", "blanche", "rouge", "verte", "bleue"]
voyelles = []
for col in couleurs:
   voy = input("Quelle voyelle est, " + col + " ?")
   voyelles.append(voy)
print("Voici tes voyelles :", voyelles)
```

1\. Afficher sur des lignes séparées les carrés de nombres de la liste suivante :

```python
lst = [1, 3, 1, 2, 10, -75]
```

2\. En utilisant une boucle les mots suivants, chacun sur une ligne, en casse de titre (avec
`str.titlecase`)

```python
words = ["tRAIteMENT", "automAtique", "du", "langage", "à", "l'", "universitÉ", "paris", "nanterre"]
```

3\. Pour chacune des familles de langues indo-européennes de la liste suivante, demandez à
l'utilisateurice d'entrer une langue de la famille. Stockez ces entrées dans une liste et affichez
cette liste à la fin.

```python
familles = ["Romanes", "Germaniques", "Balto-slaves", "Celtiques", "Indo-ariennes"]
```
