p = int(input("Nhập số p: "))
a = int(input("Nhập số nguyên a: "))
def extendedEuclidean(a, p):
    u = a 
    v = p 
    x1 = 1
    x2 = 0
    while(u != 1):
        q = v // u
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1 
        x1 = x
    return x1 % p
print("{}^-1 mod {} = ".format(a, p), extendedEuclidean(a, p))