'''
13458. <브론즈 2> 시험 감독
https://www.acmicpc.net/problem/13458
'''

import sys
import math
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

# print(N, B, C)
# print(students)

answer = 0
for st in students:
    # print()
    if st > B:
        # print(st-B, (st-B)/C, math.ceil((st-B)/C), math.ceil((st-B)/C) + 1)
        answer += (math.ceil((st-B)/C) + 1)
        # print(math.ceil((st-B)/C) + 1)
    else:
        answer += 1
        # print(1)

print(answer)

