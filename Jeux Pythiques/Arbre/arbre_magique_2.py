import math

import numpy as np
from pwn import *

conn = remote("jeuxpythiques.woody.sh", 8010)

def zParcours(matrix, i, j, size, values, index):
    if size == 1:
        matrix[i, j] = values[index]
        return index + 1
    else:
        half_size = size // 2

        index = zParcours(matrix, i, j, half_size, values, index)
        index = zParcours(matrix, i, j + half_size, half_size, values, index)
        index = zParcours(matrix, i + half_size, j, half_size, values, index)
        index = zParcours(matrix, i + half_size, j + half_size, half_size, values, index)

        return index

def matrixToList(matrix):
    return str([[matrix[i, j] for j in range(matrix.shape[1])] for i in range(matrix.shape[0])]).replace(' ','')

for tour in range(12):
    print('Tour :', tour)
    data = conn.recv().decode().split("\n")[0]
    print(data)
    
    n = int(math.sqrt(len(data.split(','))))
    
    matrix = np.zeros((n, n), dtype=int)
    values = [int(i) for i in data.split(',')]

    zParcours(matrix, 0, 0, n, values, 0)
    conn.sendline(matrixToList(matrix))

for tour in range(13, 100):
    print('Tour :', tour)
    data = conn.recvline().decode().strip()
    print(data[:100])
    print(data[-100:])
    
    n = int(math.sqrt(len(data.split(','))))
    
    matrix = np.zeros((n, n), dtype=int)
    values = [int(i) for i in data.split(',')]

    zParcours(matrix, 0, 0, n, values, 0)
    conn.sendline(matrixToList(matrix).encode())
    conn.recv()