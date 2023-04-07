import random
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

def isPrime(n, k):
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
            if power(a, n - 1, n) != 1:
                return False
    return True
# Driver code
k = 3
n = int(input("Nhập số nguyên dương n: "))
if(isPrime(n, k) == True):
    print("Số {} là số nguyên tố ".format(n))
else:
    print("Số %d không là số nguyên tố" % n)