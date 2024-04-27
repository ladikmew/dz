# for x in range(0,2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f =  (x and not(y)) or (y == z) or w
#                 if f==0:
#                     print(x,y,z,w)
# print(sum(map(int,"123")))
#
# for i in range(1,5):
#     res = ''
#     while i>0:
#         res+=str(i%3)
#         i = i//3
#     print(res[::-1])

# for n in range(1,1000):
#     n1 = bin(n)[2:]
#     n2 =n1 + str(n1.count("1")%2)
#     n3 = n2 + str(n2.count("1")%2)
#     r = int(n3,2)
#     if r>105:
#         print(n)
#         break

# for n in range(1,10000):
#     n2 = bin(n)[2:]
#     if n%2==0:
#         n2+='00'
#     else:
#         n2+="11"
#     r = int(n2,2)
#     if r<134:
#         print(n)
# a = []
# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     if n%2==0:
#         n2 = "1"+n2+"0"
#     else:
#         n2 = "11"+n2+'11'
#     r = int(n2,2)
#     if r>48:
#         a.append(r)
# print(min(a))

# for n in range(1,1000):
#     n2 = bin(n)[2:]
#     n2+=str(n2.count("1")%2)
#     n2+=str(n2.count("1")%2)
#     r = int(n2,2)
#     if r>45:
#         print(n)
#         break

# for n in range(100,1000):
#     v = str(n)
#     v1 = int(v[0])*int(v[1])
#     v2 = int(v[1])*int(v[2])
#     v3 = str(min(v1,v2))+str(max(v1,v2))
#     if v3=='615':
#         print(n)
# for n in range(100,1000):
#     s = list(str(n))
#     s.sort(reverse=True)
#     smax = s[0]+s[1]
#     s.sort()
#     if s[0]=="0":
#         smin = s[1]+s[2]
#     elif s[1]=="0" and s[0]=="0":
#         smin = s[2]+s[0]
#     r = int(smax)-int(smin)
#     if r == 70:
#         print(n)

# def tri(n):
#     res = ""
#     while n>0:
#         res+=str(n%3)
#         n//=3
#     return res[::-1]
#
# for n in range(1,1000):
#     l = tri(n)
#     if n%3==0:
#         l+=l[-3:]
#     else:
#         l+=tri((n%3)*3)
#     r = int(l,3)
#     if r<76:
#         print(n)
#
# def tri(n):
#     res = ""
#     while n>0:
#         res+=str(n%3)
#         n//=3
#     return res[::-1]
# for n in range(1,1000):
#     l = tri(n)
#     if n%3==0:
#         l = '1'+l+"02"
#     else:
#         ost = (n%3)*4
#         l = l+tri(ost)
#     r = int(l,3)
#     if r<199:
#         print(n)
def ter(n):
    t = ''
    while n > 0:
        t = str(n % 3) + t
        n //= 3
    return t
mx = 0
for n in range(1, 30):  
    s = ter(n)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        s += ter(n % 3 * 4)
    r = int(s, 3)
    if r < 199:
        mx = n
print(mx)