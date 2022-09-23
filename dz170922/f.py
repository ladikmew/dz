a = input().split()
n = int(a[0])
k = int(a[1])
s = input().split()
f = 0
for i in range(0,n):
    if int(a[i])>k:
        f+=1
        break
for j in range(n-1, i+1, -1):
    if int(a[i]) > k:
        f += 1
        break
print(f)

