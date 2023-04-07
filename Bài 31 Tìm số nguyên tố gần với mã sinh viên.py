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
def power(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result
def find_max_prime(code):
    k = 4
    primes = []
    for i in range(code + 1):
        if isPrime(i, k):
            primes.append(i)
    return max([p for p in primes if p < code % p] + [p for p in primes if p >= code % p])
code = int(input("Nhập mã số sinh viên của bạn: "))
sbd = int(input("Nhập số báo danh của bạn vào: "))
n = 123456
print("Số nguyên tố gần nhất với mã sinh viên của bạn là: ", find_max_prime(code))
print("%d^%d mod %d: "%(sbd, find_max_prime(code),n),power(sbd, find_max_prime(code), n))