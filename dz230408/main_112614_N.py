#обратный порядок
n, m = list(map(int, input().split()))
a = [[0] * m for i in range(n)]
a[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        k = a[i - 1][j - 2]
        l = a[i - 2][j - 1]
        a[i][j] += k
        a[i][j] += l
        
print(a[n - 1][m - 1])
