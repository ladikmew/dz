# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f1 = (w == x) and (y <= z)
#                 f2 = (w <= x) <= (y == z)
#                 if f1 == 1 and w == 0 and y == 1:
#                     print(x, y, z, w)

# a = [9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,16,16,16,16,16,17,17,17,17,17,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# print(len(a))
# 8
# def main(n, v1, v2) -> None:
#     a = [1]
#     v = 1
#     while len(a) < n:
#         a.append(v % 13)
#         v += v % 13
#     print(a[n - v1], a[n - v2])
#
#
# # if __name__ == '__main__':
# N = 0  # количество всего
# v1 = 0  # первый номер с той же индексацией, что и в задаче
# v2 = 0  # второй номер с той же индексацией, что и в задаче
# main((10**7-100), 200, 99999)

#5
# for x in  range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             if (y==z)==False and (x<=y)==True:
#                 #1 f = ((x and z)<=y) <= (y==z)
#                 #2 f = (y<=z)==x
#                 #3 f = ((x and not(y))==(y and z))<=(not(y)or z)
#                 #4 f = (not(y) ^ x) <= (not(z) <= ~x)
#                 #5 f = (x and not(y))<=(not(x) or z)
#                 print(f)

#1
# i=0
# ss=0
# print('start')
# while ss<10**8-628: #номер нужного
#     i += 3
#     ss+=2**(i-1)
#     #print(i,ss)
# ss-=2**(i-1)
# rez=10**8-628-ss+2**i
# print(rez)

#6
print("A B C D E F")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        g = (((((~a and ~b) == c) <= ~c) <= (((~b and ~c) == d) <= ~d))
                        <= (((~c and ~d) == e) <= ~e)) <= (((~d and ~e) == f) <= ~f)
                        print(a, b, c, d, e, f , g)

#4
# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x * 2), y)+f()
# print(f(10, 51) * f(51, 5094))
    print(15*18)