from itertools import *
c = 0
for i in product('АГЛОЬ', repeat=5):
    c+=1
    print(c,i)
    if i=="ОЛЬГА":
        print(c)