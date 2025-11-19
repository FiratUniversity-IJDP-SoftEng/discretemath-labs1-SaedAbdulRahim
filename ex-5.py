import random

def random_100_digit_prime():
    while True:
        num = random.randrange(10**99, 10**100)
        if is_prime(num):
            return num

primes_100_digits = [random_100_digit_prime() for _ in range(10)]

for p in primes_100_digits:
    print(p, "\n")
