'''
1920. <실버 4> 수 찾기
https://www.acmicpc.net/problem/1920
'''

import sys
from pprint import pprint

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
target_arr = list(map(int, input().split()))

def binary_search(target):
    si, ei = 0, N-1
    while si <= ei:
        mid_idx = ( si + ei ) // 2
        mid = arr[mid_idx]

        if target < mid :
            ei = mid_idx-1
        elif target > mid :
            si = mid_idx+1
        else : # target == mid
            return 1
    return 0

# 정렬 후 이분탐색
arr.sort()
for target in target_arr:
    print(binary_search(target))
