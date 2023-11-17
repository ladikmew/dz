from itertools import *
s = ""
n = int(input())
for i in range(n):
    s += ")"
    s += "("
#print(s)
a = 0
b = 0
for i in permutations(s):
    if i=="(":
        if a == b:
            print("".join(i))
        a+=1
    else:
        b+=1
    d = "".join(i)
    print(d)
