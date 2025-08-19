import re


def decode(a):
    a[0] = a[0]
    a[1] = list(map(int, a[1].split('#')[::-1]))
    for i in a[1]:
        a[0] = str(int(a[0], i))
    x = ""
    a[0] = str(a[0])
    for i in range(0, len(a[0]), 3):
        b = a[0][i:i+3]
        x  += chr(int(b))
    return x


def up(string, system):
    system -= 0
    alphabet = list('0123456789abcdefghijklmnopqrstuvwxyz')
    a, b = '', string
    while(b > 0):
        x = int(b) % system
        a += alphabet[x]
        b = b // system
    return a[::-1]

  
def encode(a):
    a[0] = list(map(str, list(a[0].encode("utf-8"))))
    for i in range(len(a[0])):
        a[0][i] = "0" * (3 - len(a[0][i])) + a[0][i]
    a[0] = "".join(a[0])
    print(a[0])
    a[1] = list(map(int, a[1].split('#')))
    for i in a[1]:
        a[0] = up(int(a[0]), i)
    return a[0]

    
a = input("str: ")
b = input("key: ")
m = input("mod('e' or 'd'): ")
if m == "e":
    print(encode([a, b]))
    print(b)
elif m == 'd':
    print(decode([a, b]))
input()
