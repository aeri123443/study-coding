'''
1149. <실버 1> RGB거리
https://www.acmicpc.net/problem/1149
DP에서 메모리 더 줄이기!!
'''

import sys
input = sys.stdin.readline

N = int(input())
prev = list(map(int, input().split()))
# R:0, G:1, B:2

for _ in range(1, N):
    r, g, b = map(int, input().split())
    prev = [
        r + min(prev[1], prev[2]),
        g + min(prev[0], prev[2]),
        b + min(prev[0], prev[1])
    ]

print(min(prev))