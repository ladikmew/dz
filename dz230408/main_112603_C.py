#прямой порядок
#сложность O(n^2)
n,k = list(map(int,input().split()))
l = k
jump = [0]*(n+k)
jump[0] = 1
for i in range(1,n):
    for j in range(1,k+1):
        jump[i]+=jump[i-j]
print((jump[len(jump)-k-1]))
