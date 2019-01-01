y = 0
b = 0
for x in range(1, 101):
    y += x
z = y**2

for a in range(1, 101):
    b += a**2
print((z-b))
