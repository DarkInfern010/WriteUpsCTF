def Or(a, b):
    return a | b

def And(a, b):
    return a & b

def Xor(a, b):
    return a ^ b

def Chevalo(a, b):
    return ((a+1)<<4) | ((b-1)>>4)

def Kamion(a, b):
    return (a*2) | (b*3)

from pwn import * 
conn = remote("jeuxpythiques.woody.sh", 8011)

for i in range(100):
    expression = conn.recvline().decode().split(":")[1].split("\n")[0].strip().split("+")[0]
    conn.recv()
    print(i)

    if "open" in expression.lower():
        print(expression)
        print("KO")
    else:
        result = eval(expression)
        print(result)
        conn.sendline(str(result).encode())
print(conn.recv().decode())