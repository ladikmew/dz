n = int(input())
k = n-1
r = 0
jump = [0]*(n+k)
jump[0] = 1
for i in range(0,n):
    for j in range(2,k+1):
        jump[i+j]+=1
for i in range(1,n):
    r+=jump[i]
print(r)
