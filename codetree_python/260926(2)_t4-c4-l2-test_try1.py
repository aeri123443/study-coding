'''
상한 귤
https://www.codetree.ai/ko/trails/complete/curated-cards/test-oranges-have-gone-bad/description
'''
from collections import deque

MOVE = [(0,1), (1,0), (-1,0), (0,-1)]
N,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[-2]*N for _ in range(N)]
q = deque([])

# 상한 귤 찾기
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            visited[r][c] = 0
            q.append((r,c))
        elif board[r][c] == 0:
            visited[r][c] = -1


while q:
    cr, cc = q.popleft()
    cnt = visited[cr][cc]

    for dr, dc in MOVE:
        nr,nc = cr+dr, cc+dc

        if 0<=nr<N and 0<=nc<N and visited[nr][nc] < 0 and board[nr][nc] == 1:
            visited[nr][nc] = cnt+1
            q.append((nr, nc))


print('\n'.join([' '.join(map(str, line)) for line in visited]))

