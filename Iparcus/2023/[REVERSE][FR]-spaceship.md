# Challenge
Catégorie : Reverse
Nom du chall : Spaceship
Outil utilisé : Ghidra

*Le nom des variables locals peuvent différer d'une décompilation à l'autre mais le principe reste le même*

# Analyse
On peut directement aller voir dans la function `main`. Dedans on retrouve différents strings en hexa.<br/>
On trouve une chaîne de caractère `You Win !` donc on sait ce qu'on doit atteindre.
![](/images/spaceship1.png)

# Solution
Donc on sait ce qu'on doit avoir `iVar1 == 0` donc il faut que la comparaison faite à la ligne `iVar1 = strcmp((char *)&local_16,local_48);` soit validé.<br/>
`local_48` est notre entrée utilisateur, on le reconnait avec `scanf` : `__isoc99_scanf(&DAT_00102bd9,local_48);`.<br/>
Parfait maitenant on doit trouver la valeur de `local_16`. En remontant on retrouve bien la valeur de la variable `0x6c62616972617624` soit `$variabl`.<br/>
On rentre le mot de passe (en rajoutant un `e`) trouvé et hop c'est flag

# Solution 2
Dans le même screen en haut on retrouve aussi ce qui va être affiché à l'écran :<br/>
```
printf((char *)&local_50);  // sucraPI
printf((char *)&local_9a);  // {
putchar(0x5f);              // _
printf((char *)&local_aa);  // €$r3/|3R
printf("_N0t_Th@t_|-|@rD");
putchar(0x5f);              // _
printf((char *)&local_b7);  // }
```

On remet les strings dans le bon sens `IParcus{_R3|/3r$€_N0t_Th@t_|-|@rD_}` et on trouve le flag.
