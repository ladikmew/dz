s = "AFATGBADHJBADFAT"
mn = len(s)
s = s.replace("BAD", "*").replace("FAT", "*")
last1 = -1
last2 = -1
for i in range(len(s)):
    if s[i] == '*':
        if last2 != -1:
            mn = min(mn, i - last2 + 7)
        last2 = last1
        last1 = i
print(mn)