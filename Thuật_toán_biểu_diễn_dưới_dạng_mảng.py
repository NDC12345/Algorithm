import math 
a = int(input("Nhập số nguyên a: "))
W = 8
p = 2147483647
def solve(a, W, p):
    result = []
    m = round(math.log2(p))
    t = round(m/W)
    n = [pow(2, i * W) for i in range(t)]
    for i in n[::-1]:
        result.append(math.floor(a/i))
        a = a % i 
    return result
if __name__ == '__main__':
    print(solve(a, W, p))