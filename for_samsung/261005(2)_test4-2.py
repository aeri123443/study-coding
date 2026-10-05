"""
🔗 [바이러스 퇴치](https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4804/curated-cards/fight-the-virus/description)
## ⏱ 풀이 시간
- 총 소요 시간: 3h 18m 07s
	- 문제 분석: 1h 06m 41s
	- 코드 작성: 2h 11m 26s
	- tc fail
"""

"""
for K .. 

    1. 로봇 행동
        1. 목표 설정
            1) 확산 강도 최대 집, 행 최소, 열 최소
            2) ** 감염된 집이 없으면: 최초 바이러스 발생(V)
        2. 목표를 향해 한 칸 이동
            - ** 이미 그 위치임 -> 그대로!
            - 맨해튼 거리가 줄어드는 방향, 상우하좌
        3. 바이러스 수치를 점수로 누적 
            - 바이러스가 없으면 0
            - 가만히 있어도 누적
        4. 정화 작업
            - 감염된 집일 경우:
                - 이때도 누적
                - **더 이상 감염되지 않음
                - 모든 바이러스 사라짐
            - V
                - **조기 종료!
    2. "감염된 집"의 바이러스 전파
        - 빈 공간에만 전파 (R 초기 포함, 집x)
        - t턴 감염시 t+D턴부터 d=1인 곳에 전파
        - 매 턴마다 1씩 더 먼 곳으로 바이러스 확산
          (확산강도 S) - d(거리)
          [??] d 거리에서 생산되는  수치가 S-d >= 1인 칸까지 전파
        [!] **턴마다 누적 아니고 턴 이후에도 덮어쓰기!!
        - 여러 바이러스가 같은 칸에 전파시..
            - 최대 바이러스, 집 행 최소, 집 열 최소
        [?] 전파 중 로봇 정화하면? -> 관련 모든 바이러스 사라짐

    3. 최초 바이러스(V)의 신규 감염
        - v의 배수 턴마다
        - 아직 감염된 적 없는 집들 중 하나를 새로 감염
          - 거리 최소, 행 최소, 열 최소
          - 초기 확산 강도 S

    4. 바이러스 강화
        - w의 배수 턴마다
        - 모든 바이러스 수치 2씩 증가
        - 확산 강도, 빈 공간에 퍼진 바이러스 모두!

출력
- 성공 시: 누적 바이러스 수치, 정화한 집의 개수, 소요된 총 턴 수
- 실패 시: -1

케이스
- W & V 공배수 턴
- 바이러스 업데이트 잘 되는지 
- 바이러스 확산 없이 바로 도달하는 경우 (V가 큼)

설계
for K 

    # 1. 로봇 행동
        # 1. 목표 설정 next_target
            # 목표 집 반환: 확산 강도 최대 집, 행 최소, 열 최소 (**자기 위치 포함)
            # 감염된 집이 없으면: 최초 바이러스 발생(V)
            # [?] 매 턴마다 찾아도 되는지, 시간복잡도 상 W턴마다 업데이트 해야 하는지
        # 2. 목표를 향해 한 칸 이동 next_pos
            # 이미 그 위치임 -> 그대로!
            # 다른 위치임 -> 맨해튼 거리가 줄어드는 방향, 상우하좌
        # 3. 바이러스 수치를 점수로 누적 
            # - 바이러스가 없으면 0
            # - 가만히 있어도 누적
        # 4. 정화 작업 (집 또는 바이러스 시작점일 때)
            # 감염된 집 도착했을 경우
                # [!] 윗단계에서 바이러스 누적 확인
                # 정화 여부 업데이트: 더 이상 감염되지 않음
                # 관련된 모든 바이러스 사라짐 del_virus()
                                # [?] 전부 탐색해도 되는지, 미리 표시해야 하는지 확인
            # - 최초 발생지 도착 -> **조기 종료!
    # 2. "감염된 집"의 바이러스 전파
        # for 감염 집
            # t+D턴부터 d=1인 곳에 전파 (계산), 아직일 경우 pass
            # d의 좌표를 담음(계산으로, 빈 공간에만 전파 (R 초기 포함, 집x))
                # 매 턴마다 1씩 더 먼 곳으로 바이러스 확산
            # 확산
                # [!] d 거리에서 생산되는  수치가 S-d >= 1인 칸까지 전파
                # (확산강도 S) - d(거리)
                # - 여러 바이러스가 같은 칸에 전파시..
                    # - 최대 바이러스, 집 행 최소, 집 열 최소 (덮어쓰기!!)

    # 3. 최초 바이러스(V)의 신규 감염
    # v의 배수 턴마다
        # 감염될 집 반환
            # 아직 감염된 적 없는 집들 중 하나를 새로 감염
            # 거리 최소, 행 최소, 열 최소
        # 감염될 집이 없을 경우 pass
        # 초기 확산 강도 S
        # 집 감염 여부, 해당 턴 수 업데이트

    # 4. 바이러스 강화
    # w의 배수 턴마다
        # 모든 바이러스 수치 2씩 증가
            # [!] 확산 강도, 빈 공간에 퍼진 바이러스 모두!

문제 분석 1:6:42
"""
from collections import deque

