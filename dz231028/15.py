# for A in range(1, 10000):
#     f = True
#     for x in range(5, (4095 + 1)*2 + 1, 2):
#         for y in range(2, 4095 + 1, 2):
#             if x*y % A == 0:
#                 f = False
#                 break
#         if not f:
#             break
#     if f:
#         print(A)
#         break