# Hàm tìm ước chung lớn nhât
def gcd(a, b):
    if(a < b):
        return gcd(b, a)
    if(a % b == 0):
        return b
    return gcd(b, a % b)
def power(a, k, n):
    b = 1
    
    # Cập nhật số a nêu nó lơn hơn n
    a = a % n
    while(k > 0):
        # Nếu k là số lẻ, nhân a với kết quả
        if(k % 2 != 0):
            b = (b * a) % n
        # k là số chẵn
        k = k >> 1
        a = (a * a) % n
    return b
def isCarmichael(n):
    b = 2
    while(b < n):
        # Nếu b nguyên tố cùng nhau với n
        if(gcd(b, n) == 1):
            # Và nếu pow(b, n - 1) != 1, return False
            if(power(b, n - 1, n) != 1):
                return 0
        b = b + 1
    return 1
n = int(input("Nhập số nguyên n: "))
if(isCarmichael(n) == 1):
    print("Số {} là số Carmichael.".format(n))
else:
    print("Số {} không là số Carmichael".format(n))
m = int(input("Nhập số nguyên m: "))
for i in range(1, m+1):
    if(isCarmichael(i)):
        print(i, end=" ")
            