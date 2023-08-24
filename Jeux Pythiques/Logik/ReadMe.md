# Enoncé
Il y a 5 portes logique

[Xor, Or, And, Chevalo, Kamion]
Le ou exclusif logique: Xor
Le ou logique: Or
Le et logique: And
Le chevalo logique: Chevalo
Le kamion logique: Kamion

Chevalo
((r1+1)<<4) ou ((r2-1)>>4)
Kamion
(r1*2) ou (r2*3)

Avec r1 l'opérande de gauche et r2 l'opérande de droite

Auteur: Klémou évidemment

nc jeuxpythiques.woody.sh 8011

# Solution
Le but est de résoudre l'ensemble d'une chaine d'opérateur logique.
Pour ce faire on peut réécrire les fonctions Or,And,... puis faire un eval dessus.

**IL FAUT PRENDRE EN COMPTE QUE KLEMOU A LAISSE UN OPEN**

# Flag
JP2023{j'espère que tu es tomber dans mon piège avec des eval de mort enculé}