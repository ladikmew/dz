f = open('99.txt')
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if len(set(a)) == 5:
        suma = 0
        sr = 0
        for i in range(0, len(a)):
            if a.count(a[i]) == 2:
                suma += a[i]
        sr = (sum(a) - suma) / 4
        if suma < sr:
            cnt += 1
print(cnt)
