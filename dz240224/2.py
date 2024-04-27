for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = ((y <= x) or (z and w)) <= ((x or not(w)) and (y == z))
                if f==0:
                    print(x,y,z,w)