'''
11660. <실버 1> 구간 합 구하기 5
https://www.acmicpc.net/problem/11660
'''

import sys
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
# 합 배열을 위한 패딩 적용
arr = [[0]*(N+1) for _ in range(N+1)]

# 값 입력
for i in range(1, N+1):
    arr[i][1:] = list(map(int, input().split()))
# pprint(arr)

# 합 배열
for x in range(1,N+1):
    for y in range(1,N+1):
        arr[x][y] += arr[x-1][y] + arr[x][y-1] - arr[x-1][y-1]
# pprint(arr)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print( arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1] )
