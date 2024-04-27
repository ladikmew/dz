# 2
# for k in range(0,2):
#     for m in range(0, 2):
#         for n in range(0, 2):
#             for l in range(0, 2):
#                 f = not(n) or k and not(m) or (l==m)
#                 if f==0:
#                     print(k,m,n,l)

# 5
# for n in range(1, 1000):
#     n1 = bin(n)[2:]
#     if n % 2 == 0:
#         n1 = "1" + n1 + "1"
#     else:
#         n1 = n1 + "10"
#     r = int(n1,2)
#     if r>179:
#         print(n)
#         break

# print((1079*1919*13*199)/19999999 )
#
# import itertools
# m = list(itertools.permutations("АААААЁЁЁЁЁРРРРРТТТТТШШШШШ",5))
# c = 0
# for i in m:
#     c+=1
#     s = str(i[0]+i[1]+i[2]+i[3]+i[4])
#     if s.count("А")<=1 and "ЁЁ" not in s:
#         print(c)
#         print(s)
#         break

# print((20240*14*7)/(8*1024))

# def f(s):
#     while "2222" in s or "7777" in s:
#         if "2222" in s:
#             s = s.replace("2222",'77')
#         else:
#             s = s.replace("7777",'22')
#     return s
#
# s = ''
# for i in range(47):
#     s+="7"
# print(f(s))

#
# def F(a, b, x):
#     if a <= x <= b:
#         return True
#     else:
#         return False
#
#
# mn = 10 ** 9
#
# for a in range(0, 200):
#     for b in range(a, 200):
#         k = 0
#         for i in range(-200, 200):
#             x = i / 2
#             # (¬(x∈A)∧(x∈B))→((x∈B)→¬(x∈C))
#             if ((not(F(a, b, x))) and F(74, 194, x)) <= (F(74, 194, x) <= (not (F(152, 223, x))))==1:
#                 k = k + 1
#
#         if k == 400:
#             mn = min(mn, b - a)
#
# print(mn)

# 6
# from turtle import *
# k = 10
# tracer(0)
#
# left(90)
# pendown()
# for i in range(2):
#     forward(12*k)
#     right(90)
#     forward(19*k)
#     right(90)
# penup()
# forward(4*k)
# right(90)
# forward(6*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(12*k)
#     right(90)
#     forward(6*k)
#     right(90)
# penup()
#
# for x in range(-20*k,20*k,k):
#     for y in range(-20*k,20*k,k):
#         goto(x,y)
#         dot(3,"red")
# done()

# left(90)
# pendown()
# for i in range(2):
#     forward(12*k)
#     right(90)
#     forward(19*k)
#     right(90)
# penup()
# forward(4*k)
# right(90)
# forward(6*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(12*k)
#     right(90)
#     forward(6*k)
#     right(90)
# penup()
# c = 0
# canvas = getcanvas()
# for x in range(-200,200):
#     for y in range(-200,200):
#         goto(x*k,y*k)
#         dot(3,"red")
#         if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
#             c+=1
# done()

# 7
# print((((7*14)/8)*20240)/1024)
# print((13*20240)/1024)

# 14
# from string import digits, ascii_uppercase
#
# ss = digits + ascii_uppercase
# for i in range(29):
#         s = int(f'42{ss[i]}158',29)+int(f'16{ss[i]}234',29)
#         if s%28==0:
#             print(s//28)
#             break

# 19
# def F(x, y, p):
#     if x + y >= 143 and p == 3: return True
#     if x + y < 143 and p == 3: return False
#
#     return F(x + 3, y, p + 1) or F(x * 2, y, p + 1) or F(x, y + 3, p + 1) or F(x, y * 2, p + 1)
#
#
# for s in range(1, 124):
#     if F(s, 16, 1):
#         print(s)

# 20
# def F(x, y, p):
#     if x + y >= 143 and p == 4: return True
#     if x + y < 143 and p == 4: return False
#     if x + y >= 143: return False
#
#     if p % 2 == 0:
#         return F(x + 3, y, p + 1) and F(x * 2, y, p + 1) and F(x, y + 3, p + 1) and F(x, y * 2, p + 1)
#     else:
#         return F(x + 3, y, p + 1) or F(x * 2, y, p + 1) or F(x, y + 3, p + 1) or F(x, y * 2, p + 1)
#
#
# for s in range(1, 124):
#     if F(s, 16, 1):
#         print(s)

# 21
# def F(x, y, p):
#     if x + y >= 143 and (p==3 or p==5): return True
#     if x + y < 143 and p==5: return False
#     if x + y >= 143: return False
#
#     if p%2==1:
#         return F(x+3, y, p+1) and F(x*2, y, p+1) and F(x, y+3, p+1) and  F(x, y*2, p+1)
#     else:
#          return F(x+3, y, p+1) or F(x*2, y, p+1) or F(x, y+3, p+1) or  F(x, y*2, p+1)
#
#
# def F1(x, y, p):
#     if x + y >= 143 and p==3: return True
#     if x + y < 143 and p==3: return False
#     if x + y >= 143: return False
#
#     if p%2==1:
#         return F1(x+3, y, p+1) and F1(x*2, y, p+1) and F1(x, y+3, p+1) and  F1(x, y*2, p+1)
#     else:
#          return F1(x+3, y, p+1) or F1(x*2, y, p+1) or F1(x, y+3, p+1) or  F1(x, y*2, p+1)
#
# for s in range(1, 124):
#     if F(s, 16, 1):
#         print(s)
#
# print()
#
# for s in range(1, 124):
#     if F1(s, 16, 1):
#         print(s)

# 23
# def F(x, y):
#     if x == y: return 1
#
#     if x > y: return 0
#
#     if x < y: return F(x+1, y) + F(x*2, y)
# print(F(3, 6)*F(6, 12)*F(12, 16))

# 25
# from fnmatch import *
# for x in range(0,10**10,2024):
#     if fnmatch(str(x), '10*2024?'):
#         print(x, x//2024)

# 17
# count = 0
# a = 100000001
# m = 0
# f = open('17.txt')
# l = [int(i) for i in f]
# for i in range(len(l)):
#     if l[i] > m and l[i] % 21 == 0:
#         m = l[i]
# for i in range(len(l) - 1):
#     if (l[i ] > m) or (l[i + 1] > m):
#         count += 1
#         a = min(a, l[i] + l[i + 1])
# print(count, a)

#26
f = open("26.txt")
k =[int(i) for i in f]
l = sorted(k,reverse=True)
print(l)
zvezdy = [l[0]]
for i in range(1,len(l)):
    if zvezdy[-1]-l[i]>=0.1*l[i]:
        zvezdy.append(l[i])
print(len(zvezdy),zvezdy)

# 7191862
# 41952321