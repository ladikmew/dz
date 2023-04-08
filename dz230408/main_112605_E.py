 #прямой порядок
n,k = list(map(int,input().split()))
l = int(input())
lg = list(map(int, input().split()))
jump = [0]*(n+k)
for i in range(len(lg)):
    jump[int(lg[i])-1]=-1
jump[0] = 1
for i in range(1,n):
    if jump[i]!=-1:
        for j in range(1,k+1):
            if jump[i-j]!=-1:
                jump[i]+=jump[i-j]
print((jump[len(jump)-k-1]))
