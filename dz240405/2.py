for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = not(not(x != w) and z) and not(w == z) and (x != z)
                if f==1:
                    print(x,z,w)