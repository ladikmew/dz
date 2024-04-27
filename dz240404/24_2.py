s = open('24.txt').readline()
k = 0
mx = 0
i = 0
while i < len(s) - 1:
    if s[i:i + 2] == 'PC':
        k += 2
        i += 2
    elif s[i:i + 4] == 'CSGO':
        k += 4
        i += 4
    elif i > 0 and s[i - 1:i + 3] == 'CSGO':
        k = 4
        i += 3
    else:
        k = 0
        i += 1
    mx = max(mx, k)
print(mx)