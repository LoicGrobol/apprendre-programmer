---
jupyter:
  jupytext:
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
<!-- #region slideshow={"slide_type": "slide"} -->
Cours 8 : valeur de retour et accès aux fichiers
=================================================

**Loïc Grobol** [<lgrobol@parisnanterre.fr>](mailto:lgrobol@parisnanterre.fr)
<!-- #endregion -->

Dans ce notebook

- Un nouveau pouvoir pour les fonctions
- Accéder à des fichiers externes.

Ce cours est inspiré du cours [*File
IO*](https://github.com/aniellodesanto/Utah_CompLang21/blob/main/04b_file_io.ipynb) d'Aniello de
Santo. Merci à lui.

## Valeur de retour

Pour l'instant, les fonctions qu'on a définies affichent toujours quelque chose.

```python
def f():
    print("hello")
```

```python
f()
```

```python
def bonjour(nom):
    print("Bonjour,", nom)
```

```python
bonjour("Loïc")
```

```python
bonjour("Morgan")
```

```python
def truc(i):
    j = i + 5
    k = 2*i
    print(k)
```

```python
truc(9)
```

Ce n'est pas une obligation :

```python
def ssss(arg):
    bidule = arg*2
    for i in range(10):
        bidule = bidule + i
        
ssss(3)
```

Ici, la fonction `ssss` a bien été exécutée, mais elle ne fait rien de visible.


Par contre, remarquez un truc : parfois dans le passé, on a stocké le résultat de fonctions dans des
variables. Par exemple

```python
longueur = len("anticonstitutionnellement")
```

On a bien appelé la fonction `len`, qui n'affiche rien. Donc rien ne s'affiche.


En revanche, on a bien fait quelque chose ici : on a donné une valeur à la variable `longueur`.

```python
print(longueur)
```

Autrement dit, `len` ne fait pas un affichage : elle transmet plutôt une information : la longueur
de son argument. On dit qu'elle a **renvoyé** (*return*) une valeur.


Et nos fonctions, elles renvoient quelque chose ?

```python
def bonjour():
    reponse = "Salut"
    print(reponse)
    
varbl = bonjour()
print(varbl)
```


Oui : elles passent en fait toutes la valeur `None` : un objet spécial de Python qui signifie
littéralement « rien », ce qui n'est donc pas très utile.


Comment on fait alors ? On leur donne une **valeur de retour** avec le mot-clé `return` :

```python
def renvoi():
    reponse = "Salut"
    return reponse

varbl = renvoi()
```

Vous voyez la différence ? On a rien affiché ici. Par contre :

```python
print(varbl)
```

on a bien **renvoyé** une valeur.


Renvoyer une valeur, c'est surtout utile quand on a des paramètres, sinon on renvoie toujours la
même chose, pas vraiment la peine de faire une fonction, une variable suffirait.

```python
def somme(a, b):
    res = a+b
    return res

s = somme(5, 10)
print(s)
```

```python
def somme(a, b):
    return a+b

s = somme(5, 10)
print(s)
```

Et comme d'habitude, vous pouvez mettre un appel de fonction partout où vous pouvez écrire une
valeur littérale :

```python
print(somme(12, 75))
```

```python
print(somme("ha", "ha"))
```

**Attention** maintenant à bien faire la différence :


Cette fonction **affiche** quelque chose et ne **renvoie** rien (ou `None`)

```python
def affiche(arg):
    print("Mon argument est " + arg)

ret = affiche("thing")
print("ret vaut:", ret)
```

Celle-ci n'**affiche** rien et **renvoie** quelque chose

```python
def renvoie(arg):
    return "Mon argument est " + arg

ret = renvoie("thing") # Ceci n'affiche rien
print("ret vaut:", ret)
```

Celle-ci fait les deux

```python
def porquenolosdos(arg):
    print("Voici mon argument: " + arg)
    return "Mon argument est " + arg

ret = porquenolosdos("thing")
print(ret)
```

## ↩️ Entraînements ↩️

1\. Écrire une fonction sans arguments, qui renvoie le nombre `2713`

2\. Écrire une fonction qui accepte un argument et renvoie son double

3\. Écrire une fonction qui accepte deux arguments, affiche la valeur du premier et renvoie le
triple du deuxième

4\. Écrire une fonction qui accepte un argument, supposé être une liste, qui affiche le premier
élément de cette liste et renvoie la valeur du dernier.

5\. Écrire une fonction qui accepte un argument, supposé être une liste de chaînes de caractères,
qui renvoie la plus longue chaîne de la liste.


```python

```

<!-- #region slideshow={"slide_type": "slide"} -->
<details>
<summary>Solutions</summary>

1\.

```python
def mon_nombre_préféré():
    return 2713
```

```python
a = mon_nombre_préféré()
print(a)
```

2\.

```python
def double(nombre):
    d = 2*nombre
    return d
```

```python
dbl = double(5)
print(dbl)
```

3\.

```python
def trois(a, b):
    print(a)
    return 3*b
```

```python
ret = trois(7, 9)
```

```python
print(ret)
```

```python
l=[ret, 2, ret]
print(l)
```

```python
def quatre(lst):
    print(lst[0])
    i = lst[-1]
    return i
```

```python
c = quatre(["ab", "c", 2713])
```

```python
print(c)
```

```python
print(c)
```

```python
def cinq(lst):
    chaine_max = ""
    for chaine in lst:
        if len(chaine) > len(chaine_max):
            chaine_max = chaine
    return chaine_max
```

```python
plus_longue = cinq(["abc", "a", "hallo", "truc", "oxygène", "p"])
print(plus_longue)
```

</details>

<!-- #endregion -->


## Lire des fichiers

En situation réelle, les programmes manipulent souvent des fichiers :

- Pour y lire des données ou des configurations.
- Pour y écrire le résultat d'opérations afin de les sauvegarder.
- …

En fait, un des usages les plus courants de Python, surtout comme outil pour les LSHS, c'est la
manipulation de fichiers :

- Pour établir des listes de vocabulaire dans des corpus.
- Pour traiter des enregistrements sonores.
- Pour manipuler des données sous forme tabulaire, comme des résultats d'expériences.

On va donc maintenant voir comment on peut, en Python, manipuler des fichiers.

### Bases

Dans le même dossier que ce notebook, il y a un fichier : [`ada.txt`](ada.txt) qui va servir
d'exemple pour cette partie.

<!-- beginregion -->

En Python, pour ouvrir un fichier, que ce soit pour lire son contenu, pour le modifier, ou pour
créer un nouveau fichier, on utilise la syntaxe suivante :

```python
with open(chemin_du_fichier, mode) as nom_du_flux:
    # du code qui utilise le nom du flux pour le manipuler
```
<!-- endregion -->

On fait bien la différence entre

- Le **chemin** du fichier `chemin_du_fichier`
  - Indique la position du fichier sur votre machine.
  - Une chaîne de caractères
  - `/home/lgrobol/monsupercorpus.txt`, ou
    `C:\Users\Morgan\Documents\monsupercorpus.txt` (chemin **absolu**).
  - `ada.txt` ou `sous_dossier/ada.txt` (chemin **relatif** au notebook ou au script en cours)
- Le **flux** `nom_du_flux`, qui est un objet Python qui permet d'interagir avec le fichier tant
  qu'il est ouvert.

Enfin `mode` est une chaîne de caractères qui indique qu'on veut faire avec le fichier. Les options
courantes sont :

- `"r"` (*read*) pour ouvrir le fichier en lecture, ce qui permet d'accéder à son contenu.
- `"w"` (*write*) pour ouvrir le fichier en écriture, ce qui efface son contenu et permet d'y écrire
  de nouvelles données.
- `"a"` (*append*) pour ouvrir le fichier en ajout, ce qui préserve son contenu et permet d'ajouter
  des lignes à la fin.

Pour `"w"` et `"a"`, le fichier ciblé n'existe pas, il est créé (vide). Pour `"r"`, c'est une
erreur.

Il y a d'autres options possibles, vous trouverez la liste dans la [doc]().

```python
with open("ada.txt", "r") as flux_lecture:
    print(type(flux_lecture))
```

```python
with open("sous_dossier/maria.txt", "r") as flux_lecture:
    print(type(flux_lecture))
```

Les flux vers des fichiers ouverts en lecture sont des itérables : on peut les parcourir à l'aide de
la boucle de parcours `for`. Les éléments de l'itérable sont les lignes du fichier sous forme de
chaînes de caractères.

```python
with open("ada.txt", "r") as xulf:
    for l in xulf:
        print(l)
```

Attention, il y a un truc pas forcément intuitif avec ces lignes :

```python
with open("ada.txt", "r") as flux:
    lst = []
    for ligne in flux:
        lst.append(ligne)
lst
```

Vous voyez ?

---

Les lignes sont toutes terminées par le caractère `"\n"` « fin de ligne ».

En général, on ne veut pas de ce caractère quand on traite les informations dans un fichier. On
l'enlève donc avec la méthode de chaînes de caractères `strip()`, qui supprime les espaces (y
compris les fins de lignes) en début et fin de chaîne.

