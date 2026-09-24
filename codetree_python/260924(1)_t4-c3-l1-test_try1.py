'''
뿌요뿌요
https://www.codetree.ai/ko/trails/complete/curated-cards/test-puyo-puyo/description

문제 분석: 2m 46s
코드 작성: 7m 53s

총 소요 시간: 10m 39s
'''
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
MOVE = [(0,1), (1,0), (-1,0), (0,-1)]


def grouping(sr, sc):
    num = board[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc

            if 0<=nr<N and 0<=nc<N and board[nr][nc]==num and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))
                cnt += 1


    return cnt

def main():
    group_cnt = 0
    max_len = 0

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                size = grouping(r,c)
                max_len = max(size, max_len)
                if size >= 4: group_cnt += 1

    print(group_cnt, max_len)

main()