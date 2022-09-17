a = int(input())
x = input().split()
y = input().split()
f = 0
k = [int(x[0])]
x = x + y
s = 0
for i in range(len(x)):
    x[i] = int(x[i])
x = set(x)
print(x)
for i in range(1, a+1):
    if i in x:
        f += 1
    else:
        s += 1
        print("*", f)
        print("!", s)
if s != 0:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")




