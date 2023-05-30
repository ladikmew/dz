def f(n,k):
    b = [0]*(n + 1)
    b[0] = 1
    for i in k:
        for j in range(len(b)):
            if (i <= j) :
                b[j] += b[j - i]
    return b[n]

n = int(input())
k = [1, 2, 5, 10]
print(f(n,k))
