
def r(n):
    b = str(bin(n)[2:])[::-1]
    b+=b[-1]
    res = int(b,2)
    return res
print(r(39))
# for i in range(1,600):
#     if r(i)> 99:
#         print(i)

