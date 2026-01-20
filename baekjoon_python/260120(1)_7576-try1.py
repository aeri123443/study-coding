'''
7576. <골드5> 토마토
https://www.acmicpc.net/problem/7576
'''

from pprint import pprint
import sys
from collections import deque

input = sys.stdin.readline
cnt = 0

M, N = map(int, input().split())
visited = [] # 1:방문, 0:미방문, -1:벽
s_list = []
move = [(0,1), (1,0), (-1,0), (0,-1)]
max_num = N*M # 토마토 수
num = 0 # 카운트한 토마토 수

def is_move(x, y):
    # 이동 범위 내에 있는지, 방문하지 않은 좌표인지
    if 0<=x<M and 0<=y< N and visited[y][x]==0:
        return True
    else: 
        return False
    
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            s_list.append( (j,i) )
        elif tmp[j] == -1:
            max_num -= 1

    visited.append(tmp)

# bfs

q = deque()

for sx, sy in s_list:
    q.append([sx, sy, 0])
num = len(s_list)

while q:
    cx, cy, c_cnt = q.popleft()
    n_cnt = c_cnt+1

    for dx, dy in move:
        nx, ny = cx+dx, cy+dy
        if is_move(nx,ny):
            visited[ny][nx]=1
            q.append([nx, ny, n_cnt])
            cnt = max(cnt, n_cnt)
            num += 1

# 모든 토마토가 익었는지?
# pprint([max_num, num, cnt])
if max_num == num:
    print(cnt)
else:
    print(-1)
