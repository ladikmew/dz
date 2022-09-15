f1 = 1
f2 = 1
a = int(input())
k = 0
while k < (a-2):
    summ = f1+f2
    f1 = f2
    f2 = summ
    k+=1
print(f2)