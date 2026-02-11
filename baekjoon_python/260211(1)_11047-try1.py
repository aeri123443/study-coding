'''
11047. <실버 4> 동전 0
https://www.acmicpc.net/problem/11047
'''

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [ int(input()) for _ in range(N)]

answer = 0
while K > 0 :
    v = arr.pop()
    if K >= v:
        answer += (K//v)
        K = (K%v)

print(answer)