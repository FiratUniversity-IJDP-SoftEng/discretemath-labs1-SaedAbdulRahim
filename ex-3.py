for p in primes_up_to(100):
    M = 2**p - 1
    if is_prime(M):
        print(f"2^{p} - 1 = {M} is PRIME")
    else:
        print(f"2^{p} - 1 = {M} is NOT prime")
