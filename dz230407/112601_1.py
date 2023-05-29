def fibonachi(n):

    fib = []
    fib.append(1)
    fib.append(1)
    r = fib[1]
    i = 2
    while r<n:
        fib.append(fib[i - 1] + fib[i - 2])
        r = fib[i - 1] + fib[i - 2]
        i+=1
    if fib[len(fib)-1]==n:
        return i
    else:
        return -1

if __name__ == "__main__":
    n = int(input())
    print(fibonachi(n))
