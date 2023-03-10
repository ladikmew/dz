s = []
for i in range(int(input())):
    d = list(map(int, input().split()))
    h = sum(d) // 9
    if sum(d) % 9 == 0 and min(d) >= h:
        s.append("YES")
    else:
        s.append("NO")
for sh in s:
    print(sh)
