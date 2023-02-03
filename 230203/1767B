t = int(input())
rez = []

for i in range(t):
    l = []
    k = 0

    n = int(input())
    a = list(map(int, input().split()))
    l = sorted(a)
    for i in range(n):
        if int(l[i]) > a[0]:
            if (a[0] + l[i]) % 2 == 0:
                a[0] = (a[0] + l[i]) // 2
            else:
                a[0] = ((a[0] + l[i]) // 2) + 1

    rez.append(a[0])
for i in rez:
    print(i)
