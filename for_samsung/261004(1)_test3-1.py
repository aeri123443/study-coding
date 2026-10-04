'''
동전 챙기기 | 모의고사 3회 - 1번
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4803/curated-cards/mock-collect-coins/description

문제 분석: 22m 14s
코드 1차 작성: 51m 11s
코드 2차 작성: 43m 50s
총 소요 시간: 1h 57m 15s
'''

# 분석 22m 14s

# =====================================
# 전역 선언부 2m 26s
# =====================================
from collections import deque

DEBUG = False
N = int(input())
board = [list(input()) for _ in range(N)]
BIN = 2**9
MOVE = [(0,1), (1,0), (-1,0), (0,-1)]
E = (-1, -1)

# =====================================
# 보조 함수
# =====================================
def remake_board(): # 8m 12s 이하 (확인 후 bfs 디버깅하다가 시간 랩함)
    sr, sc = -1, -1
    for r in range(N):
        for c in range(N):

            if board[r][c] == '#': board[r][c] = -1
            elif board[r][c] == '.': board[r][c] = 0
            elif board[r][c] == 'S': sr, sc = r, c; board[r][c] = 0
            elif board[r][c] == 'E': board[r][c] = -2
            else: board[r][c] = int(board[r][c])

    return sr, sc

def append_q(q, visited, cr, cc, prev_coin, prev_cnt, nr, nc, new_coin, last_coin):
    if visited[nr][nc][new_coin] == -1:
        visited[nr][nc][new_coin] = visited[cr][cc][prev_coin]+1
        q.append((nr, nc, new_coin, last_coin)) # cr, cc, coin, last_coin
def bfs(sr, sc): # 26m 02s + 14m 31s + tc 오류 디버깅 43m 50s
    visited = [[[-1]*BIN for _ in range(N)] for _ in range(N)]
    q = deque([(sr, sc, 0, 0)])
    visited[sr][sc][0] = 0

    while q:
        cr, cc, coin, last_coin = q.popleft()
        prev_cnt = str(bin(coin)).count('1')

        if board[cr][cc] == -2 and prev_cnt >= 3:
            return visited[cr][cc][coin] + 1

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc

            if 0<=nr<N and 0<=nc<N and board[nr][nc] != -1:
                num = board[nr][nc]
                # 다음 위치가 도착점이고 코인 3개 이상 -> 종료
                if num == -2 and prev_cnt >= 3:
                    return visited[cr][cc][coin]+1

                else:
                    # 다음 위치가 빈 공간임
                    if num == 0 or num==-2:
                        append_q(q, visited, cr, cc, coin, prev_cnt, nr, nc, coin, last_coin)
                    # 다음 위치가 코인임
                    else:
                        # 기존 코인보다 클 경우 획득
                        got_coin = 1 << (num-1)
                        if last_coin < got_coin:
                            new_coin = coin + got_coin
                            new_last = got_coin

                            # 코인 획득
                            append_q(q, visited, cr, cc, coin, prev_cnt, nr, nc, new_coin, new_last)

                            # 코인 포기
                            append_q(q, visited, cr, cc, coin, prev_cnt, nr, nc, coin, last_coin)

                        else:
                            append_q(q, visited,cr, cc, coin, prev_cnt, nr, nc, coin, last_coin)

    return -1
# =====================================
# 메인 로직
# =====================================

def main():
    sr, sc = remake_board()
    cnt = bfs(sr, sc)

    if DEBUG: print()
    print(cnt)

main()