'''
# 분석 20m 42s
N*N(2~20)
# 벽
. 빈공간
S
E
1~9 동전

** S → 최소 3개 동전 수집 (초과 ok) → E
** 중복 방문 허용
** 증가하는 순서대로

→ 최소 이동 횟수 / 불가능하면 -1

나올 수 있는 상황
- 특정 지점을 중복 방문해야만 동전 3개를 모을 수 있음
- 특정 지점 중복 방문해야 더 빨라지는 경우
7
.......
.....4.
.......
.......
.......
312....
.SE....

- S —> E로 가는 경우는 있지만 3개 미만으로 모임 (-1)
5
#####
#12E#
##S##
###3#
#####

- S→E, 3개 모을 수는 있지만 순서대로가 아님 (순서대로 불가, -1) → 중복방문할수 있어서 순서대로 가능
  → 순서대로 제대로 모이는지 체크
3
21E
3##
S##

구조 설계
- 브루트포스?? (동전 3개) 경우의 수 구한 후 S → a, a→b … c→ E 경우의 수 따로 구하기  → 시간 내 가능

0. S, E 찾기
0. 동전 순서 조합 정하기
  - (a, b, c) 조합
  - 정렬 후 반환

For S, 동전 조합, E
  1. 방문 거리: point to point 경로 탐색
  2.  거리 누적
3. 최소 거리 업데이트
'''

# 코드 작성 35m 51s
# 테스트 케이스 점검 4m 13s
from collections import deque
from itertools import combinations

DEBUG = False
INF = float('inf')
N = int(input())
board = [list(input()) for _ in range(N) ]
coin_pos = {}
MOVE = [(1,0), (-1,0), (0,-1), (0,1)]

# 0. S, E 찾기 및 보드 변환
start, end = (), ()
for r in range(N):
    for c in range(N):
        if board[r][c] == '#':
            board[r][c] = -1
        elif board[r][c] == '.':
            board[r][c] = 0
        elif board[r][c] == 'S':
            board[r][c] = 0
            start = (r, c)
        elif board[r][c] == 'E':
            board[r][c] = 0
            end = (r, c)
        else: # 동전
            co =  int(board[r][c])
            board[r][c] = co
            coin_pos[co] = (r,c)


# 0. 동전 순서 조합 정하기
#   - (a, b, c) 조합
#   - 정렬 후 반환
coin_order = []
for a, b, c in combinations(coin_pos, 3):
    li = sorted((a, b, c ))
    coin_order.append(li)

# if DEBUG: print()

def cal_dis(sr, sc, er, ec):
    visited = [[-1]*N for _ in range(N)]
    q = deque([(sr, sc)])
    visited[sr][sc] = 0

    while q:
        cr, cc = q.popleft()
        cnt = visited[cr][cc]

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            # 범위 내, 미방문, 장애물
            if 0<=nr<N and 0<=nc<N and board[nr][nc] != -1 and visited[nr][nc] == -1:
                if (nr,nc) == (er, ec) :
                    return cnt + 1

                q.append((nr,nc))
                visited[nr][nc] = cnt + 1
    return -1

# For S, 동전 조합, E
answer = INF
for coins in coin_order:

    order = [start] + [coin_pos[c] for c in coins] + [end]
    dis_total = 0
    flag = False
    for o in range(4):
        dis = cal_dis(*order[o], *order[o+1])
        if dis == -1:
            flag = True
            break
        dis_total += dis

    if not flag:
        answer = min(answer, dis_total)

print(answer if answer != INF else -1)


