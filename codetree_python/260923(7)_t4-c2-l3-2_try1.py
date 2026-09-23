'''
단순한 동전 챙기기
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-collect-coins-easy/description

'''
from collections import deque

MOVE = [(0,1), (1,0), (-1,0), (0,-1)]
N = int(input())
board = [list(input()) for _ in range(N)]
sr = sc = er = ec = -1
for r in range(N):
    for c in range(N):
        ch = board[r][c]
        if ch == 'S':
            sr, sc = r, c; board[r][c] = 0
        elif ch == 'E':
            er, ec = r, c; board[r][c] = 0
        elif ch == '.':
            board[r][c] = 0
        else:
            board[r][c] = int(ch)

def bfs():
    # visited[r][c][coin_cnt][cur_coin]
    visited = [[[[False]*10 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    visited[sr][sc][0][0] = True
    q = deque([(sr, sc, 0, 0, 0)])  # r, c, dist, coin_cnt, cur_coin

    while q:
        cr, cc, d, cnt, cur = q.popleft()
        if (cr, cc) == (er, ec) and cnt == 3:
            return d                      # BFS라 처음 도착 = 최단

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            coin = board[nr][nc]
            # 1) 동전 줍기
            if coin and cnt < 3 and coin > cur and not visited[nr][nc][cnt+1][coin]:
                visited[nr][nc][cnt+1][coin] = True
                q.append((nr, nc, d+1, cnt+1, coin))
            # 2) 안 줍고 지나가기
            if not visited[nr][nc][cnt][cur]:
                visited[nr][nc][cnt][cur] = True
                q.append((nr, nc, d+1, cnt, cur))
    return -1

print(bfs())