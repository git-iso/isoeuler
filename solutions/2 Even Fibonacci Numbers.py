import math
z = 0
n = 0
x = 0
while z < 4000000:
    n += 3 # Even fibs on every 3rd term
    z = (((1 + 5 ** 0.5) / 2)**n - (1 -((1 + 5 ** 0.5) / 2))**n) / math.sqrt(5) # Formula to find fib at certain term
    if z >= 4000000:
        break
    x += z
print(int(x))





