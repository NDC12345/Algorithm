def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_prime_sum_diff(n):
    result = []
    primes = find_primes(n)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] + primes[j] <= n and is_prime(primes[i] + primes[j]) and is_prime(abs(primes[j] - primes[i])):
                result.append((primes[i], primes[j]))
    return result

N = int(input("Enter a number: "))
result = find_prime_sum_diff(N)
if result is None:
    print("No such pair found.")
else:
    print(result)