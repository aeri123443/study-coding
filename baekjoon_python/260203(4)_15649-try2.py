'''
15649. <실버 3> N과 M (1)
https://www.acmicpc.net/problem/15649
백트래킹으로 풀어보기
'''

import sys
from pprint import pprint

input = sys.stdin.readline

N, M = map(int, input().split())

path = []
visited = [False]*(N+1)

def permutation(num):
    # print(path, num)

    if num == M:
        print(' '.join(map(str, path)))
        return 
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)

            permutation(num+1)

            # 백트래킹!
            visited[i] = False
            path.pop()

permutation(0)