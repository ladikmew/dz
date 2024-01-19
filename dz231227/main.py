# print("a b c d")
# for a in range(0, 2):
#     for b in range(0, 2):
#         for c in range(0, 2):
#             for d in range(0, 2):
#                 f = not(c) and ((not(a) <= (not(d))) <= (not(b)))
#                 if f == 1:
#                     print(a, b, c, d)

# def ter(n):
#     t = ''
#     while int(n) > 0:
#         t = str(int(n) % 3) + t
#         n = int(n) // 3
#     return str(t)
#
#
# def R(r):
#     n = r
#     r = str(ter(r))
#     if len(str(ter(r))) % 2 != 0:
#         r = "1" + r
#     cnt = r.count("1") + r.count("2") * 2
#     if cnt % 2 == 0:
#         r = r + r[:1]
#     else:
#         p = ter(n % 5)
#         r = r + p
#     if r[0] == "2":
#         r = r[1:]
#         while r[0] == "0":
#             r = r[1:]
#     if r[len(r)-1] == r[len(r) - 2]:
#         r = r[:len(r)-1]
#     return int(r, 3)
#
#
# for i in range(14, 100):
#     if R(i) > 150:
#         print(i,R(i))
#         break


# def R(n):
#     d = bin(n)[2:]
#     if n % 4 == 0:
#         d += "00"
#     else:
#         d += bin(n % 4)[2:]
#     if d[-1] == "0":
#         return int(d[:-1], 2)
#     else:
#         return int(d, 2)
#
# a =[]
# for i in range(56, 1000):
#     y = R(i)
#     if y > 213:
#         a.append(R(i))
# print(min(a))
#

# f = open("9.txt")
# for s in f:
#     a = list(map(int, s.split(",")))
#     povt3 = []
#     nepovt = []
#     for i in a:
#         if a.count(i) == 3:
#             povt3.append(i)
#         elif a.count(i) == 1:
#             nepovt.append(i)
#     if len(nepovt)==2 and len(povt3) == 6:
#         if min(a) not in povt3:
#             print(sum(a))

# for n in range(3,10000):
#     s = "7" + "3" * n
#     while "733" in s or "331" in s or "3333" in s:
#         if "733" in s:
#             s = s.replace("733", "411",1)
#         if "331" in s:
#             s = s.replace("331", "24",1)
#         if "3333" in s:
#             s = s.replace("3333", "7",1)
#     f = s.count("3") * 3 + s.count("7") * 7 + s.count("4") * 4 + s.count("1")
#     if f == 64:
#         print(n)
#         break

# s = "0123456789ABCDE"
# for i in s:
#     r1 = "ABCD" + i
#     r2 = "123" + i + "4"
#     if (int(r1, 15) + int(r2, 15)) % 14 == 0:
#         print((int(r1, 15) + int(r2, 15)) // 14)
#         break

# for A in range(1, 1000):
#     if all((2*x+y < A) or (y > 17) or (x > y) for x in range(1,1000) for y in range(1, 1000))==1:
#         print(A)
#         break

# def calculate(s: str) -> int:
#     stack = []
#
#     def append(operator, operand):
#         if operator == "+":
#             stack.append(operand)
#         elif operator == "-":
#             stack.append(-operand)
#         elif operator == "*":
#             stack.append(stack.pop() * operand)
#         else:
#             stack.append(int(stack.pop() / operand))
#
#     operator, operand = "+", 0
#
#     for c in s:
#         if c in "0123456789":
#             operand = operand * 10 + int(c)
#         elif c in "+-*/":
#             append(operator, operand)
#             operator, operand = c, 0
#
#     append(operator, operand)
#
#     return sum(stack)
#
# print(calculate("30+2+2+6"))

#
# import sys
# sys.setrecursionlimit(3000)
#
# def f(n):
#     if n<=1:
#         return 42
#     elif n>1 and n%2==0:
#         return f(n-2)+f(n-3)
#     else:
#         return f(n-1)+f(n-3)
# print(f(99))

