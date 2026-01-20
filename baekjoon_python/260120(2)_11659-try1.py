'''
11659. <실버3> 구간 합 구하기 4
https://www.acmicpc.net/problem/11659
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 합 배열 생성
sum_arr = [-1]*N
sum_arr[0] = arr[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1] + arr[i]
# pprint(sum_arr)

# 구간합 구하기
for _ in range(M):
    i, j = map(int, input().split())
    # print(i, j, sum_arr[j-1], sum_arr[i-2])
    if i==1:
        print(sum_arr[j-1])
    else:
        print(sum_arr[j-1]-sum_arr[i-2])
        