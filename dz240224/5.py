a =int(input())
s1 = a//100
s2 = (a%100)//10
s3 = a%10
w1 = s1*s2
w2 = s2*s3
if w1<w2:
    print(str(w1)+str(w2))
else:
    print(str(w2)+str(w1))
    