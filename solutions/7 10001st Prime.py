def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):  # Start at 3 (2 is prime), squared is non-prime, up by 2 to skip even numbers
        k = 1
        while k*k < i:  # Counting up by square (non-prime)
            k += 2 # Move up to next test (odd)
            if i % k == 0: # Prime found below n
                break
        else:
            counter += 1 # Next test
        if counter == n:
            return i # Largest prime


print(nth_prime(10001))
