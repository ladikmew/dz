def sort_ba(a):
    for i in range(len(a)):
        b:bool = True
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i], a[i + 1] = a[i+1], a[i]
                b = False
        if b:
            return a
