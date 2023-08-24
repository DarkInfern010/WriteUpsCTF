# Enoncé
## Partie 1
Comment faire: https://jeuxpythiques.woody.sh/fichiers/README.pdf

Auteur: Klemou (plaignez vous à lui svp)

nc jeuxpythiques.woody.sh 8009

## Partie 2
Comment faire: https://jeuxpythiques.woody.sh/fichiers/README.pdf

Auteur: Klemou (plaignez vous à lui svp)

nc jeuxpythiques.woody.sh 8010

# Solution
Un nombre de matrices carré de taille N^2 nous sommes passées au fur et à mesure, de petites matrices de taille 4 jusqu'à des matrices de taille 1024.
## Partie 1
Dans cette première partie, on nous les donne une matrice [[1,2][3,4]] et on doit ressortie leurs valeurs en lisant la matrice en "Z" 1,2,3,4. Pour les autres matrices plus grandes, il faut découper en "Z" tant que nous n'avons pas des matrices de taille 2.
Une fois le découpage réalisé on a plus que lire chaque matrice de 2 ligne par ligne et d'envoyer la réponse

*Dans certains cas il faut simplifier, cela veux dire que si une matrice carrée de taille 2 à tout ses coeff à 1 il faut juste renvoyer 1 et non 1,1,1,1*

Ex :
[
[01, 02, 03, 04],
[05, 06, 07, 08],
[09, 10, 11, 12],
[13, 14, 15, 16]
]
On doit déjà découper la matrice de taille 4 en 4 sous-matrice de taille 2 :
[
[1, 2],
[4, 6]
],
[
[3, 4],
[7, 8]
], ...
On obtient à la fin :
1,2,5,6,3,4,7,8,9,10,13,14,11,13,15,16

## Partie 2
Cette partie est l'inverse de la première, on nous donne le résultat et on doit donner la matrice de base. Pour ce faire et en utilisant la logique de la partie 1, on peut créer une matrice de taille N, la traversée en forme de "Z" jusqu'à lire une matrice de taille 2 et insérer les premiers chiffres.

Ex :
1,2,5,6,3,4,7,8,9,10,13,14,11,13,15,16
Matrice Vide:
[
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
]
On parcourt la sous-matrice 1 (Nord-Ouest) pour la remplir.
[
[1,2,0,0],
[5,6,0,0],
[0,0,0,0],
[0,0,0,0],
]
On continue avec le reste des donnes donc 3,4,7,8,9,10,13,14,11,13,15,16
[
[1,2,3,4],
[5,6,7,8],
[0,0,0,0],
[0,0,0,0],
]...

# Flag
## Partie 1
JP2023{J'ai pas d'idée sorry mais va y normalement ca valide}

## Partie 2
JP2023{Send nude at requin_citron@protonmail.com}