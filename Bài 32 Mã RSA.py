import random
def gcd(a, b):
    if(a < b ):
        return gcd (b, a)
    if(a % b == 0):
        return b
    return gcd(b, a % b)
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
def generate_primes():
    k = 4
    primes = []
    for i in range(100, 500):
        if isPrime(i, k):
            primes.append(i)
    p = random.choice(primes)
    q = random.choice(primes)
    while q == p:
        q = random.choice(primes)
    return p, q
def pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def generate_key_pair():
    p, q = generate_primes()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randrange(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(1, phi_n)
    d = pow(e, -1, phi_n)
    return (e, n), (d, n)

def encrypt(public_key, message):
    e, n = public_key
    c = pow(message, e, n)
    return c

def decrypt(private_key, ciphertext):
    d, n = private_key
    m = pow(ciphertext, d, n)
    return m

sbd = int(input("Nhập số báo danh : "))
public_key, private_key = generate_key_pair()
m = sbd + 123
ciphertext = encrypt(public_key, m)
plaintext = decrypt(private_key, ciphertext)

print("Public key:", public_key)
print("Private key:", private_key)
print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)
#Ciphertext và plaintext giống nhau vì thông điệp m được mã hóa và giải mã bằng cùng một khóa. Trong đoạn code trên, khóa công khai và khóa bí mật được tạo ra bằng hàm generate_key_pair(), và sau đó được sử dụng để mã hóa và giải mã thông điệp m