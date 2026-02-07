'''
2206. <골드 3> 벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
코드 깔끔하게!!
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
move = [(0,1), (0,-1), (1,0), (-1,0)]
board = []
visited = [[[False, False] for _ in range(M)] for _ in range(N)] # [0:벽 부쉈을 때, 1:안 부쉈을 때]

# 입력
for _ in range(N):
    board.append( list(map(int, list(input().strip()))) )

# pprint(board)
# pprint(visited)

q = deque() 
q.append([0,0,1,1]) # [i, j, cnt, is_breaked(부숨0, 안부숨1)]
visited[0][0][1] = True

while q:
    ci, cj, cnt, b = q.popleft()
    # print(ci, cj, cnt, b)

    if ci==N-1 and cj==M-1:
        print(cnt)
        sys.exit()

    for di, dj in move:
        ni, nj = ci+di, cj+dj

        if not (0<=ni<N and 0<=nj<M):
            continue
        # print(ci, cj, b, board[ni][nj], visited[ni][nj][0], visited[ni][nj][1])

        # 벽이 없고 방문한 적 없으면, 바로 갈 수 있음
        if board[ni][nj]==0 and not visited[ni][nj][b]:
            # print(ni, nj, 'line 65 ok')
            visited[ni][nj][b] = True
            q.append([ni, nj, cnt+1, b])

        # 벽이 있지만 부숴본 적이 없고 visited[부쉈을때]를 방문한 적 없으면, 부수고 진행
        elif board[ni][nj]==1 and b==1 and not visited[ni][nj][0]:
            # print(ni, nj, 'line 70 ok')
            visited[ni][nj][0] = True
            q.append([ni, nj, cnt+1, 0])

# pprint(visited)
print(-1)
