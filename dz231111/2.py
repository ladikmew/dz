print("xyzw")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f1 = (x == y) and (w <= z)
                f2 = (x <= y) <= (w == z)
                if f1 == 1 and w == 0 and x == 1:
                    print(x, y, z, w)
