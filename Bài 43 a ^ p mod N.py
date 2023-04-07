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
def millerTest(r, n):
    # Chon một số a ngẫu nhiên từ [2..n-2]
    # Các trường hợp đảm bảo n > 4
    a = 2 + random.randint(1, n - 4)
    # Thực hiện vòng lặp tính a^r % n
    y = power(a, r, n)
    if(y == 1 or y == n-1):
        return True
    # Tiếp tục bình phương x trong kho một trong các trường hợp sau không xảy ra:
    # 1. r không chạm tới n - 1
    # 2. y ^ 2 % n không bằng 1
    # 3. y ^ 2 % n không bằng n - 1
    while(r != n - 1):
        y = (y * y) % n 
        r *= 2
        if(y == 1):
            return False
        if(y == n - 1):
            return True
    return False
# Trả về False nếu n là composite và trả về true nếu n là số nguyên
# k là một tham số đầu vào quyết định mức độ chính xác, k càng cao nghĩa là độ chính xác càng cao
def isPrime(n, k):
    if(n <= 1 or n == 4):
        return False
    if(n <= 3):
        return True
    # Tìm giá trị của r sao cho n = 2^s * r + 1 với r >= 1
    r = n - 1
    while(r % 2 == 0):
        r //= 2
    for i in range(k):
        if(millerTest(r, n) == False):
            return False
    return True
n = int(input("Nhập số nguyên 0 < n < 1000: "))
primes = []
k = 4
for i in range(n):
    if isPrime(i, k):
        primes.append(i)
p = random.choice(primes)
print("Số p: ", p)
print("\nCác số a thỏa mãn điều kiện trên là: ")
for a in range(n):
    if isPrime(pow(a, p, n), k):
        print(a, end = " ")