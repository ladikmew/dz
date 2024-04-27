def r(n, f=0):
    if n > 25:
        return 0
    if n == 25:
        if f == 7:
            return 1
        else:
            return 0
    return r(n + 2, f | 1) + r(n * 3, f | 2)

print(r(1))
