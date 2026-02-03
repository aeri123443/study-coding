'''
11404. <골드 4> 플로이드
https://www.acmicpc.net/problem/11404
dp(폴로이드)로 풀어보기
'''

import sys
from pprint import pprint

input = sys.stdin.readline

N, M = int(input()), int(input())
dp = [[float('inf')]*(N+1) for _ in range(N+1)]

# 전체 맵 1차 업데이트 
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)
# pprint(dp)

# 자기 자신으로 가는 비용은 0으로
for city in range(1, N+1):
    dp[city][city] = 0
# pprint(dp)

for mid_city in range(1, N+1):
    for start_city in range(1, N+1):
        for end_city in range(1, N+1): 
            dp[start_city][end_city] = min(dp[start_city][end_city], 
                                           dp[start_city][mid_city] + dp[mid_city][end_city])
# pprint(dp)
        
# 갈 방법이 없는 경우는 0으로 처리, 이후 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == float('inf'):
            dp[i][j] = 0
    print(' '.join(map(str, dp[i][1:])))
