'''
메두사와 전사들: 2024 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/medusa-and-warriors/

'''

from collections import deque

##################################################
#### 전역 변수 및 클래스
##################################################

INF = float('inf')
MOVE = [(-1, 0), (+1, 0), (0, -1), (0, +1)] # 상-하-좌-우

N, M = -1, -1
MR, MC = -1, -1 # 메두사 위치
PR, PC = -1, -1 # 공원 위치
knights = [] # 기사 위치

map_board = []
see_board = []
knights_board = []

##################################################
#### 보조 함수
##################################################
def input_data():
    global N, M, MR, MC, PR, PC, knights, map_board, see_board, knights_board

    N, M = map(int, input().split())
    MR, MC, PR, PC = map(int, input().split())

    # 기사 위치 정보 업데이트
    knights_board = [ [ set() for _ in range(N) ]  for _ in range(N) ]
    k_line = list(map(int, input().split()))
    for i in range(M):
        kr, kc = k_line[i*2], k_line[i*2+1]
        knights.append( (kr, kc) )
        knights_board[kr][kc].add(i)

    map_board = [list(map(int, input().split())) for _ in range(N)]
    see_board = [[0]*N for _ in range(N)]

### 전사 제거
def remove_knight(k):
    kr, kc = knights[k]
    knights_board[kr][kc].remove(k)
    knights[k] = (-1, -1)

### 메두사 이동 (공원 -> 메두사 역bfs, 우좌하상)
def rev_bfs():
    sr, sc, er, ec = PR, PC, MR, MC

    visited = [[-1]*N for _ in range(N)]
    visited[sr][sc] = 0
    q = deque([(sr, sc)])

    while q:
        cr, cc = q.popleft()

        for d in [3,2,1,0]: # 우좌하상
            dr, dc = MOVE[d]
            nr, nc = cr+dr, cc+dc

            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1 and map_board[nr][nc]==0:
                # 도착했을 경우 리턴
                visited[nr][nc] = visited[cr][cc] + 1
                if nr==er and nc==ec:
                    continue
                q.append((nr,nc))

    medusa_info = (INF, INF, INF, INF) # 거리, 방향
    # 4방향에 대하여 최소 경로 업데이트
    # print(visited)
    for d in range(4):
        dr, dc = MOVE[d]
        nr, nc = dr+MR, dc+MC
        if 0<=nr<N and 0<=nc<N and map_board[nr][nc]==0 and visited[nr][nc]!=-1:
            medusa_info = min(medusa_info, (visited[nr][nc], d, nr, nc))
        # print()

    if medusa_info[0]==INF:
        return -1, -1
    else:
        return medusa_info[2], medusa_info[3]

def update_medusa_look(md):
    # 범위 내 전사 정보
    knight_in_see = set()

    mdr, mdc = MOVE[md]
    idx = 1
    if mdc == 0: # 상하 방향
        r = MR + mdr
        while 0<=r<N:
            sc = max(MC - idx, 0)
            ec = min(MC + idx + 1, N)
            for c in range(sc, ec):
                see_board[r][c] = 1
                if knights_board[r][c]:
                    knight_in_see.update(knights_board[r][c])
            r += mdr
            idx += 1
    else: # 좌우방향
        c = MC + mdc
        while 0<=c<N:
            sr = max(MR - idx, 0)
            er = min(MR + idx + 1, N)
            for r in range(sr, er):
                see_board[r][c] = 1
                if knights_board[r][c]:
                    knight_in_see.update(knights_board[r][c])
            c += mdc
            idx += 1
    return knight_in_see
    print()

def update_knight_look(md, k):
    mdr, mdc = MOVE[md]
    kr, kc = knights[k]

    idx = 1
    if mdc == 0: # 상하
        r = kr + mdr
        while 0 <= r < N:
            if kc < MC:
                sc = max(kc - idx, 0)
                ec = kc + 1
            elif kc > MC:
                sc = kc
                ec = min(kc + idx + 1, N)
            else: # kc==MC
                sc = MC
                ec = MC + 1

            for c in range(sc, ec):
                if see_board[r][c] == 1:
                    see_board[r][c] = 2
            idx += 1
            r += mdr
    # print()
    else: # 좌우
        c = kc + mdc

        while 0<=c< N:
            if kr < MR:
                sr = max(kr - idx, 0)
                er = kr + 1
            elif kr > MR:
                sr = kr
                er = min(kr + idx + 1, N)
            else: # kr==MR
                sr = MR
                er = MR + 1

            for r in range(sr, er):
                if see_board[r][c] == 1:
                    see_board[r][c] = 2
            idx += 1
            c += mdc

