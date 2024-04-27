from itertools import *
import math

def prost(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False
max = 0
l = 0

for n in range(100,1000):
    s = str(n)
    a = list(permutations(s,2))
    c = 0
    for i in a:
        if int(i[0])!=0:
            d = int(i[0])*10+int(i[1])

            if prost(d):
                c+=1
    if c>=max:
        max = c
        res = n
print(res)

