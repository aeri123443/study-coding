'''
11053. <실버 2> 가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
memo = [0]*N

for i in range(N):
    # print(i)
    if i==0:
        memo[i] = 1
        continue
    # 내 값보다 작은 수 반환
    small_len = []
    for j in range(0, i):
        if arr[j] < arr[i]:
            small_len.append(memo[j])
    # print(small_len)
    if small_len:
        memo[i] = max(small_len)+1
    else:
        memo[i] = 1
    # print(memo)

print(max(memo))