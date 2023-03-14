import random
def power(a, k, n):
    b = 1
    # Cập nhật x nếu nó lớn hơn p
    a = a % n
    while(k > 0):
        # Nếu y là số lẻ, nhân x với kết quả
        if(k & 1):
            b = (b * a)  % n
        # y là số chẵn
        k = k >> 1 # y = y/2
        a = (a * a) % n
    return b
# Hàm này được gọi cho tất cả k lần thử. Nó sẽ trả False nếu n hợp số và 
# trả về false nếu n thực sự là số nguyên tố. r là một số lẻ sao cho 2^s*r = n-1
# với mỗi s >= 1
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
k = 4
print("All primes smaller than 100: ")
for n in range(1, 100):
    if(isPrime(n, k)):
        print(n, end = " ")
        