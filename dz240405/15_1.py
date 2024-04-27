def f(x,n):
    return (x%n==0) or ((x%23==0) <= (not(x in range(50,71))))
for A in range(1,10001):
    c = 0
    for x in range(1,1001):
        if f(x,A)==1:
            c+=1
    if c==1000:
        print(A)

