'''
2178. <실버 1> 미로 탐색
https://www.acmicpc.net/problem/2178
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
visited = [[0]*M for _ in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0)]

for _ in range(N):
    board.append( list(map(int, list(input().strip()))) )
# pprint(board)
# pprint(visited)

# 방문 가능 여부

q = deque()
# cnt, node(x,y)
q.append([1, (0,0)])
visited[0][0] = 1

while q:
    cnt, (cx, cy) = q.popleft()

    for (dx,dy) in move:
        nx, ny = dx+cx, dy+cy
        # if cnt>=6: print(cx, cy, nx,ny)
        if 0<=nx<M and 0<=ny<N and visited[ny][nx]==0 and board[ny][nx]==1:
            visited[ny][nx] = cnt+1
            # print('append', nx, ny)
            q.append([cnt+1, (nx,ny)])

print(visited[-1][-1])
