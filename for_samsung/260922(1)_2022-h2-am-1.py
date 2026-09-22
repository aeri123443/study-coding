'''
싸움땅: 2022 하반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/battle-ground/description

문제 분석: 21m 20s
코드 작성 중 문제 재분석: 39m 44s
  - 전역/클래스와 input_data 작성 중, '전투 이후 보드 내에서 두 플레이어가 같은 위치에 있을 가능성' 고민
  - '만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90°씩 회전하여 빈 칸이 보이는 순간 이동합니다' 라는 문구에서, 4방향 모두 이동이 불가할 경우에 대한 서술이 없었기 때문
    4방향 중 어딘가에 무조건 이동 가능함을 보장한다는 문구가 없었기에, 상태 겹침의 함정이 있을 수도 있다고 생각
  - 예제(6라운드)를 손으로 그리며 해당 케이스가 있을지 체크 -> 해당 케이스가 없었으므로 예제를 통한 문제 이하 불가
  - 우선 안전하게 상태 겹침을 고려하여 각 격자를 정수(플레이어 번호)가 아닌 리스트로 관리하자고 판단
    -> 1차 작성 중, '패자는 총을 모두 내려놓는다'는 서술도 없고, 이 정도 애매한 서술이면 분명 조건에 명시했을 것이라고 판단, 우선 플레이어의 위치가 보드 내에서 겹치지 않는다는 가정으로 전략 변
코드 1차 작성: 58m 59s

TC fail 없이 통과.

총 소요 시간: 2h 0m 4s
'''

import heapq

# ===========================================
# 전역 및 클래스
# ===========================================
DEBUG = False
N, M, K = -1, -1, -1
MOVE = [(-1,0), (0,+1), (+1,0), (0,-1)]

players = []
g_board = []
p_board = []

class Player:
    def __init__(self, num, r, c, d, s):
        self.num = num
        self.r = r
        self.c = c
        self.d = d
        self.s = s
        self.gun = 0
        self.point = 0




# ===========================================
# 보조 함수
# ===========================================

def input_data():
    global N, M, K, players, g_board, p_board

    N, M, K = map(int, input().split())
    players = [None] * (M+1)

    g_board = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            g_board[r][c] = [-g_board[r][c]] if g_board[r][c]>0 else []

    p_board = [[0]*N for _ in range(N)]
    for num in range(1, M+1):
        r, c, d, s = map(int, input().split())
        r -= 1
        c -= 1

        p_board[r][c] = num
        new_player = Player(num, r, c, d, s)
        players[num] = new_player


# 플레이어 일반 이동 (디음 위치 반환)
def get_player_next_pos(pl):
    cr, cc = pl.r, pl.c
    dr, dc = MOVE[pl.d]
    nr, nc = dr + cr, dc + cc

    if 0<=nr<N and 0<=nc<N:
        return nr, nc

    # 격자에 막힐 경우, 반대 방향으로
    pl.d = (pl.d+2)%4
    dr, dc = MOVE[pl.d]
    nr, nc = dr + cr, dc + cc

    return nr, nc

def replace_gun(pl, r,c):
    if not g_board[r][c]: return
    hq = g_board[r][c]
    max_gun_here = -hq[0]

    if pl.gun == 0:
        heapq.heappop(hq)
        pl.gun = max_gun_here
        return

    if max_gun_here > pl.gun:
        heapq.heappop(hq)
        heapq.heappush(hq, -pl.gun)
        pl.gun = max_gun_here

def move_player(pl, nr, nc):
    cr, cc = pl.r, pl.c
    num = pl.num

    if p_board[cr][cc] == num:
        p_board[cr][cc] = 0
    p_board[nr][nc] = num
    pl.r, pl.c = nr, nc

def fight(a, b):
    # 공격력 합 최대, 초기 공격력 최대
    a_info = (a.s + a.gun, a.s, a)
    b_info = (b.s + b.gun, b.s, b)

    win, lose = max(a_info, b_info), min(a_info, b_info)
    return win[2], lose[2], abs(win[0]-lose[0])

def get_loser_next_pos(loser):
    cr, cc, cd = loser.r, loser.c, loser.d

    for x in range(4):
        nd = (cd + x) % 4
        dr, dc = MOVE[nd]
        nr, nc = dr+cr, dc+cc
        if 0<=nr<N and 0<=nc<N and p_board[nr][nc] == 0:
            loser.d = nd
            return nr, nc

    return cr, cc
# ===========================================
# 메인 로직
# ===========================================
def main():
    input_data()
    # if DEBUG: print()

    for k in range(K):
        # 플레이어 순차 진행
        for num in range(1, M+1):
            pl = players[num]

            # 다음 이동 방향
            nr, nc = get_player_next_pos(pl)

            # 이동 방향에 플레이어가 없을 경우\
            if p_board[nr][nc] == 0:
                # 총 있으면 총 교체 / 내려두기
                if g_board[nr][nc]:
                    replace_gun(pl, nr, nc)
                move_player(pl, nr, nc)
            # 전투
            else:
                # 일단 현재위치 지우고 시작
                if p_board[pl.r][pl.c] == pl.num: p_board[pl.r][pl.c] = 0
                pl.r, pl.c = nr, nc

                other = players[p_board[nr][nc]]
                winner, loser, score = fight(pl, other)

                # 승자: 포인트 획득
                winner.point += score

                # 패자: 총 내려두고, 이동, 이동가능할경우 이동, 총 있으면 획득/교체
                if loser.gun > 0 :
                    heapq.heappush(g_board[nr][nc], -loser.gun)
                    loser.gun = 0

                lo_nr, lo_nc = get_loser_next_pos(loser)
                move_player(loser, lo_nr, lo_nc)
                if g_board[lo_nr][lo_nc]:
                    replace_gun(loser, lo_nr, lo_nc)

                # 승자: 총 획득/교체
                move_player(winner, nr, nc)
                if g_board[nr][nc]:
                    replace_gun(winner, nr, nc)
            # if DEBUG: print()

        # if DEBUG: print()

    # 정답 출력
    answer = [players[num].point for num in range(1, M+1)]
    print(' '.join(map(str, answer)))

main()