MAX_N = 10000
MAX_M = 100
primes = []
ans = [0] * MAX_M

def sieve_of_eratosthenes():
    is_primes = [True] * (MAX_N+1)
    for i in range(2, MAX_N+1):
        if is_primes[i] == True:
            for p in range(i*2, MAX_N+1, i):
                is_primes[p] = False
            primes.append(i)

def solve(n, m, k):
    if m == 0 and n == 0:
        return True
    if m == 0 or n == 0:
        return False
    for i in range(k, len(primes)):
        if n < primes[i]:
            break
        ans[m-1] = primes[i]
        if solve(n - primes[i], m - 1, i + 1) == True:
            return True
    return False

n, m = map(int, input().split())
sieve_of_eratosthenes()
if solve(n, m, 0) == True:
    for i in range(m):
        print(ans[i], end=' ')
    print()
else:
    print("NO")