```python
s ="    abzdfzef   "
print(s)
print(s.strip())
```

```python
with open("ada.txt", "r") as flux:
    lst = []
    for ligne in flux:
        lst.append(ligne.strip())
print(lst)
```

### Lecture manuelle

Si vous préférez récupérer les lignes une à une manuellement plutôt que d'utiliser une boucle, vous
pouvez utiliser la méthode `readline()`.

```python
with open("ada.txt", "r") as in_stream:
    line = in_stream.readline()
    print(line.strip())
    line = in_stream.readline()
    print(line.strip())
```

Vous pouvez aussi récupérer en un coup tout le contenu du fichier dans une variable avec `read`

```python
with open("ada.txt", "r") as stream:
    everythingg = stream.read()
    print(everythingg)
```

### Portée

Attention, le fichier n'est accessible que dans le bloc introduit par `with open(fichier) as flux:`.
Quand vous sortez du bloc, la variable `flux` n'est plus définie :

```python tag=["raises-exception"]
with open("ada.txt", 'r') as flux:
    line = flux.readline().strip()
    print(line)
    
line = flux.readline()
```

En revanche, si vous avez stocké son contenu (ou une partie) dans une variable, ces valeurs restent
accessibles (l'affectation les a copiées en mémoire) :

```python
with open("ada.txt", 'r') as flux:
    line = flux.readline().strip()
    print(line)

print(line)
```

### 🍞 Entraînement 🍞

1\. Afficher ligne par ligne le contenu du fichier
[`sous_dossier/maria.txt`](sous_dossier/maria.txt).

2\. Afficher la longueur en nombre de caractères de chacune des lignes du fichier
[`ada.txt`](ada.txt).

### Solution

1\.

```python
with open("sous_dossier/maria.txt") as flux_lecture:
    for line in flux_lecture:
        print(line)
```

2\.

```python
with open("sous_dossier/maria.txt") as flux_lecture:
    for line in flux_lecture:
        print(len(line))
```

## Écrire dans des fichiers

Comme on l'a dit précédemment, le mode `"w"` ouvre les fichiers en écriture, en les créant si
besoin.

```python
with open("apprendre_a_programmer.txt", "w") as out_stream:
    out_stream.write("Clairement, le meilleur cours de la licence SDL.")
```

Allez maintenant voir [`apprendre_a_programmer.txt`](apprendre_a_programmer.txt).

Attention : `open()` peut créer pour vous un fichier qui n'existerait pas encore, mais pas un
dossier :

```python tags=["raises-exception"]
with open("bidule/apprendre_a_programmer.txt", "w") as out_stream:
    out_stream.write("Clairement, le meilleur cours de la licence SDL.")
```

Attention aussi : si vous voulez des retours à la ligne, il faudra les donner explicitement :

```python
with open("apprendre_a_programmer.txt", "w") as out_stream:
    out_stream.write("Clairement, le meilleur cours de la licence SDL.")
    out_stream.write("Dans trois semaines, y en aura plus.")

with open("apprendre_a_programmer.txt", "r") as in_stream:
    print(in_stream.read())
```

```python
with open("apprendre_a_programmer.txt", "w") as out_stream:
    out_stream.write("Clairement, le meilleur cours de la licence SDL.\n")
    out_stream.write("Dans trois semaines, y en aura plus.")
    out_stream.write("\n")

with open("apprendre_a_programmer.txt", "r") as in_stream:
    print(in_stream.read())
```

De plus, `write` n'est pas aussi aimable que `print`, et ne fera pas de conversion pour vous : il
écrit des chaînes de caractères et c'est tout.

```python tag=["raises-exception"]
with open("apprendre_a_programmer.txt", "w") as out_stream:
    out_stream.write(131)
```

Si vous voulez faire ça, il faut convertir explicitement avec `str` :

```python tag=["raises-exception"]
with open("apprendre_a_programmer.txt", "w") as out_stream:
    out_stream.write(str(131))
```

L'autre option, c'est cette technique secrète et mal vue :

```python
with open("apprendre_a_programmer.txt", "w") as out_stream:
    print("Clairement, le meilleur cours de la licence SDL.", file=out_stream)
    print("Dans trois semaines, y en aura plus.", file=out_stream)
    print(13, file=out_stream)

with open("apprendre_a_programmer.txt", "r") as in_stream:
    print(in_stream.read())
```

## ✍🏻 Entraînement ✍🏻

1\. Écrire un programme qui copie dans `sortie.txt` le contenu de `ada.txt`

2\. Écrire une fonction `copie`, avec comme argument deux chaînes de caractères `chemin_entree` et
`chemin_sortie`, qui copie dans le fichier dont le chemin est `chemin_sortie` le contenu du fichier
dont le chemin est `chemin_entree`.

<!-- #region slideshow={"slide_type": "slide"} -->
<details>
<summary>Solutions</summary>

1\.

```python
with open("ada.txt") as flux_lecture:
    with open("sortie.txt", "w") as flux_ecriture:
        for ligne in flux_lecture:
            flux_ecriture.write(ligne)
```

2\.

```python
def copie(chemin_entree, chemin_sortie):
    with open(chemin_entree) as flux_lecture:
        with open(chemin_sortie, "w") as flux_ecriture:
            for ligne in flux_lecture:
                flux_ecriture.write(ligne)
```
</details>

<!-- #endregion -->
