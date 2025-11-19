def is_pseudoprime_base2(n):
    if is_prime(n):
        return False
    return pow(2, n-1, n) == 1  # Fermat test

pseudoprimes = [n for n in range(3, 10001) if is_pseudoprime_base2(n)]

print(pseudoprimes)
