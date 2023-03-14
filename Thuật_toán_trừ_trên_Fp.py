import math, re
p = 2147483647
a = [0, 11, 173, 248]
b = [0, 1, 226, 64]
W = 8
m = round(math.log2(p))
t = round(m/W)

def int_to_dec(n):
    n = bin(n)[2:].zfill(8*t)
    b = re.findall('\d{8}', n)
    c = ['0b' + i for i in b]
    return [int(i, 2) for i in c]
def dec_to_int(n):
    n = ''.join([bin(i)[2:].zfill(8) for i in n])
    return int(n, 2)
def multiprecision_addtion(a, b, W, t):
    a.reverse() 
    b.reverse()
    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        s = a[i] + b[i] + epsilon
        x = s%e
        if(s>e): epsilon = 1
        else: epsilon = 0
        c.append(x)
    return [epsilon, c[::-1]]
def multiprecision_subtraction(a, b, W, t):
    a.reverse()
    b.reverse()
    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        d = a[i] - b[i] - epsilon
        if (d< 0):
            d += e
            epsilon = 1
        else: epsilon = 0
        x = d%e
        c.append(x)
    return epsilon, c[::-1]
if __name__ == "__main__":
    [epsilon,c] = multiprecision_subtraction(a, b, W, t)
    p = int_to_dec(p)
    if epsilon == 1:
        d = multiprecision_addtion(c, p, W, t)
    elif epsilon == 0:
        d = c
    print(d)