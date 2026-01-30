'''
12865. <골드 5> 평범한 배낭
https://www.acmicpc.net/problem/12865
1차원 DP로 줄이기
'''

import sys
input = sys.stdin.readline

N, W = map(int, input().split())
arr = [] #[w, v]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0]*(W+1)

for w, v in arr: # 물품 수 0~100
    for std_w in range(W, w-1, -1): # 기준 무게 0~100,000
        dp[std_w] = max( dp[std_w], v + dp[std_w-w]  ) 
    # print(dp)

print(dp[-1])
        