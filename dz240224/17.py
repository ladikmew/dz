f = open('17.txt')
s = f.readlines()
for i in range(len(s)):
    s[i] = int(s[i])
count = 0
maxi = 0
mini = 0
for i in range(len(s)):
    if abs(s[i]) % 10 == 7:
        mini = min(mini, s[i])
for i in range(1, len(s)):
    if abs(s[i-1]) % 10 == abs(s[i]) % 10:
        if abs(s[i-1]) % 7 == 0 and abs(s[i]) % 7 != 0 and s[i-1]**2 + s[i]**2 <= mini**2:
            count+=1
            maxi=max(maxi, s[i-1]**2 + s[i]**2)
        elif abs(s[i]) % 7 == 0 and abs(s[i-1]) % 7 != 0 and s[i-1]**2 + s[i]**2 <= mini**2:
            count+=1
            maxi=max(maxi, s[i-1]**2 + s[i]**2)
print(count, maxi)