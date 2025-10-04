'''
11659. <실버3> 구간 합 구하기 4
https://www.acmicpc.net/problem/11659
'''
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]
for i in range(N):
    dp.append(dp[i] + nums[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])