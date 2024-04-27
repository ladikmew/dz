from itertools import *

a = list(permutations("AAAABBBB",4))
d = set()

for i in range(len(a)):
    res = 1
    for j in a[i]:
        if j=="A":
            res +=2
        else:
            res *=3
    d.add(res)

print(len(d))
