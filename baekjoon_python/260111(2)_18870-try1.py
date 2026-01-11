'''
18870. <실버2> 좌표 압축
https://www.acmicpc.net/problem/18870
'''

import sys
input = sys.stdin.readline

N = int(input())
input_arr = list(map(int, input().split()))

# 매핑하기
nums = sorted(set(input_arr))
mapping = {v:i for i,v in enumerate(nums)}
# print(nums)
# print(mapping)
for x in input_arr:
    print(mapping[x], end=' ')