n = int(input())
p1 =[]
a = 0
for i in range(n):
    p = int(input())
    p1.append(p)
for i in range(n):
    t = p1[i]
    c = 1
    while t!=-1:
        c+=1
        t = p1[t-1]
    a = max(c,a)
print(a)
