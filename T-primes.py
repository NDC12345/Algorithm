def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
n= int(input("Nhập vào số tự nhiên n: "))
print("Các số T- prime là: ")
for i in range(n+1):
    if(is_prime(i) == True):
        T = i * i
        if(T < n):
            print(T, end = " ")