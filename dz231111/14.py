h = []
for y in range(0, 37):
    for x in range(0, 37):
        a = 9 * 1 + y * (37 ** 1) + 7 * (37 ** 2) + 5*(37 ** 3) + 4 * (37 ** 4) + x * (37 ** 5) + 1 * (37 ** 6) + 2 * (
                    37 ** 7)

        if a%36==0:
           # print(x,y)
           h.append(int(x*37+y))
print(max(h))

# # print(72/1.5)
# # print(54*2)
# print((5*(2**8))-25-990)
# print(265/8)