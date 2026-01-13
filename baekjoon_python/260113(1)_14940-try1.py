'''
14940. <실버1> 쉬운 최단거리
https://www.acmicpc.net/problem/14940
'''

from pprint import pprint
import sys
from collections import deque

input = sys.stdin.readline

board = []
move = [[-1,0],[1,0],[0,-1],[0,1]]
sx, sy = -1, -1

n, m = map(int, input().split())
visited = [[-1]*m for _ in range(n)]

## 이동 가능 + 방문 좌표 확인
def is_possible(x, y):
    # 이동 가능 범위이고, 0이 아니며, 방문하지 않은 좌표인가?
    if (0<=x<m) and (0<=y<n) and (board[y][x]!=0) and visited[y][x]<0:
        return True
    else:
        return False

## 보드 입력 및 시작 좌표 찾기, 0은 미리 표시해둠
for i in range(n):
    tmp_arr = list(map(int, input().split()))    

    for j in range(m):
        if tmp_arr[j]==2:
            sx, sy = j, i
        elif tmp_arr[j]==0:
            visited[i][j]=0
    
    board.append(tmp_arr)

# print(sx, sy)
# pprint(board)
# pprint(visited)

## bfs [x, y, cnt]

q = deque()
q.append([sx, sy, 0])
visited[sy][sx] = 0

while q:

    cx, cy, cnt = q.popleft()

    for dx, dy in move:
        nx, ny = dx+cx, dy+cy
        new_cnt = cnt+1
        if is_possible(nx, ny):
            visited[ny][nx]=new_cnt
            q.append([nx, ny, new_cnt])
# pprint(visited)

## 정답 출력
for arr in visited:
    print(' '.join(map(str, arr)))
