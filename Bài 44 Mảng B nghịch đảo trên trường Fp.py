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
def inverse(a, p):
    # Sử dụng thuật toán Euclid mở rộng để giải ax + py = 1
    x0, y0, x1, y1 = 1, 0, 0, 1 # Khởi tạo các hệ số
    r0, r1 = a, p # Khởi tạo các số dư
    while r1 > 0:
        q = r0 // r1 # Tính thương nguyên
        r0, r1 = r1, r0 - q*r1 # Cập nhật các số dư
        x0, x1 = x1, x0 - q*x1 # Cập nhật các hệ số x
        y0, y1 = y1, y0 - q*y1 # Cập nhật các hệ số y
    # Khi thoát khỏi vòng lặp ta có r0 = gcd(a, p) và ax0 + py0 = r0
    if r0 != 1:
        return None
    else:
        return x0 % p
k = 4
p = int(input("Nhập vào giá trị của p: "))
if not isPrime(p, k):
    exit()
n = int(input("Nhập vào số lượng phần tử của mảng A: "))
A = []
for i in range(n):
    a = int(input(f"Nhập vào phần tủ thứ {i + 1} của mảng A: "))
    if a < 0:
        print(f"{a} không thuộc F_p")
    A.append(a)
B = []
for a in A:
    b = inverse(a, p)
    if b is None:
        print(f"{a} không có nghịch đảo modulo {p}")
    B.append(b)
print(f"Mảng B có các phần tử là nghịch đảo của các phần tử trong A là: {B}")
    