DEBUG = False
INF = float('inf')
MOVE = [(-1,0), (0,1), (1,0), (0,-1)]

N, M, K = map(int, input().split())
V, D, S, W = map(int, input().split())
I, R = (), ()
houses = {}
place_board = [list(input()) for _ in range(N)]
virus_board = [[(0,-1,-1) for _ in range(M)] for _ in range(N)]

class House:
    def __init__(self, r, c):
        self.pos = (r,c)
        self.status = 0
        self.s = S
        self.last_virus = deque([(r,c)])

def input_board():  # 전역+ 여기까지 16:06
    global I, R

    for r in range(N):
        for c in range(M):
            if place_board[r][c] == 'H':
                new_house = House(r,c)
                houses[(r,c)] = new_house
            elif place_board[r][c] == "V":
                place_board[r][c] = 'I'
                I = (r, c)
            elif place_board[r][c] == "R":
                place_board[r][c] = '.'
                R = (r,c)

# 목표 집 반환: 확산 강도 최대 집, 행 최소, 열 최소 (**자기 위치 포함)
def get_next_target():
    info = (-INF, -INF, -INF)
    for (r,c), house in houses.items():
        if house.status > 0:
            info = max(info, (house.s, -r, -c))

    _, nr, nc = info
    return -nr, -nc


# 맨해튼 거리가 줄어드는 방향, 상우하좌
def move_robot(er, ec):
    global R

    info = (INF, INF, INF, INF) # 거리 최소, 방향 최소, 다음위치 정보

    cr, cc = R
    for d in range(4):
        dr, dc = MOVE[d]
        nr, nc = dr+cr, dc+cc
        if 0<=nr<N and 0<=nc<M:
            dis = abs(nr-er) + abs(nc-ec)
            info = min(info, (dis, d, nr, nc))

    _, _, nr, nc = info
    R = (nr,nc)

# t+D턴부터 d=1인 곳에 전파 (계산)
# d의 좌표를 담음(계산으로, 빈 공간에만 전파 (R 초기 포함, 집x))
# 매 턴마다 1씩 더 먼 곳으로 바이러스 확산
def get_spread_pos(house, t):
    d = t - D - house.status + 1
    if house.s - d < 1:
        return -1, []
    hr, hc = house.pos
    res = []
    for dr in range(-d, d+1):
        dc = d - abs(dr)
        for nc in {hc+dc, hc-dc}:
            nr = hr + dr
            if 0<=nr<N and 0<=nc<M and place_board[nr][nc] == '.':
                res.append((nr, nc))
    return d, res
