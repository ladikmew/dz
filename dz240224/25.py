# n = int(input())
# max_del = 0
# for i in range(n, n + 101):
#     s = 1
#
#
#     def primfacs(n):
#         i = 2
#         primfac = []
#         while i * i <= n:
#             while n % i == 0:
#                 primfac.append(i)
#                 n = n / i
#             i = i + 1
#         if n > 1:
#             primfac.append(n)
#         return primfac
#
#
#     all_prost = primfacs(i)
#     prost = set(all_prost)
#     for j in prost:
#         s = s * ((all_prost.count(j) + 1))
#     if max_del < s:
#         max_del = s
#         res = i
# print(res)
