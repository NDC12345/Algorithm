def gcd_extended(a, b):
    if a == 0: 
        return (b, 0, 1)
    else: 
        gcd, x, y = gcd_extended(b%a, a)
    return (gcd, y - (b // a) *x, x)
def inverse_modulo_poly(num, modulus, poly):
    if num == 0 or modulus == 0:
        return None
    else: gcd, x, y = gcd_extended(num, modulus)
    if gcd != 1:
        return None
    else: 
        x  = x % poly
        while x < 0:
            x += poly
    return x
num = 0b0111 # x^2 + x + 1
modulus = 283 # The modulus we want to find the inverse modulo of
poly = 0b1011 # x^3 + x + 1

inverse = inverse_modulo_poly(int(num), modulus, poly)
res = [int(i) for i in bin(inverse)[2:]]

if inverse is None:
    print("The number has no inverse modulo the given polynomial.")
else:
    print(f"The inverse of {[int(i) for i in bin(num)[2:]]} modulo {modulus} is: {res}")