n = int(input("Nhap n: "))
if (n < 0):
    n *= -1
i = 2

while(n != 1):
    if (n % i == 0):
        print(i)
        if (n != i):
            print("x")
        else:
            print(" ")
        n /= i
    else:
        i+=1
        