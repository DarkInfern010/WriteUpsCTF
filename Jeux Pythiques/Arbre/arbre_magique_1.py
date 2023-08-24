from rich import inspect
from pwn import *
import ast

conn = remote("jeuxpythiques.woody.sh", 8009)

def calculMatrix(matrix):
    parcours = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or i == len(matrix) - 1 or (i == j):
                parcours.append(matrix[i][j])
    return parcours
#endef

def splitMatrix(matrix):
    n = len(matrix)
    if n == 2:
        return matrix
    else:
        newTaille = n // 2
        newMatrix = []
        for i in range(0, n, newTaille):
            for j in range(0, n, newTaille):
                sousMatrix = []
                for k in range(newTaille):
                    ligne = []
                    for l in range(newTaille):
                        ligne.append(matrix[i+k][j+l])
                    #endfor
                    sousMatrix.append(ligne)
                #endfor
                newMatrix.append(splitMatrix(sousMatrix))
            #endfor
        #endfor
        return newMatrix
#endef

def simply(data):
    simplifie = []
    for i in range(0, len(data), 4):
        group = data[i:i+4]
        if all(x == group[0] for x in group):
            simplifie.append(data[i])
        else:
            simplifie.append(data[i])
            simplifie.append(data[i+1])
            simplifie.append(data[i+2])
            simplifie.append(data[i+3])
    return ",".join(simplifie)
#endef

solved = [
    "1,2,3,4",
    "1,1,1,1",
    "1,2,5,6,3,4,7,8,9,10,13,14,11,12,15,16",
    "1,1,1,1",
    "1,3,1,3,2,4,5,4,5,3,2,3,2",
    "1,1,1,3,1,1,5,5,1,3,1,3,2",
    "6,1,1,5,5,1,3,1,3,2",
    "4,4,4,4",
    '3,4,4,0',
    "7,3,3,9,5,4,4,4,8,4,4,6,1,5,0,2"
]

for i in range(len(solved)):
    data = conn.recv()
    print(data.decode())
    conn.sendline(solved[i].encode())
    print(solved[i])

data = conn.recv()

firstMatrix = []
for i in range(len(data.decode().split("\n")[:-1])):
    firstMatrix.append(ast.literal_eval(data.decode().split("\n")[:-1][i]))

sousMatrixs = splitMatrix(firstMatrix)
parcoursTotal = []
for a in sousMatrixs:
    for b in a:
        for c in b:
            parcoursTotal.append(calculMatrix(c))
conn.sendline(",".join([",".join([str(i) for i in x]) for x in parcoursTotal]).encode())
print(",".join([",".join([str(i) for i in x]) for x in parcoursTotal]))

print(conn.recv())
conn.sendline("1,2,5,6,3,4,7,8,9,10,13,14,11,12,15,16".encode())

for i in range(100):
    firstMatrix = [ast.literal_eval(conn.recvline().decode().strip()) for _ in range(1024)]
    print(firstMatrix)

    conn.recv()
    sousMatrixs = splitMatrix(firstMatrix)

    parcoursTotal = []
    for a in sousMatrixs:
        for b in a:
            for c in b:
                for d in c:
                    for e in d:
                        for f in e:
                            for g in f:
                                for h in g:
                                    for i in h:
                                        parcoursTotal.append(calculMatrix(i))
    #print(parcoursTotal)

    conn.sendline(simply(",".join([",".join([str(i) for i in x]) for x in parcoursTotal]).split(',')).encode())
    print(",".join([",".join([str(i) for i in x]) for x in parcoursTotal]))