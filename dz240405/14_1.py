for z in "0123456789abcdefghijklmnopqrstuvwxy":
    z1 = "3b"+ str(z) +"4c"
    for y in "0123456789abcdefghi":
        y1 = "a12f" + str(y)
    res = int(z1,35)+int(y1,19)
    if res%7==0:
        print(res)

