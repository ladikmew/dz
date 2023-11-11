from itertools import *
c = 0
for i in product('АВЕСТ', repeat=5):
    c+=1
    print(c,i)
    if i=="СВЕТА":
        print(c)