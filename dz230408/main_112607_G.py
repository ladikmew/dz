def no_dogs(n):
    b = [[0] * 2 for i in range(n + 1)]
    b[0][0],b[0][1] = 1,1
    for i in range(1, n + 1):
        b[i][0] = b[i - 1][0] + b[i - 1][1]
        b[i][1] = b[i - 1][0]
    return b[len(b) - 1][0]


if __name__ == "__main__":
    n = int(input())
    print(no_dogs(n))
