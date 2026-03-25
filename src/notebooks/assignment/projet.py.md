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

# Projet Apprendre à programmer

## Pratique

- Projet à rendre le 11 mai 2026 *au plus tard*
  - Si vous avez un problème, si vous êtes en retard, contactez-moi le plus tôt possible pour ce
    qu'il est possible d'arranger.
- Projet individuel ou par groupe de deux personnes.
  - S'il y a un problème — quel qu'il soit — dans votre groupe, n'hésitez pas à m'en parler.
- Rendu via la page Cours en Ligne du cours, ou en cas de problème par email à
  [`lgrobol@parisnanterre.fr`](mailto:lgrobol@parisnanterre.fr).

## Principe

Pour ce projet, vous allez réaliser un clone du jeu
[Wordle](https://www.nytimes.com/games/wordle/index.html) (voir aussi
[Le Mot](https://wordle.louan.me/), une version en français). Le principe de ce jeu est le suivant :

- Vous avez six essais pour trouver un mot secret de six lettres.
- Le mot secret est un mot courant, qui n'est pas un nom propre, choisi au hasard dans un lexique
  prédéterminé.
- À chaque essai, vous proposez un mot, qui doit être dans un lexique prédéterminé. Proposer un mot
  qui n'est pas dans ce lexique ne compte pas comme un essai manqué.
- Si le mot que vous avez proposé est le bon, vous avez gagné.
  - La comparaison ne tient pas compte de la casse (`a` et `A` sont considérés somme la même lettre
    par exemple)
- Sinon, le jeu vous indique parmi les lettres du mot proposé lesquelles sont également présentes
  dans le mot secret et pour chacune de celle-ci, si elle se trouve à la même place dans le mot
  proposé et dans le mot secret.
- Si au bout de six essais, vous n'avez pas trouvé le mot proposé, vous avez perdu.

L'objectif de ce projet est de produire un script Python qui implémente les règles ci-dessus.

Voici à quoi pourrait ressembler une partie où le mot à trouver était *attela*. Les saisies sont
indiquées par `>`, une lettre bien placée est indiquée par `o`, une lettre présente, mais mal placée
par `+` et une lettre fausse par `×` :

```text
Deviner un mot de 6 lettres
Il reste 6 essais
> trahir
+×+×××
Il reste 5 essais
> paysan
+××+×
Il reste 4 essais
atelle n'est pas un mot autorisé
Il reste 4 essais
> abaque
o×+××+
Il reste 3 essais
> attire
ooo××+
Il reste 2 essais
> attela
oooooo
Bravo !
```

## Consignes

Pour ce projet, vous devrez donc rendre un script en Python qui implémente les règles ci-dessus.
Vous pouvez le faire soit complètement par vos propres moyens, soit en répondant aux questions
suivantes, voire en faisant un peu des deux. Pour aller plus loin, vous pouvez en plus essayer
d'implémenter les [règles facultatives](#regles-facultatives).

Vous pouvez travailler directement dans ce notebook pour répondre aux questions, **mais** je vous
recommande plutôt d'écrire un script en Python dans un environnement de développement sur votre
machine (comme Thonny). Dans ce cas, écrivez simplement un script `.py` qui démarre le jeu quand on
le lance. Vous pouvez indiquer les parties du code qui correspondent aux questions en écrivant des
commentaires `#`.

### 1. Comparer une proposition au mot secret

Écrire une fonction `comparer`, avec comme arguments deux chaînes de caractères, `proposition` et
`secret`. On suppose qu'elles sont toutes les deux uniquement composées de lettres minuscules et
sont de même longueur.

`comparer` doit renvoyer une chaîne de caractère de la même longueur que `proposition` et `secret`,
chacun des caractères indiquant si le caractère correspondant dans `proposition` est bien placé
(`o`), bien trouvé, mais mal placé (`+`), ou incorrect (`x`).

Exemples :

- `comparer("manger", "mordue")` renvoie `'oxxx++'`
- `comparer("chaton", "oberon")` renvoie `'xxxxoo`
- `comparer("tortue", "crepes")` renvoie `'xx+xx+`

Pour vous aider : un rappel sur deux façons de construire des chaînes de caractères

```python
s = "abc"
print(s + "d")
```

```python
l = ["a", "b", "c", "d"]
print(str.join("", l))
```

```python

```

### 2. Un tour de jeu

Écrire une fonction `tour`, avec comme argument `secret`, une chaîne de caractères et `lexique`, une
liste de chaînes de caractères. `tour` doit

- Demander la saisie d'un mot, qui sera mis en minuscules et stocké dans une variable `proposition`
- Si `proposition` n'est pas dans `lexique`, redemander une nouvelle saisie. Continuer jusqu'à ce
  que `proposition` soit dans `lexique`. Là aussi, mettez bien cette saisie en minuscules.
- Agir en fonction de `proposition`
  - Si `proposition` est égal à `secret`, renvoyer `True`.
  - Sinon, afficher le résultat de `comparer(proposition, secret)` et renvoyer `False`.

Pensez à tester votre fonction, par exemple avec `"caisse"` pour `secret` et
`lexique = ["caisse", "sieges", "bureau", "tables", "canapé"]`. Pour le jeu final, on utilisera un
vrai lexique.

**Indice** : rappelez-vous que la boucle conditionnelle `while` existe.

```python

```

```python
tour("caisse", ["caisse", "sieges", "bureau", "tables", "canapé"])
```

### 3. La boucle principale

Écrire une fonction `partie`, avec comme argument `lexique`, une liste de chaînes de caractères.
`partie` doit

- Choisir au hasard un mot dans `lexique` et le stocker dans une variable `secret`.
- Appeler plusieurs fois `tour` :
  - Si un appel à `tour` renvoie `True` (donc si le mot secret a été trouvé), afficher un message de
    félicitation et s'arrêter.
  - Si au bout de six tours la solution n'a pas été trouvé, afficher un message qui indique que la
    partie est perdu et s'arrêter.
- Après chaque tour, afficher le nombre d'essais restants.

Pensez à tester votre fonction, par exemple avec
`lexique = ["caisse", "sieges", "bureau", "tables", "canapé"]`.

**Indices** :

- Si **dans un premier temps**, vous ne trouvez pas comment choisir un mot au hasard, prenez
  simplement le premier, afin de ne pas rester bloqué⋅e sur ce point (mais revenez-y).
- La fonction `random.choice` qu'on a vue dans le cours peut vous aider.

```python

```

```python
partie(["caisse", "sieges", "bureau", "tables", "canapé"])
```

### 4. Importer un lexique

Écrire une fonction `lire_lexique`, avec comme argument un chemin vers un fichier. On suppose que le
fichier en question existe et est un fichier texte qui contient une liste de mot, chaque mot étant
sur une ligne. `lire_lexique` doit ouvrir ce fichier en mode lecture et lire son contenu afin de
renvoyer une liste `lexique`, qui contiendra les mots autorisés pour le jeu.

Pour tester, vous pouvez utiliser le fichier [`lexique.txt`](lexique.txt), qui se trouve dans le
même dossier que ce notebook et que vous pouvez télécharger sur votre machine en suivant le lien
précédent.

Attention à bien retirer les caractères de fin de ligne `"\n"`.

```python

```

```python
lire_lexique("lexique.txt")
```

### 5. Tout mettre ensemble

Vous avez maintenant tout ce qu'il vous faut pour écrire un programme qui charge un lexique depuis
un fichier prédéterminé et fait jouer une partie.

```python

```

## Règles facultatives

Les règles suivantes, qui sont présentes dans la plupart des versions existantes, sont facultatives.
Assurez-vous d'avoir une version qui implémente les règles de base avant de vous y attaquer.

- Le mot secret est choisi dans un lexique beaucoup plus petit que celui des mots autorisés et qui
  ne contient que des mots très fréquents.

  - Vous pouvez trouver par exemple sur <http://www.lexique.org> des lexiques du français avec les
    fréquences d'usages des mots.

- La comparaison entre le mot secret et le mot proposé ne tient compte ni de la casse, ni des
  diacritiques. Ainsi `a` et `A` sont considérés comme la même lettre, et `é` et `e` également.

- On indique les lettres bien trouvées et bien placées dans les mots proposés par un code couleur :

  - Dans la version de base, 🟩 indique une lettre bien placée, 🟨 une lettre présente, mais mal
    placée et ⬛ une lettre fausse.
  - Dans une version adaptée aux personnes daltoniennes, 🟧 indique une lettre bien placée, 🟦 une
    lettre présente, mais mal placée, et ⬛ une lettre fausse.
  - Attention, il se peut que les emojis soient mal affichés dans Thonny.

- En fin de partie, un résumé est affiché, donnant le déroulement de la partie avec les emojis
  précédents, sans révéler le mot secret ou les propositions, afin de pouvoir être partagé sans
  spoiler.

- Le mot secret est déterminé par la date, ainsi on ne peut faire qu'une partie par jour. Attention
  cependant à trouver une détermination qui ait l'air pseudo-aléatoire pour que le jeu soit plus
  agréable. Par exemple, éviter de donner les mots par ordre alphabétique.

- Quand une même lettre apparaît $n$ fois dans le mot proposé et $m$ fois dans le mot secret avec
  $m<n$, elles sont traitées ainsi :

  - Les $k$ occurrences bien placées de cette lettre sont signalés comme telles.
  - Si $n-k>0$, les $n-k$ premières occurrences de cette lettre qui sont mal placées sont signalées
    comme présentes, mais mal placées.
  - Les occurrences restantes sont signalées comme fausses.

  Exemples :

  - Mot secret *avions*, mot proposé *avares* : 🟧🟧⬛⬛⬛🟧
  - Mot secret *marche*, mot proposé *aimant* : 🟦⬛🟦⬛⬛⬛
