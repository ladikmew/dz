from collections import deque
a = int(input())
e = []
for i in range(a):
    n = int(input())
    s = input().split()
    t = input().split()
    rez = []
    r = 0
    for i in range(len(s)):
        if int(r) <= int(s[i]):
            rez.append(int(t[i]) - int(s[i]))
        else:
            rez.append(int(t[i]) - int(r))
        r = t[i]
    # print(str(rez))
    e.append(" ".join(map(str, rez)))
for i in e:
    print(i)
