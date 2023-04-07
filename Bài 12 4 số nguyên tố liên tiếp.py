def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_consecutive_primes(n, num_primes):
    sequences = []
    primes = []
    num = 2
    while sum(primes) <= n:
        if is_prime(num):
            primes.append(num)
            if len(primes) > num_primes:
                primes.pop(0)
            if len(primes) == num_primes and is_prime(sum(primes)):
                sequences.append(primes.copy())
        num += 1
    return sequences

N = int(input("Enter a number: "))
num_primes = int(input("Enter the number of consecutive primes to find: "))
sequences = find_consecutive_primes(N, num_primes)
if len(sequences) == 0:
    print("No sequences found.")
else:
    for seq in sequences:
        print(seq)