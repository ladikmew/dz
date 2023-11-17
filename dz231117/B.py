a = int(input())
c = 0
k = 0
for i in range(a):
    d = int(input())
    if d == 1:
        c += 1
    elif d == 0:
        c = 0
    if c >= k:
        k = c

print(k)

