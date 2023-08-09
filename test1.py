
# s1 = "HRW"
# s2 = "HERHRWS"
#
# s3 = []
#
#
# for n, i in enumerate(s2):
#     for m, j in enumerate(s2[n+1::]):
#         for p, k in enumerate(s2[n+1::][m+1::]):
#             try:
#                 s4 = f"{i}{j}{k}"
#                 s3.append(s4)
#             except IndexError:
#                 pass
#
# print(s3.count(s1))
# def is_leap(year):
#     leap = False
#
#     if year % 4 == 0:
#         leap = True
#         if year % 100 == 0:
#             leap = False
#             if year % 400 == 0:
#                 leap = True
#     return leap
#
#
# year = int(input())
# print(is_leap(year))

import numpy as np

a = int(input())
b = []
for i in range(a):
    b.append([float(i) for i in input().split(' ')])

print(np.linalg.det(b))

