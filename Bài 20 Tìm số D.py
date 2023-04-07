def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def print_pairs(M, N, D):
    result = []
    for i in range(M, N + 1):
        for j in range(i+1, N+1):
            if gcd(i, j) == D:
                result.append((i, j))
    return result
M = int(input("Enter M: "))
N = int(input("Enter N: "))
D = int(input("Enter D: "))
print("Các cặp số (a, b) thỏa mãn điều kiện trên là:", ", ".join(str(i) for i in print_pairs(M,N,D)))