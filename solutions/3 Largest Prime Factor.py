n = 600851475143
p = 2
while n >= p*p:  # Compare to smallest non-prime made of primes
    if n % p == 0:  # Reduce to lower num
        n /= p
    else:
        p += 1  # Try different num
print(n)



