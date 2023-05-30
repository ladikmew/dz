n = int(input())
f = list(map(int, input().split()))
a = []
a.append(0)
h = True
for j in range(1, n+1):
    a.append(f[j-1])
for i in range(1, n+1):
    l = a[a[i]]
    if a[l] == i:
        print('YES')
        h = False
        break

if h:
    print('NO')
