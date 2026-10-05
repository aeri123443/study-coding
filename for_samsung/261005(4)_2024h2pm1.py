# 삼성 기출 - 메두사와 전사들
# 문제 분석 1h 1m 19s
# 총 소요시간 3h 4m 53s
# non-fail pass

"""
0-inx
N*N
    0 도로
    1 도로 아님
전사 M명 {}
메두사 집 (,)
공원 (,)
전사 위치 보드 set()
메두사 위치 인덱스 mi
메두사 path

출력:
 - 매 턴: 모든 전사가 이동한 거리의 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수
 - 도착한 턴에는 0
 - 이동 불가시 -1
매두사: 집 -> 공원, 최단 경로, only 도로,

전사: (r,c) -> aㅔ두사, 최단 경로, 도로/비도로 구분 없음 **

class 전사
    - 위치
    - 돌 된 턴 수

def 한 사람의 시야각 만들기(시야각 번호):
    - 시야각 매핑 만들고 그거 기준으로 drow line


def 전체 시야각 만들기 :
    1) 메두사 시야각 만들기
        - 내부에 있는 전사들 있으면 반환 (돌 후보)
    2) 내부에 있는 전사들의 시야각 빼기 (한사람 시야각)

        - 생존 병사 여부 확인
        - 그 내부에 다른 전사 있으면 얘는 생존
    return 돌 된 전사, 시야각 수

0. 공원 -> 집 path 뽑기, pop으로 경로 관리
1. 메두사의 이동 (한 칸)
    - 집 -> 공원, 최단 경로(상하좌우 순서), only 도로 한 칸
    - 이동한 곳에 전사 있음 -> 전사 사망
    - 공원 도달 경로가 없을 경우 -1 출력 후 종료

2. 메두사의 시선
    1) 시야 방향 찾기
        - 시야 방향: 1) 전사 많이 볼 수 있음 2) 상하좌우
    2) 최종 시야각 만들기
    - 메두사 시야각 - 전사들 시야각
        전사 시야각은 메두사&전사 위치에 따라 상대적임
    - 메두사가 본 전사: 돌. 다음 턴에서 움직일 수 있음
        - 한 칸에 두명 이상이면 모두 돌

3. 전사 이동
    - 최대 두 칸, 메두사 방향
    - 전사간 좌표 중복 가능
    - 돌이면 이동 불가
    (1) 이동 1
        - 1) 거리 줄임 2) 상하좌우
        - 격자 밖 & 메두사 시야각 쪽으론 이동 불가
    (2) 이동 2
        - 1) 거리 줄임 2) 좌우상하
        - 격자 밖 & 메두사 시야각 쪽으론 이동 불가
4. 전사 공격
    - 전사가 메두사 칸 도달하면 -> 사망
    -
"""
from collections import deque

# 문제 분석 1h 1m 19s
class Knight:
    def __init__(self, r, c):
        self.pos = (r,c)
        self.stone = -1

DEBUG = False
INF = float('inf')
MOVE = [(-1,0), (1,0), (0,-1), (0,1)]
N, M = map(int, input().split())
SR, SC, ER, EC = map(int, input().split())

place = []
m_path = []
mi = 0

knights = {}
knights_board = [[set() for _ in range(N)] for _ in range(N)]

# 시야 방향에 따른 변화값 매핑
see_mapping = {
    # d: [직선, 감소 방향, 증가 방향]
    0: [(-1,0), (-1, -1), (-1, 1)],
    1: [(1,0), (1, -1), (1, 1)],
    2: [(0,-1), (-1,-1), (1,-1)],
    3: [(0,1), (-1,1), (1,1)]
}

# 전사 정보 업데이트
def input_knight_data():
    line = list(map(int, input().split()))
    for m in range(M):
        idx = m*2
        r, c = line[idx], line[idx+1]
        new_knight = Knight(r,c)
        knights[m+1] = new_knight
        knights_board[r][c].add(m+1)

# 공원 -> 집 path 뽑기
def get_medusa_path():
    global m_path
    def bfs():
        q = deque([(ER, EC)])
        visited = [[-1]*N for _ in range(N)]
        visited[ER][EC] = 0

        while q:
            cr, cc = q.popleft()

            for dr, dc in MOVE:
                nr, nc = dr+cr, dc+cc
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == -1 and place[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] + 1

                    if (nr,nc) == (SR,SC): return True, visited
                    q.append((nr,nc))

        return False, None
    def get_path(visited):
        m_path.append((SR,SC))
        cr, cc = SR, SC
        cnt = visited[SR][SC]

        while cnt > 0:
            for dr, dc in MOVE:
                nr, nc = dr+cr, dc+cc
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == cnt - 1:
                    cr, cc, cnt = nr, nc, cnt-1
                    m_path.append((nr,nc))
                    break

        # 한번 더 posh

    success, v = bfs()
    if success:
        get_path(v)


# 시작좌표, 변화좌표, 채워질 값
# 만나는 병사 리턴
def draw_line(see_map, ssr, ssc, sr, sc, see_d, val):
    met = set()
    cr, cc = sr, sc
    dr, dc = see_mapping[see_d][0]
    while 0<=cr<N and 0<=cc<N:
        if (cr,cc) != (ssr, ssc):
            see_map[cr][cc] = val
            if knights_board[cr][cc]:
                met.update(knights_board[cr][cc])

        cr += dr
        cc += dc

    return met

