# from string import *
# alf = ('0123456789' + ascii_uppercase)[:25]
# for x in alf:
#     y1 = int(f'1{x}2{x}3{x}4{x}5', 25)
#     y2 = int(f'2{x}024', 25)
#     y3 = int(f'1{x}099', 25)
#     if (y1 + y2 + y3) % 24 == 0:
#         xm = (y1 + y2 + y3) // 24
# print(xm)

# def f(x,y,a):
#     return (x < 4) or (x >= 20) or (y >= 3 * x + a) or (y < 100)
#
# for a in range(1000, 0, -1):
#     if all(f(x,y,a) for x in range(2000) for y in range(2000)):
#         print(a); break\

# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n == 2: return 2
#     return n * (n - 1) + f(n - 1) + f(n - 2)
#
# for n in range(1, 2024): f(n)
# print(f(2024) - f(2022) - 2 * f(2021) - f(2020))

# def f(x): return 1000 <= abs(x) < 10000
# a = [int(x) for x in open('17var03.txt')]
# mx = max(x for x in a if abs(x) % 100 == 90)
# ans = []
# for i in range(2, len(a)):
#      if f(a[i - 2]) + f(a[i - 1]) + f(a[i]) > 0:
#          if sum(a[i - 2 : i + 1]) > mx:
#              ans.append(sum(a[i - 2 : i + 1]))
# print(len(ans), min(ans))

# f = open('17var09.txt')
# nums = list(map(int, f.readlines()))
#
# pairs = 0
# max_sum = -20000
#
# for i in range(1, len(nums)):
#     if nums[i-1] > 0 and int(nums[i-1]**0.5) ** 2 == nums[i-1] or \
#         nums[i] > 0 and int(nums[i]**0.5) ** 2 == nums[i]:
#             pairs += 1
#             max_sum = max(max_sum, nums[i-1] + nums[i])
#
# print(pairs, max_sum)
#
# def f(x, y):
#     if x == y: return 1
#     if x > y or x == 6 or x == 17: return 0
#     return f(x + 2, y) + f(x + 3, y) + f(x * 5, y)
# print(f(1, 31))

f = open("26 вар3.txt")
data = []
for s in f:
    y_l, len_sq = map(int, s.split())
    data.append([y_l + len_sq, y_l])
data.sort()

podoshel = [data[0]]
max_dist = 0
for r_y, l_y in data[1:]:
    if l_y >= podoshel[-1][0]:
        podoshel.append([r_y,l_y])
    if len(podoshel) == 29 and l_y >= podoshel[-2][0]:
        max_dist = max(max_dist,l_y - podoshel[-2][1])

print(len(podoshel), max_dist)