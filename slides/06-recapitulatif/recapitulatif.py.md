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

## Rappel : usage du notebook

Si vous avez suivi le bon lien, ce document est un *notebook interactif*, il contient des cellules
de texte et des cellules de code exécutable. Exécuter la  cellule courante (celle en surbrillance)
se fait en utilisant « execute » dans le menu « cell », en utilisant le bouton ▶️ de la barre
d'outils ou en appuyant simultanément sur les touches <kbd>ctrl</kbd> (ou <kbd>cmd</kbd>/<kbd>⌘</kbd> pour les
Macs) et <kbd>entrée</kbd>/<kbd>↲</kbd> de votre clavier.

Testez : cliquez sur le texte écrit dans une police différente ci-dessous et exécutez-la avec
chacune des méthodes proposées

```python
print("Salut à toi !")
```

Si rien ne se passe, vous n'êtes probablement pas dans le bon environnement : cliquez sur le bouton
suivant : [![Launch in Binder
badge](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LoicGrobol/apprendre-programmer/main?urlpath=tree/slides/06-recapitulatif/recapitulatif.py.md).


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
>   (quotient), `%` (reste), et `**` puissance.
> - Pour les chaînes de caractères, seules `+` (concaténation) et `*` (multiplication par un entier)
>   sont définies, ainsi que l'opérateur `in` qui teste l'inclusion d'une chaîne dans une autre (et
>   renvoie donc un booléen).
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
résultats dans la cellule de texte en-dessous

<!-- #region -->

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

<!-- #endregion -->


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
nom = "Université Paris X
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