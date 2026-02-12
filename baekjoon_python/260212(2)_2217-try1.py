'''
2217. <실버 4> 로프
https://www.acmicpc.net/problem/2217
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + sorted([int(input()) for _ in range(N)], reverse=True)
# print(arr)

max_w = 0
for i, v in enumerate(arr):
    max_w = max(max_w, i*v)

print(max_w)