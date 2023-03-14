import gcd
def pollard_rho(n,  seed = 2, f = lambda x: x ** 2 + 1):
    x, y, d = seed, seed, 1
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd((x-y) % n, n)
    if d != n: return d
if __name__ == '__main__':
    n = input("Nhập vào số bất kì: ")
    print("Ước chung lơn nhất là {}".format(pollard_rho(n)))