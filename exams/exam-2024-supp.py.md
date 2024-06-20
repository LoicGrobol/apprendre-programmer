---
jupyter:
  jupytext:
    custom_cell_magics: kql
    formats: ipynb,md
    split_at_heading: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- LTeX: language=fr -->
Examen Apprendre à programmer 2024 (rattrapage)
===============================================

## ATTENTION

<small>Quelques rappels bien voyants, pour ne pas que vous les manquiez</small>

- **PENSEZ À TESTER VOTRE NOTEBOOK/SCRIPT EN L'EXÉCUTANT AVANT DE LE RENDRE**
  - si vous travaillez dans un notebook, vérifiez que ça marche aussi si vous faites « *restart
    kernel and run all* »
- **SAUVEGARDEZ RÉGULIÈREMENT VOTRE TRAVAIL**

## Consignes

Ce partiel se présente comme une série de questions indépendantes. Pour chacune d'entre elles, vous
devrez écrire un programme en Python. Vous avez plusieurs possibilités pour travailler :

<!-- #region -->
- Répondre directement dans ce notebook, sur le modèle des exercices que vous avez faits pendant le
  semestre.
- Vous pouvez écrire un script `.py`, soit dans un éditeur local (comme Thonny ou vscode), soit en utilisant
  <https://repl.it>. Dans ce cas, mettez toutes les programmes-réponses les uns à la suite des
  autres en mettant les numéros de questions en commentaire comme ceci :

```python
# Question 1
< Votre code pour répondre à la question 1 >

# Question 2
< Votre code pour répondre à la question 2 >

…
```
<!-- #endregion -->

- Enfin, si vous ne pouvez pas, pour une raison ou une autre, travailler sur machine, vous pouvez
  également rendre vos réponses sur papier. On aura dans ce cas un peu plus d'indulgence à l'égard
  des coquilles.

