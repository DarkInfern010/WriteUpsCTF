# Challenge
Catégorie : Reverse
Nom du chall : Sloubi
Outil utilisé : Ghidra

*Le nom des variables locals peuvent différer d'une décompilation à l'autre mais le principe reste le même*

# Analyse
En ouvrant le fichier dans ghidra on peut comprendre que le code utilisé est du C++, on le remarque au vue des strings `std::basic_ostream<char,std::char_traits<char>>` par exemple.<br/>
Allons directement dans la fonction appelé main.<br/>
Ce qui vas nous interesser dans le programme est la ligne `local_c = strcmp(local_118,local_148);` et ce qui va suivre après le `if`.<br/>
En lisant le code, on retrouve cette ligne : `std::operator>>((basic_istream *)std::cin,local_118);` qui nous permet de comprendre avec `cin` que l'entrée utilisateur sera stockée dans `local_118`.<br/>
Donc le but est d'avoir la même entrée que la valeur de `local_148`<br/>

# Solution
On commence a traduire les variables hexa en mettant des commentaires dans ghidra :
![](/images/sloubi1.png)

En suite on récupère les lignes de code permettant de former la string `local_148` :
```
strcpy(local_148,(char *)&local_12e);
strcat(local_148,(char *)&local_13d);
strcat(local_148,(char *)&local_11b);
strcat(local_148,(char *)&local_139);
```

Très bien plus qu'a écrire tout ça autrement :
```
local_148 = "ols";
local_148 += "ibu";
local_148 += "3_";
local_148 += "84";

local_148 = "843_ibuols";
```

On inverse les données : `sloubi_348`

Parfait on a notre entrée, on test et on flag
