'''
11659. <실버3> 구간 합 구하기 4
https://www.acmicpc.net/problem/11659

시간초과 오류가 나는 코드 예시
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())

    sum_num = 0
    for idx in range(i-1, j):
        sum_num += arr[idx]
    print(sum_num)