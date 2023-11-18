# def partition(n, x):
#     h = []
#     if len(n) < 1:
#         return [0,0]
#     l_n = [j for j in n if j < x]
#     b_n = [i for i in n if i >= x]
#     h.append(len(l_n))
#     h.append(len(b_n))
#     return h
#
# k = int(input())
# n = list(map(int, input().split()))
# x = int(input())
# print(partition(n, x)[0])
# print(partition(n, x)[1])a
a = int(input())
b = int(input())
print(a**b)