gl = ["A","O"]
sogl = ["C","D","F"]
f = open("24.txt")
a = f.read()
k = 0
kmax = 0
print(a)
for i in range(0,len(a)-1,2):
    if a[i] in sogl and a[i+1] in gl:
        k += 1
        kmax = max(k, kmax)
    else:
        k = 0
print(kmax)
