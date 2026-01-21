'''
15650. <실버 3> N과 M(2)
https://www.acmicpc.net/problem/15650
'''

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
iter = [i+1 for i in range(N)]
# print(iter)

com_arr = list(combinations(iter, M))
# print(com_arr)

for tu in com_arr:
    print(' '.join(map(str,tu)))