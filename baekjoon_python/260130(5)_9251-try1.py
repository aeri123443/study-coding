'''
9251. <골드 4> LCS
https://www.acmicpc.net/problem/9251
'''

import sys
from pprint import pprint

input = sys.stdin.readline

s1 = [0] + list(input().strip())
s2 = [0] + list(input().strip())
n1, n2 = len(s1), len(s2)

dp = [[0]*(n2) for _ in range( (n1)  )]

# print(s1, s2)
# pprint(dp)

for i in range(1, n1):
    for j in range(1, n2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
            
