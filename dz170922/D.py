a = int(input())
x = input().split()
y = input().split()
x+=y
for i in range(len(x)):
    x[i] = int(x[i])
f = 0
x = set(x)
#print(x)
for i in range(1,a+1):
    if i in x:
        f+=1
#print(f)
if f!=a:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")
