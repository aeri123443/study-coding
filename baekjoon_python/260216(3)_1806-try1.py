'''
1806. <골드 4> 부분합
https://www.acmicpc.net/problem/1806
'''

import sys

input = sys.stdin.readline

INF = float('inf')
N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = INF

i = j = 0
total = arr[0]
while i < N and j < N:
    l = j-i+1
    if total < S:
        # 슬라이딩이 잡고 있는 범위가 answer len보다 1 작으면, 
        # j만 늘리지 말고 i,j를 같이 늘려서 범위 길이를 유지
        if l == answer - 1:
            total -= arr[i]
            i += 1
        j+=1
        if j >= N: break
        total += arr[j]
    else:
        answer = min(answer, l)
        total -= arr[i]
        i += 1

print(answer if answer<INF else 0)
