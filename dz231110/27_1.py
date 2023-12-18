f = open("27_A.txt")
n = int(f.readline())
v = 36
a = []
for i in range(n):
    s, k = map(int, f.readline().split())
    if k % v == 0:
        c = k//v
    else:
        c = k//v + 1
    a.append([s, c])
a.sort()

min_sum = 10**20
for i in range(n):
    new_sum = 0
    for j in range(n):
        new_sum += abs(a[i][0]-a[j][0])*a[j][1]
    min_sum = min(min_sum, new_sum)

print(min_sum)