# f = open("17 (2).txt")
# chet = []
# m = []
# c = 0
# su = []
# for s in f:
#     chet.append(int(s))
# for j in chet:
#     if j%100 == 47:
#         m.append(j)
# for i in range(len(chet) - 4):
#     if ((chet[i] > 1000 and chet[i + 1] > 1000 and chet[i + 2] <= 1000 and chet[i + 3] <= 1000) or
#         (chet[i] > 1000 and chet[i + 1] <= 1000 and chet[i + 2] > 1000 and chet[i + 3] <= 1000) or
#         (chet[i] > 1000 and chet[i + 1] <= 1000 and chet[i + 2] <= 1000 and chet[i + 3] > 1000) or
#         (chet[i] <= 1000 and chet[i + 1] > 1000 and chet[i + 2] > 1000 and chet[i + 3] <= 1000) or
#         (chet[i] <= 1000 and chet[i + 1] > 1000 and chet[i + 2] <= 1000 and chet[i + 3] > 1000) or
#         (chet[i] <= 1000 and chet[i + 1] <= 1000 and chet[i + 2] > 1000 and chet[i + 3] > 1000)) and \
#             ((chet[i] + chet[i + 1] + chet[i + 2] + chet[i + 3]) <= max(m)):
#         c += 1
#         su.append(chet[i] + chet[i + 1] + chet[i + 2] + chet[i + 3])
# print(c)
# print(max(su))

# def allPathsSourceTarget(graph):
#     def dfs(current, graph, path, end, result,visited):
#         if current == end:
#             result.append(path)
#             path = []
#
#         for i in graph[current]:
#             if i not in visited:
#                 path.append(i)
#                 visited.append(i)
#                 dfs(i, graph, path, end, result,visited)
#
#     end = len(graph) - 1
#     result = []
#     visited = []
#     dfs(0, graph, [0], end, result,visited)
#     return result
#
# g = [[1,2],[3],[3],[]]
# print(allPathsSourceTarget(g))

# print (bin(111)[2:], bin(81) [2:], bin(208) [2:],bin(27) [2:])
# print (bin(111)[2:], bin(81) [2:], bin(192) [2:],bin(0) [2:])

# 2
# for x in range(0,10):
#     for y in range(0,10):
#         s = "123"+str(x)+"4567"+str(y)+"28"
#         if int(s)%99==0:
#             print(x,y)
#             print(x**2+y**2)
#

# 3
# import math
# fact = 1
# for i in range(1, 75):
#     fact = fact * i
#
# fact1 = 1
# for i in range(1, 76):
#     fact1 = fact1 * i
#
# s = fact**3+fact1**3
# for i in range(1,s//2):
#     if s%i==0:
#         print(i)

# print(fact**3+fact1**3)

# 5
# for a in range(2,1000000000000000000000000):
#     s = (2531-a*1468)/(a-1)
#     #print(s)
#     if (s-int(s))==0:
#         print(s)
#         print(a)


# 9
# from math import *
# print(45*45)
# for a in range(1, 100):
#     for b in range(1, 100):
#         for c in range(1, 100):
#             if (c < a + b) and (a < b + c) and (b < a + c) and (c ** 2 == a ** 2 + b ** 2 + 2):
#                 p = (a + b + c)*(0.5)
#                 p = int(p)
#                 #print(p)
#                 s = (p * (p - a) * (p - b) * (p - c))
#                 print(s)
#                 s = int(s)
#                 if (s == 45**2):
#
#                     print((a ** 2) * (b ** 2))


# 8
# for i in range(0,1000):
#     a = 1000-i
#     if (a%3==2) and (a%5==4) and (a%7==1):
#         print(i)


# 10
# c = 0
# for i in range(1, 9901):
#     if (i + i + 100) % 107 == 0:
#         c += 1
# for i in range(1, 10000):
#     t = i + i + 1
#     if t % 107 == 0:
#         c += 1
# print(c)

