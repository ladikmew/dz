# f = open("27_B.txt")
# n, v = map(int, f.readline().split())
# a = []
# for i in range(n):
#     s, k = map(int, f.readline().split())
#     if k % v == 0:
#         c = k//v
#     else:
#         c = k//v + 1
#     a.append([s, c])
# a.sort()
#
# bags = [0]*n
# bags[0] = a[0][1]
# for i in range(1,n):
#     bags[i] = bags[i-1] + a[i][1]
#
# s = 0
# for j in range(n):
#   s += abs(a[0][0]-a[j][0])*a[j][1]
#
# min_sum = s
# for i in range(1,n):
#     diff = a[i][0] - a[i-1][0]
#     s = s + diff*bags[i-1] - diff*(bags[n-1]-bags[i-1])
#     min_sum = min(min_sum,s)
#
# print(min_sum)

import math

f=open('27_A.txt')

k=9999995

n=int(f.readline())

a=[0]*k

sm=0

for i in range(n):
    x, y = f.readline().split()
    x=int(x)
    y=int(y)
    z = math.ceil(y/36)
    a[x] = z
    sm = sm + (x-1)*z

# Вспомогательные суммы
s1=[]
s2=[]
s1.append(0)
s2.append(0)
s1.append(0)
s2.append(0)

for i in range(1, k):
    s1[1] = s1[1] + a[i]


for i in range(2, k):
    s1.append(s1[i-1] - a[i-1])
    s2.append(s2[i-1] + a[i-1])

# Ищем минимальное значение
mn=sm

for i in range(2,  k):
    sm = sm - s1[i] + s2[i]
    mn=min(mn, sm)

print(mn)