# #прямой порядок


n,m = list(map(int,input().split()))
a = [[1] * m for i in range(n)]
if n==1 or m==1:
    print(1)
else:
    for i in range(1,n):
        for j in range(1,m):
            p = int(a[i-1][j])
            l = int(a[i][j-1])
            a[i][j] = p+l
    print(int(a[i][j]))
