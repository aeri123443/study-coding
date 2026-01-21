'''
15654. <실버 3> N과 M(5)
https://www.acmicpc.net/problem/15654
'''

import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
iter = list(map(int, input().split()))
# print(iter)

com_arr = sorted(list(permutations(iter, M)))
# print(com_arr)

for tu in com_arr:
    print(' '.join(map(str,tu)))