import math
a = input().split()
n = int(a[0])
m = int(a[1])
e2 = (n**2)-m
e1 = (2*n)
h = 0
for i in range(0, 1001):
    s = (i**4) - e1 * (i ** 2) + i + e2
    if s == 0:
        b = n-(i**2)
        if i+b**2 == m:
            h += 1
print(h)

