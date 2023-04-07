import math
W = 8
p = 2147483647
t = 4
def solve(a, W, p):
    result = []
    m = round(math.log2(p))
    t = round(m/W)
    n = [pow(2, i * W) for i in range(t)]
    for i in n[::-1]:
        result.append(math.floor(a/i))
        a = a % i 
    return result
def sum(a,b,W, t):
    a.reverse()
    b.reverse()
    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        s = a[i] + b[i] + epsilon
        x = s % e
        if(s>e): epsilon = 1
        else: epsilon = 0
        c.append(x)
    return [epsilon, c[::-1]]
if __name__ == "__main__":
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    print("TỔng biểu diễn dưới dạng số nguyên là: %d" %(a+b))
    a = solve(a,W,p)
    b = solve(b,W,p)
    print("Tổng biểu diễn dưới dạng mảng là: ")
    print(sum(a, b, W, t))