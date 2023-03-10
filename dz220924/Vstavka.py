def sort_v(a: list) -> None:
    for i in range(1, len(a)):
        for j in range(i - 1, -1, -1):
            if a[j] > a[i]:
                a[j], a[i] = a[i], a[j]
            else:
                return a
