'''
2805. <실버2> 나무 자르기
https://www.acmicpc.net/problem/2805
시간 초과
'''
from pprint import pprint

import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
# print(arr)

# 나무 간 높이 차이
target_height = 0
target_sum = 0
for i in range(1, N):
    temp_target = arr[i]
    temp_sum = 0
    # 2
    for j in range(N):
        if arr[j] > temp_target:
            temp_sum += arr[j] - temp_target
        else:
            break
    # print(temp_sum, arr[j])
    # 3
    if temp_sum >= M:
        # print('here', target_height, target_sum, j)
        break
    else:
        target_height = arr[j]
        target_sum = temp_sum
# 4
print( target_height - math.ceil((M-target_sum)/(j)) )