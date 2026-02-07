'''
10844. <실버 1> 쉬운 계단 수
https://www.acmicpc.net/problem/10844
dp
'''

import sys
from pprint import pprint

N = int(sys.stdin.readline())

# 매핑 (이전수-다음수)
mapping = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8]]
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
# pprint(dp)

for n in range(2, N+1):
    for i in range(10):
        for nxt in mapping[i]:
            dp[n][i] += dp[n-1][nxt]

# pprint(dp)
print(sum(dp[-1]) % 1000000000)
