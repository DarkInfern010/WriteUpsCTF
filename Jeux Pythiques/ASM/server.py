#!/usr/bin/python3
from pwn import *
import random
import sys
from time import time


context.clear(arch='amd64')

rand = hex(64)

print(f"Here is the rand : {rand} !")

start = time()
#instr = input("what's your new instruction (only add or sub is authorized) ?\n")
instr = "add al, 1"

time_taken = time() - start

if time_taken > 4:
    print("Too slow")
    sys.exit()

if len(instr) >= 14:
    print("Don't try to bypass me :p")
    sys.exit()

check = instr.split(" ")[0]
if check != "add" and check != "sub":
    print("Don't try to bypass me :p")
    sys.exit()

# Xor sur lui même
# push du xor dans rsi
# Depile dans rdx
# /bin/bash dans rdi
# push dans rdi
# mov rsp dans rdi
# mov <hexa> r10
# execute une instruction
# on pousse dans r10
# depile rax

# r10 soit égale à 59, en décimale
# r10 = 40
# add r10, 19

try:
    shellcode = asm(f"""
    xor rsi, rsi;
    push rsi;
    pop rdx;
    push rsi;
    mov rdi, 0x68732f2f6e69622f;
    push rdi;
    mov rdi, rsp;
    mov r10,{rand};
    {instr};
    push r10;
    pop rax;
    syscall;
    """)

    elf = ELF.from_bytes(bytes(shellcode))
    #io = gdb.debug(elf.path)
    io = process(elf.path)

    #io.interactive()
    io.sendline("ls".encode())
except:
    print("Crashing :(, you fail")


