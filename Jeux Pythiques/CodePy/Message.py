#!/usr/bin/python2

import sys

def Erreur():
    print "Vous n'avez aucun message"
    sys.exit(0)

print "Bienvenue, que voulez-vous ? \n"

try:
    p = input("Dire la phrase magique : \n")
except:
    Erreur()


with open(".passwd") as f:
    Mot_De_Passe = f.readline().strip()
    print "Mot de passe correct, voici le message secret"
