def f(a,b):
    if a < b:
        d = [0] * (b + 1)
        d[a] = 1
        for i in range(a + 1, b + 1):
            if i % 3 == 0:
                d[i] = d[i - 1] + d[i // 3]
            else:
                d[i] = d[i - 1]
        return d[b]
    elif a>b:
        return 0
if __name__=="__main__":
    a, b = list(map(int, input().split()))
    print(f(a,b))
