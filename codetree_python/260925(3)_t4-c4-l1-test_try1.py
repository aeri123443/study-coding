'''
우리는 하나
https://www.codetree.ai/ko/trails/complete/curated-cards/test-we-are-the-one/description

'''
from collections import deque
from itertools import combinations

N, K, U, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
MOVE = [(0,1), (1,0), (-1,0), (0,-1)]

def bfs(starts):
    q = deque(starts)
    visited = [[False]*N for _ in range(N)]
    for sr, sc in starts: visited[sr][sc] = True
    v_cnt = len(starts)

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if U <= abs(board[cr][cc] - board[nr][nc]) <= D:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    v_cnt += 1
    return v_cnt

def main():
    max_cnt = 0
    blocks = [(r,c) for r in range(N) for c in range(N)]
    for starts in combinations(blocks, K):
        cnt = bfs(starts)
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)

main()