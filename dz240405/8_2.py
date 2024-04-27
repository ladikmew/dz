from itertools import *
a = list(permutations("ХОЧУНАБЮДЖЕТ",12))
b = list(permutations("ОУАЮЕ"),5)
c = 0
for i in a:
    for j in b:
        if "".join(j) not in "".join(i):
            c+=1
print(c)

#474163200