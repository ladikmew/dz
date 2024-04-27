#2
# for x in range(0,2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = (x and not(y)) or (y == z) or not(w)
#                 if f==0:
#                     print(x,y,z,w)

#5
# for n in range(1,1000):
#     n1 = bin(n)[2:]
#     if n%3==0:
#         k = n1[-3:]
#         if len(k)<3:
#             k = "0"+n1[-3:]
#         n1 = n1+k
#     else:
#        n1+= bin((n%3)*3)[2:]
#     r = int(n1,2)
#     if r>151:
#         print(r)

# #6
# from turtle import *
# left(90)
#
# pendown()
# k = 10
# for i in range(2):
#     forward(8*k)
#     right(90)
#     forward(18*k)
#     right(90)
# penup()
# forward(4*k)
# right(90)
# forward(10*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(17*k)
#     right(90)
#     forward(7*k)
#     right(90)
# penup()
# tracer(0)
# for x in range(-20*k,20*k,k):
#     for y in range(-20*k, 20*k,k):
#         goto(x,y)
#         dot(3)
# done()

#7
# print((1024*12*768*256)/(1024*8))
# print(12*768*32)

#14
# from string import digits, ascii_uppercase
# ss = digits+ascii_uppercase
# for i in range(19):
#     g =  int(f'98897{ss[i]}21',19)+int(f'2{ss[i]}923',19)
#     if g%18==0:
#         print(g//18)
#         print(ss[i])
#         break

#12
# s = '5'
# for n in range(3,10000):
#     s +='2'*n
#     while '52' in s or '22221' in s or '1122' in s:
#         if '52' in s:
#             s = s.replace('52','11')
#         elif '2222' in s:
#             s = s.replace('2222','5')
#         elif '1122' in s:
#             s = s.replace('1122','25')
#     res = 0
#     for i in s:
#         res+=int(i)
#     if res==64:
#         print(n)
#

#11
#
# print((68*65536)/1024)

#13
# print(bin(192)[2:],bin(168)[2:],bin(32)[2:],bin(160)[2:],bin(240)[2:])

#16
# print(2023*2022)

#21
# def f(x,y):
#     if x==y:return 1
#     if x>y or x==11:return 0
#     if x<y: return f(x+1,y)+f(x*2,y)+f(x**2,y)
# print(f(2,20))

#25
from fnmatch import *
for i in range(0,10000000000,2024):
    if fnmatch(str(i),'1?2157*4'):
       # print()
        if i%2024==0:
             print(i,i//2024)