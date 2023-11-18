file = open('24.txt')
s = file.readline().strip()
l, r = 0, -1
c_A, c_B = 0, 0
ans = -1
while True:
    if c_A > 1 or c_B > 1:
        l += 1
        if s[l - 1] == "A":
            c_A -= 1
        if s[l - 1] == "B":
            c_B -= 1
    else:
        r += 1
        if r == len(s):
            break
        if s[r] == "A":
            c_A += 1
        if s[r] == "B":
            c_B += 1
    if c_A == 1 and c_B == 1:
        ans = max(ans, r - l + 1)
print(ans)
#182


