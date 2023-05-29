#прямой порядок
n, m = list(map(int, input().split()))
w = max(n,m)
a = [[0] * (w+1) for i in range(w+1)]
a[0][0] = 1
for i in range(0, n - 1):
    for j in range(0, m - 1):
        a[i + 1][j + 2] += a[i][j]
        a[i + 2][j + 1] += a[i][j]
print(a[n - 1][m - 1])
