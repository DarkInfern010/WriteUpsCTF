password = input()
spec = "!@#$&*"

if len(password) >= 8:
    if len([i for i in password if i.isdigit()]) > 0:
        if len([i for i in password if i.isupper()]) > 0:
            if len([i for i in password if i.islower()]) > 0:
                if len([i for i in password if i in spec]) > 0:
                    print("Le mot de passe est robuste")
                else:
                    print("Le mot de passe n'a pas de caractere special valide")
            else:
                print("Le mot de passe n'a pas de minuscule")
        else:
            print("Le mot de passe n'a pas de majuscule")
    else:
        print("Le mot de passe n'a pas de chiffre")
else:
    print("Le mot de passe n'est pas assez long")