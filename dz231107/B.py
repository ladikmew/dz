n, m = list(map(int, input().split()))
k = int(input())
if k == 1:
    print(0)
elif k > 1 and k <= m:
    print(n * (m - 1))
elif k > m:
    print(n * (m - 1) + m * (n - 1))
