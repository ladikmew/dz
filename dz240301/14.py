def primfacs(n):
    for i in range(2,n//2):
        if n%i==0:
            return 1
    return 0
c = 0
for i in range(1,100000000):
    f = (5*(18**3)+6*(18**2)+i*(18**1)+3*(18**0))+(6*(18**2)+i*(18**1)+3*(18**0))-(5*(18**3)+7*(18**2)+i*(18**1)+1*(18**0))
    if primfacs(f)==0:
        c+=1
print(c)