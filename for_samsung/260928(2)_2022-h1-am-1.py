'''
술래잡기: 2022 상반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/hide-and-seek

문제 분석: 29m 43s
코드 1차 작성: 1h 22m 35s (42m 56s + 15m 43s +15m 44s + 8m 12s)
    - [TC3 fail] 잡히면 사라진다는 조건 누락, '자기 포함' 3칸 시야 누락(클로드 도움)
코드 2차 작성: 8m 6s

총 소요 시간 2h 0m 27s
'''

# ===================================
# 전역 및 클래스
# ===================================
DEBUG = True

N, M, H, K = map(int, input().split())
MOVE = [(-1,0), (0,+1), (+1,0), (0,-1)]

trees = set()
runner_board = [[set() for _ in range(N)] for _ in range(N)] # 도망자
dir_board = [] # 0: 안->밖. 1: 밖->안

runners = {}
boss_pos = (N//2, N//2)
boss_d = 0
boss_path = []
boss_idx = 0

class Runner:
    def __init__(self, num, r, c, d):
        self.num = num
        self.r = r
        self.c = c
        self.d = d

# ===================================
# 보조 함수
# ===================================

def input_data():

    # 도망자
    for num in range(1, M+1):
        r, c, d = map(int, input().split())
        r, c = r-1, c-1
        runner_board[r][c].add(num)
        runners[num] = Runner(num, r, c, d)

    # 나무
    for _ in range(H):
        r, c = map(lambda x: int(x)-1, input().split())
        trees.add((r,c))

def get_bos_direction():
    d0 = [ [-1]*N for _ in range(N) ]
    br, bc = boss_pos

    idx = 0
    cr, cc = br, bc
    while 0<=cr<N and 0<=cc<N:
        d = idx % 4
        dr, dc = MOVE[idx % 4]
        rep = (idx // 2) + 1
        for _ in range(rep):
            d0[cr][cc] = d
            boss_path.append((cr,cc))
            cr += dr
            cc += dc
            if not (0 <= cr < N and 0 <= cc < N): break
        idx += 1

    d0[0][0] = 2
    dir_board.append(d0)

    boss_path.pop() # (0,0) 중앙 중복 방지
    cr, cc = 0, 0
    d1 = [[-1]*N for _ in range(N)]
    d1[0][0] = 2

    tmp_dirs = [2, 1, 0, 3]
    tmp_d = 0
    while 0<=cr<N and 0<=cc<N:
        d = tmp_dirs[tmp_d]
        dr, dc = MOVE[d]
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<N and d1[nr][nc] == -1:
            d1[cr][cc] = d
            boss_path.append((cr, cc))
            cr, cc = nr, nc
        else:
            tmp_d = (tmp_d+1)%4
            d = tmp_dirs[tmp_d]
            dr, dc = MOVE[d]
            nr, nc = cr + dr, cc + dc
            if 0<=nr<N and 0<=nc<N and d1[nr][nc] == -1:
                d1[cr][cc] = d
                boss_path.append((cr, cc))
                cr, cc = nr, nc
            else:
                break

    d1[br][bc] = 0
    dir_board.append(d1)


# 도망자의 다음 좌표가 이동 가능한지 확인 후 이동
def move_runner(runner):
    num, cr, cc, d = runner.num, runner.r, runner.c, runner.d
    dr, dc = MOVE[d]
    nr, nc = cr+dr, cc+dc

    # 격자 내 여부 반환
    if 0<=nr<N and 0<=nc<N:
        if (nr, nc) != boss_pos:
            runner_board[cr][cc].remove(num)
            runner_board[nr][nc].add(num)
            runner.r, runner.c = nr, nc
        return True
    else:
        return False

def move_boss():
    global boss_idx, boss_pos

    # br, bc = boss_pos
    boss_idx = (boss_idx+1) % len(boss_path)
    nr, nc = boss_path[boss_idx]
    boss_pos = (nr, nc)

def get_look_d():
    br, bc = boss_pos
    nr, nc = boss_path[(boss_idx + 1)%len(boss_path)]
    dr, dc = (nr-br), (nc-bc)

    return MOVE.index((dr,dc))

def boss_find_runner(d):
    dr, dc = MOVE[d]
    br, bc = boss_pos
    found = set()

    for i in range(3):
        nr, nc = br + dr * i, bc + dc * i
        if not (0 <= nr < N and 0 <= nc < N): break
        if (nr, nc) not in trees and runner_board[nr][nc]:
            found.update(runner_board[nr][nc])

    return found

# ===================================
# 메인 로직
# ===================================
def main():
    input_data()
    get_bos_direction()
    # if DEBUG: print()
    # 여기까지 초기 작성시간 42m 56s

    answer = 0

    for k in range(1, K+1):
        # 1. 도망자 m명 이동 (초기 작성시간 15m 43s)
        br, bc = boss_pos
        for runner in runners.values():
            # 거리 확인
            rr, rc = runner.r, runner.c
            dis = abs(rr-br) + abs(rc-bc)
            if dis > 3: continue


            # 도망자의 다음 좌표가 이동 가능한지 확인 후 이동
            is_range = move_runner(runner)
            if not is_range:
                runner.d = (runner.d + 2) % 4
                move_runner(runner)

        # if DEBUG: print()

        # 2. 술래 이동 (초기 작성시간 15m 44s)
          # 해당 단계 작성 중, 잠깐 재설계해보고, 기존 dir_board를 버리기로 결정. 술래가 바라보는 방향은 계산으로 알아낼 수 있다고 판단, 이에 both_path를 추가.
        move_boss()
        # if DEBUG: print()

        # 3. 술래잡기 (초기 작성시간 8m 12s)
        bd = get_look_d()
        found = boss_find_runner(bd)
        answer += (k * len(found))

        for num in found:
            del_runner = runners[num]
            rr, rc = del_runner.r, del_runner.c
            runner_board[rr][rc].remove(num)
            del runners[num]


    # if DEBUG: print()
    print(answer)
main()