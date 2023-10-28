r = int(input())
g = str(r)
a = []
b_r = bin(r)[2:]
for char in b_r:
    a.append(int(char))
if sum(a)%2==0:
    a.append(0)
    a[0] = 1
    a[1] = 0
    n = int(''.join(map(str, a)))

    print(int(str(n),2))
else:
    a.append(1)
    a[0] = 1
    a[1] = 1
    n = int(''.join(map(str, a)))
    print(int(str(n), 2))
