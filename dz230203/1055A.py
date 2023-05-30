def find_way(n, s, a, b):
    if a[0] == 1:
        k = False
        if a[s - 1] == 1:
            return "YES"

        elif b[s - 1] == 1:
            for i in range(s - 1, n):
                if a[i] == 1 and b[i] == 1:
                    k = True
            if k:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == "__main__":
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(find_way(n, s, a, b))
