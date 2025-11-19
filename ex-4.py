all_prime = True
for n in range(0, 40):
    value = n*n + n + 41
    if not is_prime(value):
        all_prime = False
        print(f"Not prime at n={n}: {value}")

print("Polynomial is prime for all n = 0..39" if all_prime else "Some values were not prime")

# Test at n=40
value_40 = 40*40 + 40 + 41
print(f"n=40 gives {value_40}, prime? {is_prime(value_40)}")
