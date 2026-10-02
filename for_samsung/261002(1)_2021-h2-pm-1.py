'''
팩맨: 2021 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pacman/description

문제 분석: 50m 21s
1차 코드 작성: 58m 18s
  - [TC6 fail] <클로드 도움으로 오류 확인> 8방향 모두 막힌 몬스터가 사라짐, 팩맨이 갔던 칸을 다시 못 가게 막음
1차 디버깅: 4m 38s

총 소요 시간: 1h 53m 17s
'''
from itertools import product
from collections import defaultdict

# ==========================================
# 전역 선언
# ==========================================
DEBUG = False
INF = float('inf')
N = 4
M, T = map(int, input().split())
pr, pc = map(lambda x: int(x)-1, input().split())

MOVE = [(-1,0), (-1,-1), (0,-1), (1,-1), (+1,0), (1,1), (0,1), (-1,1)]
MOVE_PAC = list(product([0, 2, 4, 6], repeat=3))

dead_board = [[0]*N for _ in range(N)]
# ==========================================
# 보조 함수
# ==========================================

def init_monster():
    board = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        r, c, d = map(lambda x: int(x)-1, input().split())
        board[r][c][d] += 1

    return board

def get_next_monster_pos(r, c, d, t):
    for di in range(8):
        nd = (di+d)%8
        dr, dc = MOVE[nd]
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N and t > dead_board[nr][nc] and (pr, pc) != (nr, nc):
            return nr, nc, nd

    return r, c, d

def get_next_pacman_pos(moved_board):
    max_info = (-INF, -INF) # cnt, i

    for i in range(len(MOVE_PAC)):
        cr, cc = pr, pc
        cnt = 0

        flag = False
        visited = set()
        for d in MOVE_PAC[i]:
            dr, dc = MOVE[d]
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<N:
                if (nr, nc) not in visited and moved_board[nr][nc]:
                    for v in moved_board[nr][nc].values():
                        cnt += v
                visited.add((nr,nc))
                cr, cc = nr, nc

            else:
                flag = True
                break
        if flag: continue

        max_info = max(max_info, (cnt, -i))

    out_cnt, nd_list = max_info[0], MOVE_PAC[-max_info[1]]

    next_pos = []
    cr, cc = pr, pc
    for nd in nd_list:
        dr, dc = MOVE[nd]
        cr += dr
        cc += dc
        next_pos.append((cr, cc))

    return out_cnt, next_pos


# ==========================================
# 메인 로직
# ==========================================
def main():
    global pr, pc

    # ==============================
    # 0. 초기 몬스터 입력 (전역 값 작성까지 11m 43s)
    # ==============================
    mon_board = init_monster()
    monster_cnt = M
    # if DEBUG: print()

    for t in range(1, T+1):
        # ==============================
        # 1. 몬스터 복제 시도 (1m 38s)
        # ==============================
        egg_cnt = monster_cnt

        # ==============================
        # 2. 몬스터 이동 (18m 17s)
        # ==============================
        moved_board = [[defaultdict(int) for _ in range(N)] for _ in range(N)]

        for r in range(N):
            for c in range(N):
                for d, cnt in mon_board[r][c].items():
                    # 다음 위치 반환
                    nr, nc, nd = get_next_monster_pos(r, c, d, t)
                    # 이동할 수 있을 경우, 다음위치로
                    moved_board[nr][nc][nd] += cnt
        if DEBUG: print()

        # ==============================
        # 3. 팩맨 이동 (21m 10s)
        # ==============================
        out_cnt, pac_next_path = get_next_pacman_pos(moved_board)
        monster_cnt -= out_cnt
        for r, c in pac_next_path:
            if moved_board[r][c]:
                moved_board[r][c] = defaultdict(int)
                dead_board[r][c] = t+2
        pr, pc = pac_next_path[-1]

        if DEBUG: print()


        # ==============================
        # 5. 몬스터 복제 (4m 33s)
        # ==============================
        monster_cnt += egg_cnt
        for r in range(N):
            for c in range(N):
                if mon_board[r][c]:
                    for d, v in mon_board[r][c].items():
                        moved_board[r][c][d] += v

        if DEBUG: print()

        mon_board = moved_board

    # 두번째 공개 TC에서 에러 수정 (4m 38s)
    print(monster_cnt)

main()