'''
1987. <골드 4> 알파벳
https://www.acmicpc.net/problem/1987
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

INF = float('inf')
N, M = map(int, input().split())
move = [(0,1), (0,-1), (1,0), (-1,0)]
board = [ list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
alpha_used = set()
# pprint(board)
# pprint(visited)

q = deque( (0,0) )
visited[0][0] = 1

max_cnt = 0
def dfs(ci, cj, cnt):
    global max_cnt
    # print(ci, cj, board[ci][cj],cnt)
    max_cnt = max(max_cnt, cnt)

    if max_cnt==26:
        return
    
    for di, dj in move:
        ni, nj = ci+di, cj+dj
        
        if (0<=ni<N and 0<=nj<M) and (not visited[ni][nj]) and (not board[ni][nj] in alpha_used):
            visited[ni][nj] = True
            alpha_used.add(board[ni][nj])

            dfs(ni, nj, cnt+1)

            visited[ni][nj] = False
            alpha_used.remove(board[ni][nj])

visited[0][0] = True
alpha_used.add(board[0][0])
dfs(0, 0, 1)

print(max_cnt)