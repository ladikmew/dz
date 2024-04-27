# def f(x, y, A):
#     return ((3 * x + 4 * y) != 101) or (x < A) or (3 * y <= A)
#

for A in range(1, 1001):
    c = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if ((3 * x + 4 * y) != 101) or (x < A) or (3 * y <= A) == 0:
                c = False
    if c:
        print(A)
