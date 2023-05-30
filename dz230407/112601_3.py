def get_fib(i):
    if (i <= 2): 
        return 1
    if (fib[i] != 0):
        return fib[i]
    fib[i] = get_fib(i - 1) + get_fib(i - 2)
    return fib[i]

def fibonachi(n):
    if n == 1:
        return 2
    else:
        for i in range(100):
            if get_fib(i) == n:
                return i
            elif get_fib(i) > n:
                return -1


if __name__ == "__main__":
    n = int(input())
    fib = [0]*100
    print(fibonachi(n))
