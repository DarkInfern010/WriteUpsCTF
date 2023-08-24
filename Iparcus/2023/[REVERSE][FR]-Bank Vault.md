# Challenge
Catégorie : Reverse
Nom du chall : Bank Vault
Outil utilisé : Ghidra

*Le nom des variables locales peuvent différer d'une décompilation à l'autre, mais le principe reste le même*

# Analyse
En ouvrant le fichier dans ghidra on peut comprendre que le code utilisé est du C++, on le remarque au vue des strings `std::basic_ostream<char,std::char_traits<char>>` par exemple.<br/>
On voit les deux entrées utilisateur, une pour le mail `local_238` et une pour le code de la banque `local_438`.<br/>
Il y a une vérification pour le mail et une vérification pour le code de la banque.
Une fonction `vault_login()` est appelée plusieurs fois à différents moments, si on s'y intéresse : <br/>
```
  puts("------------------------");
  puts("|      CODE ERROR      |");
  puts("------------------------");
  exit(0);
```
Donc c'est une fonction a evitée.<br/>
<br/>
*Petit Bonus : pour la vérification du mot de passe de la banque j'ai dû changer le type de la variable. En utilisant Ctrl+L ou Command+L*<br/>
*On passe de `byte local_438 [4]` à `char local_438 [25]` (il suffit de compter dans la vérification du mot de passe, on verra ça après)*


# Solutions
![](/images/bank1.png)
Dans ce bout de code on voit bien les deux entrées ainsi qu'une "vérification" du mail. <br/>
Il faut que la longueur du mail est au moins un caractère. `if (sVar2 <= uVar6) break;` <br/>
Il faut qu'il y est au moins un `@` dans le amil . `if (local_238[local_20] == '@') { local_19 = '\x01'; } local_20 = local_20 + 1;`
<br/>
On sait comment avoir un mail "valide". Ex : `a@b` suffit pour valider le mail.<br/>

Très bien maitenant on peut regarder la vérification du mot de passe : <br/>
![](/images/bank2.png)
Du reste voici le code de base sans le retypage fait lors de l'analyse.<br/>
![](/images/bank3.png)

Alors on connaît la taille du mot de passe `(sVar2 < 0x19)` soit 25. <br/>
Ensuite on a juste à créer un mot de passe, le mot de passe vide est donc sous la forme : `00000-00000-00000-00000` <br/>
Enfin on peut en déduire les code de la bank en suivant les vérifications : `17248-17778-92754-66084`<br/>

Voilà on peut valider le chall en rentrant le code de bank suivant.