# a = 1
# b = 2
# for i in range(2010):
#     k = a
#     l = b
#     a = (l+k)/2
#     b = (2/((1/k)+(1/l)))
#     print(a*b)
# print(a*b)
#
# for a in range(100,1000):
#     s1 = (a//100)+((a//10)%10)
#     s2 = ((a//10)%10)+(a%10)
#     e= max(s1,s2)
#     b = min(s1,s2)
#     g = str(e)+str(b)
#     if g=="126":
#         print(a)

#
# a = {0: "Б", 1: "В", 2: "Г", 3: "Д"}
# k = 0
# for i in range(0, len(a)):
#     for j in range(0, len(a)):
#         for g in range(0, len(a)):
#             for m in range(0, len(a)):
#                     k += 1
#                     if k == 244:
#                         print(a[i], a[j], a[g], a[m], end=" ")

# x = 16**15 - 4**13 +2**48 +15
# s = ''
# while x != 0:
#     s += str(x % 4)
#     x //= 4
# s = s[::-1]
# print(s.count("3"))

# def factorial(a):
#     s = 1
#     for i in range(1,a+1):
#         s=s*i
#     return s
# print(factorial(7))
# for n in range(1,100000):
#     for m in range(1,100000):
#         if factorial(n) * factorial(7) == factorial(m):
#             print(n,m)

#
# import math
#
#
# def divisorGenerator(n):
#     large_divisors = []
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i * i != n:
#                 large_divisors.append(n / i)
#     for divisor in reversed(large_divisors):
#         yield divisor
#
#
# for i in range(100, 1000):
#     s = list(divisorGenerator(i))
#
#     if len(s) == 8:
#         chet = 0
#         nechet = 0
#         for j in s:
#             if j % 2 == 0:
#                 chet += 1
#             else:
#                 nechet += 1
#         if chet==4 and nechet==4:
#             if sum(s)==1296:
#                 print(s)
#                 print(sum(s))
#                 print(i)
#

# print(13**13+13**14+13**15)
# print(55426144506382299%79)
# c = 0
# for i in range(100,1000):
#     j = i**2+i+1
#     if j%11==0:
#         c+=1
# print(c)

# a = int(input())
# if a%2==0:
#     print(a)
# else:
#     print(a-1)

s1h, s1m, f1h, f1m = list(map(int, input().split()))
s2h, s2m, f2h, f2m = list(map(int, input().split()))
if s1h > f1h:
    t1h = 24 - s1h - 1 + f1h
    t1m = 60 - s1m + f1m
    k = t1m
    t1h += t1m // 60
    t1m = k % 60
# print(t1h,t1m)

if s1h < f1h:
    t1h = f1h - s1h - 1
    t1m = 60 - s1m + f1m
    k = t1m
    t1h += t1m // 60
    t1m = k % 60
    # print(t1h,t1m)

if s2h > f2h:
    t2h = 24 - s2h - 1 + f2h
    t2m = 60 - s2m + f2m
    k = t2m
    t2h += t2m // 60
    t2m = k % 60
# print(t2h, t2m)

if s2h < f2h:
    t2h = f2h - s2h - 1
    t2m = 60 - s2m + f2m
    k = t2m
    t2h += t2m // 60
    t2m = k % 60
    # print(t2h,t2m)

min1 = t1h * 60 + t1m
min2 = t2h * 60 + t2m

a = max(min1, min2)
b = min(min1, min2)
p = a

i = 0
while (a - 60 * i) - (b + i * 60) >= 60:
    i += 1
    # a = a-60*i
    # b = b+i*60
    # break
a = a - 60 * i
b = b + i * 60

if p == min1:
    print(a // 60, a % 60)
    print(b // 60, b % 60)

if p == min2:
    print(b // 60, b % 60)
    print(a // 60, a % 60)
