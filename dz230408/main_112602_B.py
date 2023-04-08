#прямой порядок
# сложность O(n)
# память O(n)
n = int(input())
jump = [0]*(n+1)
jump[0] = 1
jump[1] = 1
for i in range(1,n-1):
    jump[i+1]+=(jump[i]+jump[i-1])
print(jump[len(jump)-2])
