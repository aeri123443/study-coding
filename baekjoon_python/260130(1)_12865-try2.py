'''
12865. <골드 5> 평범한 배낭
https://www.acmicpc.net/problem/12865
'''

import sys
input = sys.stdin.readline
# from pprint import pprint

N, W = map(int, input().split())
arr = [] #[w, v]
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0]*(W+1) for _ in range(N)]
# pprint(arr)

# dp 첫열 미리 작성 (첫행은 모두 0)
w, v = arr[0]
dp[0] = [ v if i >= w else 0 for i in range(W+1) ]
# pprint(dp)
print(dp[0])
for item_num in range(1, N): # 물품 수 0~100
    w, v = arr[item_num]
    # print(w, v)
    for std_w in range(1, W+1): # 기준 무게 0~100,000
        
        if w > std_w:
            dp[item_num][std_w] = dp[item_num-1][std_w]
        else:
            dp[item_num][std_w] = max( dp[item_num-1][std_w], v + dp[item_num-1][std_w-w]  )
    print(dp[item_num])
# pprint(dp)
print(dp[-1][-1])
        
    