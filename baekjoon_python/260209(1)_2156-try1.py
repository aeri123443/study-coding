'''
2156. <실버 1> 포도주 시식
https://www.acmicpc.net/problem/2156
'''

# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
import sys

N = int(sys.stdin.readline())
arr = [0,0,0] + [ int(input()) for _ in range(N)]
dp = [0]*(N+3)
# print(arr)

for n in range(3, N+3):
    # n = i + 3
    # print('dp', dp)
    # print(i, n)
    dp[n] = max(
        dp[n-2] + arr[n],
        dp[n-3] + arr[n-1] + arr[n],
        dp[n-1],
    )

print(max(dp))