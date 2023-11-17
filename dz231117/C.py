n = int(input())
a = []
for i in range(n):
    d = int(input())
    if d not in a:
        a.append(d)
print(*a, sep='\n')