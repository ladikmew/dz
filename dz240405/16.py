def F(n):
    if n>10:
        return F(n-1)+3*F(n-3)+2
    elif n%2==0:
        return-1
    else:
        return 1
print(F(20))
