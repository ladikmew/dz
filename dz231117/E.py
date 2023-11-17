j = input()
s = input()
if len(j) != len(s):
    print(0)
else:
    if "".join(sorted(j)) == "".join(sorted(s)):
        print(1)
    else:
        print(0)
