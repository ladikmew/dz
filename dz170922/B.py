a = int(input())



def fib(f1,f2,k,n):
    while k < (a-1):
        sum = f1+f2
        f1 = f2
        f2 = sum
        k += 1
        n.append(f2)
#print(n)
#print()

k = 0
f = []
n = [1]
fib(1,1,k ,n)
n = set(n)
for i in range(1, a+1):
    #print(i)
    if i in n:
        f.append("O")
    else:
        f.append("o")

print("".join([str(el) for el in f]))