def see_medusa():
    see_info = (INF, INF) # -돌 수, +상하좌우

    # 4방향에 대해
    for md in range(4):
        for i in range(N):
            for j in range(N):
                see_board[i][j] = 0

        knight_in_see = update_medusa_look(md)

        # 전사 시야각
        for k in knight_in_see:
           update_knight_look(md, k)
        # print()

        # 돌이 되는 전사를 탐색
        stones = 0
        for i in range(N):
            for j in range(N):
                if see_board[i][j] == 1 and knights_board[i][j]:
                    stones += len(knights_board[i][j])

        see_info = min(see_info, (-stones, md))

    return -see_info[0], see_info[1]

def find_knight_move(k, dlist):

    kr, kc = knights[k]
    standard = abs(kr-MR) + abs(kc-MC) # 원래 거리

    for d in dlist:
        dr, dc = MOVE[d]
        nr, nc = dr+kr, dc+kc
        dis = abs(nr-MR) + abs(nc-MC)
        # print()
        # 범위 내, 시야각 내, 맨헤튼 거리가 가까워지는지
        if 0<=nc<N and 0<=nr<N and see_board[nr][nc]!=1 and dis<standard:
            return nr, nc

    return -1, -1

### 전사 이동
# 반환: 이동 여부(moved), 사라짐 여부(dead)
def move_knight(k, dlist):
    nkr, nkc = find_knight_move(k, dlist)

    if nkr == -1:
        return False, False

    # 메두사가 있으면 사라짐
    if nkr == MR and nkc == MC:
        remove_knight(k)
        return True, True
    # 메두사가 있으면 이동
    else:
        kr, kc = knights[k]
        knights[k] = (nkr, nkc)
        knights_board[kr][kc].remove(k)
        knights_board[nkr][nkc].add(k)
        return True, False
##################################################
#### 메인 로직
##################################################
def main():
    global MR, MC
    answer = []

    input_data()
    # print()

    while True:
        ########################################
        ### [1] 메두사 이동
        ########################################

        nmr, nmc = rev_bfs()

        # 이동 불가할 경우 -1 종료
        if nmr == -1:
            answer.append('-1')
            break

        # 4방향 중 최단경로


        # 공원 도착시 종료
        if nmr == PR and nmc == PC:
            answer.append('0')
            break

        # 전사가 있을 경우 전사 사라짐
        if knights_board[nmr][nmc]:
            tmp_set = set(knights_board[nmr][nmc])
            for k in tmp_set:
                remove_knight(k)

        # 메두사 실제 이동
        MR, MC = nmr, nmc

        # print()

        ########################################
        ### [2] 메두사 시선
        ########################################

        # 메두사의 시선 방향
        stone_cnt, md = see_medusa()
        # 최종 시야각 업데이트
        for i in range(N):
            for j in range(N):
                see_board[i][j] = 0

        knight_in_see = update_medusa_look(md)

        # 전사 시야각
        for k in knight_in_see:
           update_knight_look(md, k)

        # print()

        ########################################
        ### [3] 전사의 이동
        ########################################

        attack_cnt = 0
        move_cnt = 0
        for k in range(M):
            kr, kc = knights[k]
            # 사망했거나 돌이 된 전사는 이동할 수 없음
            if kr == -1 or see_board[kr][kc] == 1: continue

            # 1차 이동
            moved, dead = move_knight(k, [0,1,2,3]) # 상하좌우
            if moved:
                move_cnt += 1
                if dead:
                    attack_cnt += 1
                    continue
            # print()
            # 2차 이동
            moved, dead = move_knight(k, [2,3,0,1])  # 좌우상하
            if moved:
                move_cnt += 1
                if dead:
                    attack_cnt += 1
            # print()
        answer_line = [move_cnt, stone_cnt, attack_cnt]
        answer.append(' '.join(map(str, answer_line)))

        # print()

    print('\n'.join(answer))

main()