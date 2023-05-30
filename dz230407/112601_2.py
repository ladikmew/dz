def fibonachi(n):

    if n == 1:
        return 2
    else:
        fib = [0]*100
        fib[1] = 1
        for i in range(1, 100):
            fib[i + 1] += fib[i]
            fib[i + 2] += fib[i]

            if fib[i] == n:
                return i
            elif fib[i]>n:
                return -1

if __name__ == "__main__":
    n = int(input())
    print(fibonachi(n))
