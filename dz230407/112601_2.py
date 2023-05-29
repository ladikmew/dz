def fibonachi(n):
    if n>6:
        fib = [0]*(n)
    else:
        fib = [0]*(n+2)
    fib[0] = 1
    i = 0
    r = 0
    while r < n:
        fib[i + 1] += fib[i]
        fib[i + 2] += fib[i]
        r = fib[i+1]
        i += 1
    if r==n:
        return i+1
    else:
        return -1

if __name__ == "__main__":
    n = int(input())
    print(fibonachi(n))
