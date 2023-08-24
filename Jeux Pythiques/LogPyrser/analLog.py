## Récupération des données interessantes
ry = open("./rockyou.txt", "r", encoding="latin1")
ryL = ry.readlines()
ryLs = [line.strip().replace(" ", "%20") for line in ryL]

file = open('apache_log.log', 'r')
lines = file.readlines()

for line in lines:
    data = line.strip().split("GET")[1].split("HTTP")[0].strip()[1:]
    if data not in ryLs:
        print(data)

## "Bruteforce" de base64
import base64
import itertools

data = [
"jAyM30=",
"Wx5c2lz",
"G9nX2Fu",
"GlxdWVf",
"jN7cHl0",
"iBKUDIw",
"GZsYWcg",
"WNpIGxl",
"2UuIFZv",
"GFsbGVu",
"SBsZSBj",
"HJldXNz",
"HR1IGFz",
"nJhdm8s"
]

for i in data:
    for j in data:
        for k in data:
            for l in data:
                try:
                    print(base64.b64decode(i+j+k+l))
                except:
                    pass
