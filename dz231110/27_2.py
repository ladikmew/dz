f = open("27_A.txt")
n= int(f.readline())
v = 36
a = []
for i in range(n):
    s, k = map(int, f.readline().split())
    if k % v == 0:
        c = k//v
    else:
        c = k//v + 1
    a.append([s, c])
a.sort()

bags = [0]*n
bags[0] = a[0][1]
for i in range(1,n):
    bags[i] = bags[i-1] + a[i][1]

s = 0
for j in range(n):
  s += abs(a[0][0]-a[j][0])*a[j][1]

min_sum = s
for i in range(1,n):
    diff = a[i][0] - a[i-1][0]
    s = s + diff*bags[i-1] - diff*(bags[n-1]-bags[i-1])
    min_sum = min(min_sum,s)

print(min_sum)