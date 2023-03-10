import math
n,m = list(map(int, input().split()))
k = 0

for a in range(0,m+1):
    for b in range(0, n+1):
        if a**2 + b == n and a + b**2 == m:
            k+=1
print(k)
