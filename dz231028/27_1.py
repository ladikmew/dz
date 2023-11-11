import math
file = "27_A.txt"
# while True:
#     a = f.readline()
#     print(a)
# # for i in range(1,len(a),2):
# #     print(a[i])
s = []
p = []
t = []
b = []

with open(file) as f:
    for i, k in enumerate(f):
        if i:
            s1, p1 = [int(j) for j in k.split()]
            s.append(s1)
            t.append(p1)
            p.append(math.ceil(p1/36))
b.append( sum(s) - 2 * int(s[0]) * int(p[0]) + int(s[0])*(2 * int(p[0]) - sum(p)))
for i in range(1, len(s)):
    b1 = b[i - 1] + (s[i] - s[i - 1]) * 2 * sum(p[:i - 1])
    b.append(b1)
print(s)
print(t)
print(p)
print(min(b))
