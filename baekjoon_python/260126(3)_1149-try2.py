'''
1149. <실버 1> RGB거리
https://www.acmicpc.net/problem/1149
DP로 풀기
'''

import sys
input = sys.stdin.readline

N = int(input())
houses = []
# R:0, G:1, B:2
for _ in range(N):
    houses.append( list(map(int, input().split())) )
# print(houses)

dp = [[0]*3 for _ in range(N)]
dp[0] = houses[0][:]
for i in range(1, N):
    dp[i][0] = houses[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = houses[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = houses[i][2] + min(dp[i-1][0], dp[i-1][1])
print(min(dp[-1]))
