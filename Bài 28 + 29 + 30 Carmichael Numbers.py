import random
def gcd(a, b):
    if(a < b ):
        return gcd (b, a)
    if(a % b == 0):
        return b
    return gcd(b, a % b)
# Hàm nhân bình phương có lặp
def power(a, k, n):
    res = 1
    a = a % n
    if(a == 0):
        return 0
    while(k > 0):
        if(k & 1): # Sử dụng phép AND kiểm tra ki = 1 hay không
            res = (res * a)  % n
        k = k >> 1 # Loại các bits đã kiểm tra
        a = (a * a) % n
    return res

def isCarmichaelNumber(n):
    b = 2
    while (b < n):
        # Nếu b và n nguyên tố cùng nhau
        if(gcd(b, n) == 1 and power(b, n-1, n) != 1):
            return 0
            # Và nếu pow(b, n - 1 ) không bằng 1 return False
        b = b + 1
        
    return 1
def millerTest(r, n):
    # Chon một số a ngẫu nhiên từ [2..n-2]
    a = 2 + random.randint(1, n - 4)
    # Tính a^d % n
    y = power(a, r, n)
    if(y == 1 or y == n-1):
        return True
    # Thực hiện vòng lặp khi r != n - 1 học y^2 % n không bằng 1 hoặc bằng n-1
    while(r != n - 1):
        y = (y * y) % n 
        r *= 2
        if(y == 1):
            return False
        if(y == n - 1):
            return True
    return False
def isPrime(n, k):
    if(n <= 1 or n == 4):
        return False
    if(n <= 3):
        return True
    r = n - 1
    while(r % 2 == 0):
        r //= 2
    for i in range(k):
        if(millerTest(r, n) == False):
            return False
    return True
n = int(input("Nhập số nguyên n: "))
# Sử dụng định lí Fermat nhỏ để kiểm tra tính Carmichael của một số. Kiểm tra n có là số nguyên tố hay không nếu n là số nguyên tố
# thì n không phải là số Carmichael
if(isCarmichaelNumber(n) == 1 and isPrime(n, 4) == False):
    print("Số %d là số Carmichael" % n)
else:
    print("Số % d không là Carmichael" % n)
m = int(input("Nhập số nguyên dương m: "))
print("Các số Carmichael nhỏ hơn {} là: ".format(m))
sum = 0
for i in range(2, m + 1):
    if(isCarmichaelNumber(i) == 1 and isPrime(i, 4) == False):
        sum += i
        print(i, end= " ")
print("\nTổng các số Carmichael đó là: ", sum)