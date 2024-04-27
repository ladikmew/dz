# def f(x,A):
#     return (((x%A==0) and (x%45==0))<=(x%162==0)) and (A>200)
# for A in range(500,0,-1):
#     if all([f(x,A) for x in range(1,1001)])==True:
#         print(A)

def f(x, A):
    return (((x % A == 0) and (x % 45 == 0)) <= (x % 162 == 0)) and (A > 200)


for A in range(1, 1001):
    c = 0
    for x in range(1, 1001):
        if f(x, A) == 1:
            c += 1
    if c == 1000:
        print(A)
