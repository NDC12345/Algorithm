def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

def find_amicable_numbers(n):
    amicable_numbers = []
    for i in range(1, n):
        sum_divisors_i = sum_of_divisors(i)
        if sum_of_divisors(sum_divisors_i) == i and sum_divisors_i != i:
            amicable_numbers.append((i, sum_divisors_i))
    return amicable_numbers

n = int(input("Nhập N: "))
print(find_amicable_numbers(n))