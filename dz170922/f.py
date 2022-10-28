

def f1(a: list, k: int) -> int:
    f = 0
    n = len(a)
    for i in range(0, n):
        if a[i] > k:
            break
        else:
            f += 1
    for j in range(n-1, i, -1):
        if a[i] > k:
            break
        else:
            f += 1
    return f


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    r = f1(s, k)
    print(r)
