def fib(f1, f2, a, k):
    while k < (a - 2):
        s = f1 + f2
        f1 = f2
        f2 = s
        k += 1
    print(f2)


if __name__ == "__main__":
    f1 = 1
    f2 = 1
    a = int(input())
    k = 0
    fib(f1, f2, a, k)
