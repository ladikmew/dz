f = open('27A.txt')

n = int(f.readline())

summ = [0] * 100

for i in range(n):
    a = f.readline().split()
    x, y = int(a[0]), int(a[1])
    a1 = [0] * 100
    a2 = [0] * 100
    for j in range(100):
        s1 = int(summ[j]) + int(x)
        j1 = s1 % 100
        a1[j1] = max(summ[j1],s1 )

        s2 = int(summ[j]) + int(y)
        j2 = s2 % 100
        a2[j2] = max(summ[j2], s2)
    for k in range(100):
        summ[j] = max(a1[j],a2[j])

print(summ)