# 감염될 집 반환
# 아직 감염된 적 없는 집들 중 하나를 새로 감염
# 거리 최소, 행 최소, 열 최소
def get_virus_house():
    ir, ic = I
    info = (INF, INF, INF, INF) # 거리, 행, 열, 집 객체
    for (r,c), house in houses.items():
        if house.status == 0:
            dis = abs(ir-r) + abs(ic-c)
            info = min(info, (dis, r, c, house))

    return info[3]

# 우선순위에 따른 바이러스 확산
# 여러 바이러스가 같은 칸에 전파시: 최대 바이러스, 집 행 최소, 집 열 최소 (덮어쓰기!!)
def update_virus(house, r, c, s):
    hr, hc = house.pos
    info = (s, -hr, -hc)

    # 해당 칸에 전파 이력이 있을 경우 업데이트
    if virus_board[r][c][1] != -1 :
        ps, pr, pc  = virus_board[r][c]
        info = max(info, (ps, -pr, -pc))

    vs, vr, vc = info
    vr, vc = -vr, -vc
    virus_board[r][c] = (vs, vr, vc)

# 관련된 모든 바이러스 제거
def del_virus(house):
    hr, hc = house.pos
    for r in range(N):
        for c in range(M):
            _,vr, vc = virus_board[r][c]
            if (hr, hc) == (vr, vc):
                virus_board[r][c] = (0,-1,-1)

def main():
    input_board()
    # # if DEBUG: print()
    virus_sum, cleand = 0, 0

    for t in range(1, K+1):
        # =====================================
        # 1. 로봇 행동
        # =====================================

        er, ec = get_next_target()
        target_v = False

        # 감염된 집이 없으면: 최초 바이러스 발생지로
        if er == INF:
            er, ec = I
            target_v = True

        # 다음 위치 반환
        # 이미 그 위치임 -> 그대로!
        # 다른 위치임 -> 맨해튼 거리가 줄어드는 방향, 상우하좌
        if (er, ec) != R:
            move_robot(er, ec)

        # 바이러스 수치를 점수로 누적
        rr, rc = R
        virus_sum += virus_board[rr][rc][0]

        ## 여기까지 22:52

        if R == (er, ec):  # 목표에 도착했을 때만 정화
            if target_v:
                print(virus_sum, cleand, t)
                return  # main 함수이므로 return
            house = houses[R]
            house.status = -1
            del_virus(house)
            cleand += 1
                                    # [?] 전부 탐색해도 되는지, 미리 표시해야 하는지 확인
        # 최초 발생지 도착 -> **조기 종료!
        elif place_board[rr][rc] == 'I' and cleand == len(houses) :
            print(virus_sum, cleand, t)
            return

        # if DEBUG: print()

        # =====================================
        # 2. "감염된 집"의 바이러스 전파
        # =====================================

        for house in houses.values():
            if house.status in (0, -1): continue
            if house.status + D > t: continue # 아직일 경우 pass

            dis, spread_pos = get_spread_pos(house, t)
            if spread_pos:
                s = house.s - dis
                for spr, spc in spread_pos:
                    update_virus(house, spr, spc, s)
            # if DEBUG: print()

        # =====================================
        # 3. 최초 바이러스(V)의 신규 감염
        # =====================================
        # v의 배수 턴마다
        if t%V == 0:
            virus_house = get_virus_house()

            if virus_house!=INF: # 감염될 집이 없을 경우 pass
                virus_house.status = t
                hr, hc = virus_house.pos
                virus_board[hr][hc] = (S, hr, hc)

            # if DEBUG: print()

        # =====================================
        # 4. 바이러스 강화
        # =====================================
        # w의 배수 턴마다
        if t%W == 0:
            for r in range(N):
                for c in range(M):
                    vs, vr, vc = virus_board[r][c]
                    if vs == 0 : continue
                    virus_board[r][c] = (vs+2, vr, vc)
                    if (r,c) in houses:
                        houses[(r,c)].s += 2
            # if DEBUG: print()

        # if DEBUG: print()
    print(-1)
main()
# for K

