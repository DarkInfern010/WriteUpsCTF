# Enoncé
Voici un serveur, votre objectif et de lui répondre de la bonne façon afin d'obtenir un shell ! Bon courage et révisez bien l'ASM ..

Fichier: https://jeuxpythiques.woody.sh/fichiers/server.py

Auteur: Itarow

# Solution
Le code donné en énoncé permet d'exécuter à distance un revershell, cependant on doit faire en sorte que le registre r10 soit égale à 59, 59 étant la représentation de execve lors d'un syscall

On peut soit soustraire soit ajouter un nombre à R10 pour atteindre 59.

# Flag
JP2023{m4gIc_ASM}