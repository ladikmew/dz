
def f(n,k,a):
    b = [0]*(n+1)
    b[0] = 1
    for i in a:
        for j in range(len(b)):
            if (i <= j):
                b[j] += b[j - i]
    return b[n]

n = int(input())
k = int(input())
a = list(map(int, input().split()))
print(f(n,k,a))
