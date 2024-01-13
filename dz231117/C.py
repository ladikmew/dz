n = int(input())
a = []
k = -100000000000
for i in range(n):
    d = int(input())
    if d>k:
        k = d
        a.append(d)
print(*a, sep='\n')