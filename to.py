import math, re

def int_to_dec(n):
    n = bin(n)[2:].zfill(8*2)
    b = re.findall('\d{8}', n)
    c = ['0b' + i for i in b]
    return [int(i, 2) for i in c]
print(int_to_dec(103*37))