# 한 방향,한 사람에 대한 시야각 업데이트
# 시야 방향, 직선/좌/우 인덱스
def make_see_one(see_map, sr,sc, see_d, d_type, val):
    met = set()
    cr, cc = sr, sc
    dr, dc = see_mapping[see_d][d_type]
    if d_type != 0:
        cr += dr
        cc += dc
    while 0<=cr<N and 0<=cc<N:
        line_met = draw_line(see_map, sr, sc, cr, cc, see_d, val)
        if line_met: met.update(line_met)

        cr += dr
        cc += dc

    return met
# 한 방향에 대한 시야각 제작
def make_see_all(see_d):
    see_map = [[0]*N for _ in range(N)]

    # 1) 메두사 시야각 만들기
    mr, mc = m_path[mi]
    medusa_met = set()
    for d_type in range(3):
        medusa_met.update(make_see_one(see_map, mr, mc, see_d, d_type, -1))

    # 2) 내부에 있는 전사들의 시야각 빼기 (한사람 시야각)
    alive = set()
    for k_num in medusa_met:
        if k_num in alive: continue
        kr, kc = knights[k_num].pos

        # 메두사 - 기사 상대위치
        mdr,mdc = see_mapping[see_d][0]
        if kr < mr: rr = -1
        elif kr > mr: rr = 1
        else: rr = 0

        if kc < mc: rc = -1
        elif kc > mc: rc = 1
        else: rc = 0

        rr, rc = rr-mdr, rc-mdc

        # 공통
        alive.update(make_see_one(see_map, kr, kc, see_d, 0, -2))

        # 커지는 방향
        if rr + rc > 0:
            alive.update(make_see_one(see_map, kr, kc, see_d, 2, -2))
        # 작아지는 방향
        elif rr + rc < 0:
            alive.update(make_see_one(see_map, kr, kc, see_d, 1, -2))

    return medusa_met - alive, see_map

# 시야 방향 찾기
# 시야 방향: 1) 전사 많이 볼 수 있음 2) 상하좌우
def get_see_d():
    info = (-INF, -INF) # 전사 최대, 방향 최소
    for d in range(4):
        stones, _ = make_see_all(d)
        info = max(info, (len(stones), -d))

    return -info[1]

def get_knight_next_pos(see_map, knight, d_list):
    cr, cc = knight.pos
    mr, mc = m_path[mi]
    dis = abs(mr-cr) + abs(mc-cc)

    for d in d_list:
        dr, dc = MOVE[d]
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<N and see_map[nr][nc] != -1:
            nxt_dis = abs(mr-nr) + abs(mc-nc)
            if nxt_dis < dis:
                return nr, nc

    return -1, -1

def move_knight(num, nr, nc):
    knight = knights[num]
    cr, cc = knight.pos

    knights_board[cr][cc].remove(num)
    knights_board[nr][nc].add(num)
    knight.pos = (nr, nc)

def main():
    global place, mi
    # =============================
    # 0. 입력 및 전처리 31m 09s
    # =============================
    input_knight_data()
    place = [list(map(int, input().split())) for _ in range(N)]
    get_medusa_path()

    # 공원 도달 경로가 없을 경우 -1 출력 후 종료
    if not m_path:
        print(-1)
        return

    # if DEBUG: print()

    answer = []
    while True:
        # 모든 전사가 이동한 거리의 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수
        move_cnt, stone_cnt, attack_cnt = 0,0,0
        # =============================
        # 1. 메두사의 이동 (한 칸)
        # =============================
        mi += 1

        mr, mc = m_path[mi]
        # 도착 시 종료
        if (mr,mc) == (ER,EC):
            if answer: print('\n'.join(answer)) #if문 누락으로 tc fail - 수정 3m 07s
            print(0)
            return

        # 이동한 곳에 전사 있음 -> 전사 사망
        if knights_board[mr][mc]:
            for k_num in knights_board[mr][mc]:
                del knights[k_num]
            knights_board[mr][mc] = set()

        # if DEBUG: print()

        # =============================
        # 2. 메두사의 시선 1h 8m 31s
        # =============================
        see_d = get_see_d()
        stones, see_map = make_see_all(see_d)
        stone_cnt = len(stones)

        # if DEBUG: print()

        # =============================
        # 3. 전사 이동 16m 41s
        # =============================
        attacks = set()
        for num, knight in knights.items():
            # 돌이면 이동 불가
            if num in stones: continue

            nr, nc = get_knight_next_pos(see_map, knight, [0,1,2,3])
            if (nr, nc) == (mr, mc):
                move_cnt += 1
                attacks.add(num)
            elif nr != -1:
                move_knight(num, nr, nc)
                move_cnt += 1
                nr, nc = get_knight_next_pos(see_map, knight, [2, 3, 0, 1])
                if (nr, nc) == (mr, mc):
                    move_cnt += 1
                    attacks.add(num)
                elif nr != -1:
                    move_knight(num, nr, nc)
                    move_cnt += 1

        # =============================
        # 4. 전사 공격 3m 8s
        # =============================
        attack_cnt += len(attacks)
        for num in attacks:
            knight = knights[num]
            kr, kc = knight.pos
            knights_board[kr][kc].remove(num)
            del knights[num]

        answer.append(f"{move_cnt} {stone_cnt} {attack_cnt}")

    # 예제 tc 확인 및 디버깅: 3m 08s

main()