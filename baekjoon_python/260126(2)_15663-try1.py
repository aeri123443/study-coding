'''
15663. <실버 2> N과 M (9)
https://www.acmicpc.net/problem/15663
'''

import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# print(arr)
per = sorted(set(permutations(arr, M)))
for x in per:
    print(' '.join(map(str, x)))
