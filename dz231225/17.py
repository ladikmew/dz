f = open("17 (1).txt")
n1=int(f.readline())
n2=int(f.readline())
print(n1,n2)

for s in f.readlines():
    n3 = int(s)
    print(n3)