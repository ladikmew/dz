def f(i):
    b = [[0] * 4 for i in range(n)]
    b[0] = [1, 1, 0, 0]
    for i in range(1, n):
        b[i][0] = b[i - 1][0] + b[i - 1][1] + b[i - 1][2]
        b[i][1] = b[i - 1][0]
        b[i][2] = b[i - 1][1]
        b[i][3] = b[i - 1][2] + 2 * b[i - 1][3]
    return (b[-1][0]+b[-1][1]+b[-1][2])
if __name__=="__main__":
    n = int(input())
    print(f(n))
