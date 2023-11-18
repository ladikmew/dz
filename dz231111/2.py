print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f1 = (w == x) and (y <= z)
                f2 = (w <= x) <= (y == z)
                if f1 == 1 and w == 0 and y == 1:
                    print(x, y, z, w)
