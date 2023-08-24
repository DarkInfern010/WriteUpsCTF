import base64

f = open("data.txt", "r", encoding="utf-8")
f2 = open("data2.txt", "w")
for x in f:
    if "0x" in x.strip():
        f2.write(x.strip().split('exit')[0] + " exit(" + str(int(x.strip().split("exit(")[1][:-2], 16)) + ");" + "\n")
    else:
        f2.write(x.strip() + "\n")
f2.close()


import collections
f = open("data2.txt", "r", encoding="utf-8")
dico = {}
for x in f:
    dico[int(x.strip().split('exit(')[1][:-2])] = x.strip().split("!= '")[1].split("')")[0]

od = collections.OrderedDict(sorted(dico.items()))

flag = ""
for k,v in od.items():
    flag += v
print(flag)

for i in range(10):
    flag = base64.b64decode(flag)
    print(flag)