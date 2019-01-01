
for x in range(999, 100, -1):  # All 3 digits
    for y in range(999, 100, -1):
        z = x*y
        if str(z) == str(z)[::-1]:  # Check if palindrome
            print(z)