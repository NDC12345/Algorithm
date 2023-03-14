a = [0, 11, 173, 248]
b = [0, 1, 226, 64]
W = 8
t = 4
def solve(a,b,W, t):
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
    print(solve(a, b, W, t))