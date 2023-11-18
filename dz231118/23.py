def f(start, end):
    d = [0] * 10000
    d[start] = 1
    for i in range(start, end + 1):
        d[i + 1] += d[i]
        d[i * 2] += d[i]
        d[i * i] += d[i]
        d[12] = 0
    return d[end]


print(f(3, 25))
