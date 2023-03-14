import math
import re
p = 2147483647
a = [0,11, 173, 248]
b = [0, 1, 226, 64]
W = 8
m = round(math.log2(p))
t = round(m/W)
def solve(a, W, p):
    result = []
    m = round(math.log2(p))
    t = round(m/W)
    n = [pow(2, i * W) for i in range(t)]
    for i in n[::-1]:
        result.append(math.floor(a/i))
        a = a % i 
    return result
def int_to_dec(n):
    n = bin(n)[2:].zfill(8*2)
    b = re.findall('\d{8}', n)
    c = ['0b' + i for i in b]
    return [int(i, 2) for i in c]
def interger_multiprecision(a,b,t):
    a.reverse()
    b.reverse()
    c = [0]*8
    for i in range(t):
        c[i] = 0
    for i in range(t):
        U = 0
        for j in range(t):
            p = c[i+j] + a[i]*b[j] + U
            d = int_to_dec(p)
            c[i+j] = d[1]
            U = d[0]
        c[i+t] = U
    return c[::-1]
if __name__ == "__main__":
    print(interger_multiprecision(a,b,t))