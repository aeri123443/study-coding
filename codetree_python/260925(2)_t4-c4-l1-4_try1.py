'''
빙하
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-glacier/description

문제 분석: 4m 46s
코드 작성: 20m 17s

총 소요 시간: 25m 3s
'''
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
MOVE = [(0,1), (1,0), (-1,0), (0,-1)]

def bfs(visited, sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    ice = []

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc =cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                visited[nr][nc] = True
                # 물이면 다음으로 진행
                if board[nr][nc] == 0:
                    q.append((nr,nc))
                # 얼음이면 반환 리스트에 담음
                else:
                    ice.append((nr,nc))

    return ice

def main():
    t = 0
    last_ice_cnt = 0

    # 가장자리 리스트
    side_pos = set()
    for r in range(N):
        side_pos.add((r, 0))
        side_pos.add((r, M-1))
    for c in range(M):
        side_pos.add((0,c))
        side_pos.add((N-1, c))

    # 1초씩 증가
    while True:

        visited = [[False]*M for _ in range(N)]
        side_ice = []
        for sr, sc in side_pos:
            # 가장자리 0을 찾고, bfs 시작, 가장자리 1 반환
            if board[sr][sc]==0 and not visited[sr][sc]:
                ice_pos = bfs(visited, sr, sc)
                side_ice.extend(ice_pos)

        # 가장자리 1 있으면 바꾸고, 없으면 종료
        if side_ice:
            for r, c in side_ice:
                board[r][c] = 0
            last_ice_cnt = len(side_ice)
        else:
            print(t, last_ice_cnt)
            break

        t += 1
main()