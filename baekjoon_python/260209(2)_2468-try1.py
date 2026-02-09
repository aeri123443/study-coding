'''
2468. <실버 1> 안전 영역
https://www.acmicpc.net/problem/2468
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline
# sys.setrecursionlimit(int(1e6))

N = int(input())
board = []
visited = [ [False]*N for _ in range(N) ] 
max_h = 0
move = [(1,0), (-1,0), (0,1), (0,-1)]

# 방문 가능 여부 확인
def can_move(i,j,h):
    if 0<=i<N and 0<=j<N and not visited[i][j] and board[i][j]>h:
        return True
    else:
        return False

# 그룹 확인 bfs
def group(si, sj, h):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True

    while q:
        ci, cj = q.popleft()
        for di, dj in move:
            ni, nj = ci+di, cj+dj

            if can_move(ni, nj, h):
                visited[ni][nj] = True
                q.append((ni,nj))

# board 입력
for _ in range(N):
    tmp = list(map(int, input().split()))
    max_h = max(max_h, max(tmp))
    board.append(tmp)
# print(max_h)    
# pprint(board)

answer = 0
for h in range(max_h+1):
    # visited 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    g_num = 0    
    # 그룹 확인
    for i in range(N):
        for j in range(N):
            if can_move(i, j, h):
                g_num+=1
                # print(i, j, h, g_num)
                group(i, j, h)
    # print(h, g_num)
    answer = max(answer, g_num)
    # status 업데이트

print(answer)