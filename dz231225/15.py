for A in range(0,300):
    a = 0
    for x in range(0,300):
        for y in range(0,300):
            f = (x+2*y<A) or (y>x) or (x>60)
            if f==1:
                a+=1
    if a==90000:
        print(A)
        break
#

# for a in range(0, 300):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if (x + 2 * y < a) or (y < x) or (y > 60):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break