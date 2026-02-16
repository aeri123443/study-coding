'''
14502. <골드4> 연구소
https://www.acmicpc.net/problem/14502
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

# 0은 빈 칸, 1은 벽, 2는 바이러스.
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [(0,1), (1,0), (-1,0), (0,-1)]
visited = []

# 바이러스 위치, 비어있는 곳 저장
virus = []
blanks = []
for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            virus.append( (i,j) )
        elif board[i][j]==0:
            blanks.append( (i,j) )

answer = 0

def add_virus():

    q = deque()
    for i, j in virus:
        q.append( (i,j) )
        visited[i][j] = True
    
    while q:
        ci, cj = q.popleft()

        for di, dj in move:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and board[ni][nj]==0:
                visited[ni][nj] = True
                q.append( (ni, nj) )

def find_safe(si,sj):
    cnt = 1
    q = deque([ (si,sj) ])
    visited[si][sj] = True

    while q:
        ci, cj = q.popleft()

        for di, dj in move:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and board[ni][nj]==0:
                cnt += 1
                visited[ni][nj] = True
                q.append( (ni, nj) )
    return cnt

# 메인 탐색
def explore():
    global visited

    safe_area = 0
    visited = [[False]*M for _ in range(N)]

    # 병 퍼져나가기
    add_virus()

    # 안전한 영역 탐색
    for i,j in blanks:
        if board[i][j]==0 and not visited[i][j]:
            safe_area += find_safe(i,j)

    return safe_area

# 조합 + 백트래킹
combi_visited = set()
def install_wall(cnt):
    global answer

    # 벽을 3개 모두 지었을때만 진행
    if cnt==3:
        # pprint(board)
        safe_area = explore()
        answer = max(safe_area, answer)
        return

    for i, j in blanks:
        if (i, j) in combi_visited: continue

        if board[i][j]==0:
            board[i][j] = 1
            combi_visited.add( (i,j) )
            install_wall(cnt+1)
            board[i][j] = 0
            combi_visited.remove( (i,j) )

install_wall(0)

print(answer)