À part si vous composez sur papier, votre rendu (notebook au format `ipynb` ou script `py`) à
déposer sur [Cours en Ligne](https://coursenligne.parisnanterre.fr/course) (suivre le lien), ou en
dernier recours à `<lgrobol@parisnanterre.fr>`.

**Tous les documents, papiers et numériques sont autorisés.**

**Toute communication est interdite pendant la durée de l'examen.**

Vous avez deux heures. Bon courage.

## Questions

1\. Écrire un programme qui affiche la chaîne de caractères `Be not afraid!`.

```python
# Codez ici
```

2\. Construire et afficher une chaîne de caractères contenant `keep cool` suivie de $128$ fois `☃️`.

```python
# Codez ici
```

3\. Écrire un programme qui calcule et affiche le résultat du calcul suivant $\frac{3*12+2}{3}$.

```python
# Codez ici
```

4\. Créer une variable `opinion` contenant la chaîne de caractères `AUCUNE RÉVOLUTION N’AURA LIEU SANS
CHANGEMENT RADICAL DE L'IDÉE QU'ON SE FAIT DU RÉEL`, puis, à l'aide d'une opération sur les chaînes
de caractères, mettez le contenu de `opinion` en minuscules et stockez cette nouvelle chaîne dans une
variable `y`. Enfin, affichez le contenu de `y`.

```python
# Codez ici
```

5\. Écrire un programme qui demande la saisie d'une chaîne de caractères, puis qui affiche
`quel enfer` si cette chaîne contient le mot « travail » et affiche `super` dans le cas contraire.

```python
# Codez ici
```

6\. Écrire un programme qui demande la saisie d'un nombre, puis qui affiche ce nombre multiplié par $6$.

```python
# Codez ici
```

7\.

7.1 En utilisant uniquement les chaînes de caractères déjà définies (pas forcément toutes) dans la
cellule-ci dessous, modifiez cette cellule pour afficher exactement `l’environnement c’est aussi ce que créent
les sociétés`.

```python
lst = ["l'", "c'est aussi ce que", "créent", "les", "sociétés",  "environnement", " "]
# Codez ici
```

7.2 Même question avec la liste suivante

```python
lst = ["l'", [["c'est aussi ce que"]], "créent", "les", ["sociétés",  "environnement"], " "]
# Codez ici
```

8\. Afficher sur des lignes séparées les doubles des nombres de la liste suivante, en écrivant une
seule fois `print` et une fois `**`.

```python
lst = [21, 1, 1901, 2, 7, -16]
# Codez ici
```

9\. Écrire un programme qui compte le nombre de mots finissant par `e` dans la
liste suivante, puis affiche ce nombre

```python
text = [ "once", "a", "person", "acknowledges", "that", "they", "possess", "some", "form", "of", 
"privilege", ",", "they", "are", "more", "likely", "to", "accept", "the", "reality", "that", "they", 
"are", "not", "in", "any", "way", "objective", "about", "the", "form", "of", "marginalization", 
"in", "question"]
# Codez ici
```

10\. Écrire un programme qui compte le nombre de consonnes dans le texte ci-dessous, puis affiche ce
nombre

```python
text = [ "once", "a", "person", "acknowledges", "that", "they", "possess", "some", "form", "of", 
"privilege", ",", "they", "are", "more", "likely", "to", "accept", "the", "reality", "that", "they", 
"are", "not", "in", "any", "way", "objective", "about", "the", "form", "of", "marginalization", 
"in", "question"]
voyelles = ["a", "e", "i", "o", "u", "y"]
# Codez ici
```

11\. Écrire un programme qui stocke dans une liste tous les mots finissant par une voyelle dans le
texte ci-dessous, puis affiche cette liste.

```python
text = [ "once", "a", "person", "acknowledges", "that", "they", "possess", "some", "form", "of", 
"privilege", ",", "they", "are", "more", "likely", "to", "accept", "the", "reality", "that", "they", 
"are", "not", "in", "any", "way", "objective", "about", "the", "form", "of", "marginalization", 
"in", "question"]
voyelles = ["a", "e", "i", "o", "u", "y"]
# Codez ici
```

12\. Écrire une fonction nommée `suzie` qui affiche la chaîne de caractères `Dressed to kill`.
Appeler cette fonction trois fois.

```python
# Coder ici
```

13\. Écrire une fonction nommée `ma_hini` acceptant un argument `n`, supposé être un nombre entier
positif. Cette fonction doit afficher le `n`-ième mot du texte suivant si un tel mot existe et
afficher `ERREUR` si `n` est trop grand ou trop petit. Appeler cette fonction avec les valeurs `0`,
`-1`, `15` et `2024` pour `n`.

```python
text = [ "once", "a", "person", "acknowledges", "that", "they", "possess", "some", "form", "of", 
"privilege", ",", "they", "are", "more", "likely", "to", "accept", "the", "reality", "that", "they", 
"are", "not", "in", "any", "way", "objective", "about", "the", "form", "of", "marginalization", 
"in", "question"]
# Codez ici
```

14\. Écrire une fonction `ma_fonction` à deux arguments `a` et `z`, qui affiche `a` et renvoie
`a-z`. Appeler cette fonction pour `a=15` et `z=12` et pour `a="Bonjour"` et `z=[1,2,3]`.

```python
# Coder ici
```

15\. Écrire une fonction `ta_fonction` à un argument `lst`, supposé être une liste de chaînes de
caractères, qui renvoie la plus longue chaîne de cette liste. Appeler cette fonction avec comme
valeur pour `lst` la liste `machin` suivante.

```python
machin = [ "once", "a", "person", "acknowledges", "that", "they", "possess", "some", "form", "of", 
"privilege", ",", "they", "are", "more", "likely", "to", "accept", "the", "reality", "that", "they", 
"are", "not", "in", "any", "way", "objective", "about", "the", "form", "of", "marginalization", 
"in", "question"]
# Coder ici
```
