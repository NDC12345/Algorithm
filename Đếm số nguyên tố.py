import math
def is_Prime(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True
if __name__ == '__main__':
    n = int(input("Nhập vào số nguyên n: "))
    count = 0
    for i in range(n):
        if (is_Prime(i) == True):
            print(i, end =" ")
            count += 1
    print("\nCó {count} số nguyên tố nhỏ hơn hoặc bằng {n}".format(count=count, n=n))
            