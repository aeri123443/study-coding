'''
메두사와 전사들: 2024 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/medusa-and-warriors/

문제 분석: 12m 27s
코드 1차 작성: 2h 38m 05s
최종 디버깅: 0m 0s

총 소요 시간: 2h 50m 35s
'''
from collections import deque

########################################################
##### 전역 선언
########################################################

INF = float('inf')
N, M = -1, -1
MOVE = [(-1,0), (-1,+1), (0,+1), (+1,+1), (+1,0), (+1,-1), (0,-1), (-1,-1)] # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
SEE_MAP = { # 사방향 : 대각선 매핑
    0: [7, 0, 1], # 상
    2: [1, 2, 3], # 우
    4: [5, 4, 3], # 하
    6: [7, 6, 5] # 좌
}

knights = {} # 기사 위치 정보
m_route = [] # 메두사 기본 경로

see_board = [] # 시야각 정보맵
knights_board = [] # 기사 위치 맵

########################################################
##### 보조 함수
########################################################
### 데이터 입력
def input_data():
    global N, M, knights, see_board, knights_board

    N, M = map(int, input().split())
    sr, sc, er, ec = map(int, input().split())

    k_list = list(map(int, input().split()))
    knights_board = [[ set() for _ in range(N) ] for _ in range(N) ]
    for i in range(M):
        idx = i*2
        kr, kc = k_list[idx:idx+2]
        knights[i] = (kr, kc)
        knights_board[kr][kc].add(i)

    map_board = [list(map(int, input().split())) for _ in range(N)]
    map_board[sr][sc] = 2

    see_board = [ [0]*N for _ in range(N) ]

    return sr, sc, er, ec, map_board

### 범위 확인
def in_range(nr, nc, n):
    return 0<=nr<n and 0<=nc<n

### 마녀 -> 공원 경로를 탐색 (역 bfs)
def find_route_m_to_park(map_board, mr, mc, pr, pc):
    visited = [ [-1]*N for _ in range(N)]
    visited[pr][pc] = 0
    q = deque([(pr, pc)])

    # visited 기록
    def bfs():
        while q:
            cr, cc = q.popleft()

            for d in [2, 4, 6, 0]: # 우좌하상
                dr, dc = MOVE[d]
                nr, nc = dr+cr, dc+cc

                if in_range(nr,nc,N) and visited[nr][nc]==-1 and map_board[nr][nc] != 1:
                    visited[nr][nc] = visited[cr][cc] + 1

                    if map_board[nr][nc] == 2:
                        return
                    q.append((nr, nc))

    # 마녀의 상하좌우기준으로 다음 경로를 탐색
    bfs()
    # print()
    _route = []
    r_count = visited[mr][mc]
    cr, cc = mr, mc

    while True:
        nxt = (-1, -1)
        for d in [0, 4, 6, 2]: # 상하좌우
            dr, dc = MOVE[d]
            nr, nc = dr+cr, dc+cc

            # 다음 경로가 r보다 1 작으면 이동
            if in_range(nr, nc, N) and visited[nr][nc]+1 == r_count:
                nxt = (nr, nc)
                cr, cc = nr, nc
                r_count -= 1
                _route.append(nxt)
                break

        if nxt == (-1, -1): # 경로 없음
            return []
        if nxt == (pr, pc):
            return _route

### 특정 기사를 제거
def remove_knight(k):
    kr, kc = knights[k]

    del knights[k]
    knights_board[kr][kc].remove(k)

### 직선 그리기
# 메두사가 기사를 처음 만났을 경우, 해당 좌표를 반환
# 그러지 않을 경우, (-1 ,-1) 을 반환 -> 문제 없이 잘 그려짐
def draw_line(sr, sc, d, num):
    dr, dc = MOVE[d]
    nr, nc = sr, sc

    while in_range(nr, nc, N):
        # 시야각이 2로 채워졌을 경우, 이미 기사의 시야각이므로 더 그리지 않음
        if see_board[nr][nc] == 2:
            return -1, -1
        # 메두사 기준으로, 기사를 처음 만났을 때엔 새로 기사의 시야각을 그려야 함.
        if knights_board[nr][nc] and see_board[nr][nc]==0 and num==1:
            return nr, nc

        see_board[nr][nc] = num
        nr += dr
        nc += dc

    return -1, -1

### 기사 시야각
# k_pos: 만난 기사의 위치
# rel_num: 상대위치 -> 0: 작아지는 방향, 1: 직선, 2 커지는 방향
def knight_see(k_pos, rel_num, md, mr, mc):
    kr, kc = k_pos
    d0, d1, d2 = SEE_MAP[md]

    # 직선 그리기
    draw_line(kr, kc, d1, 2)
    # print()

    # 기사 상대 위치를 기준으로 탐색 방향 선정
    if rel_num == 0:
        dr, dc = MOVE[d0]
    elif rel_num == 2:
        dr, dc = MOVE[d2]
    else: return # 직선은 직전에 처리함

    kr += dr
    kc += dc
    while in_range(kr, kc, N):
        draw_line(kr, kc, d1, 2)

        kr += dr
        kc += dc

### 메두사 시선
def medusa_see(mr, mc):
    m_see_info = (-INF, None) # 돌 수, 시야각 좌표 정보

    for see_d in [0, 4, 6, 2]: # 상하좌우
        # 시야각 초기화
        for i in range(N):
            for j in range(N):
                see_board[i][j] = 0

        d0, d1, d2 = SEE_MAP[see_d]
        # 직선 탐색
        meet_k = draw_line(mr, mc, d1, 1)
        # 기사를 만났을 경우, 해당 좌표에서 기사의 시야각을 그림!
        if meet_k != (-1,-1):
            knight_see(meet_k, 1, see_d, mr, mc)
            see_board[meet_k[0]][meet_k[1]] = 1  # knight_see에서 덮어쓰인 값을 다시 정정함

        # print()
        # 양옆 탐색

        dr0, dc0 = MOVE[d0]
        mr0, mc0 = mr+dr0, mc+dc0
        while in_range(mr0, mc0, N):
            meet_k = draw_line(mr0, mc0, d1, 1)
            if meet_k != (-1, -1):
                knight_see(meet_k, 0, see_d, mr, mc)
                see_board[meet_k[0]][meet_k[1]] = 1  # knight_see에서 덮어쓰인 값을 다시 정정함
            # print()

            mr0 += dr0
            mc0 += dc0

        dr2, dc2 = MOVE[d2]
        mr2, mc2 = mr+dr2, mc+dc2
        while in_range(mr2, mc2, N):
            meet_k = draw_line(mr2, mc2, d1, 1)
            if meet_k != (-1, -1):
                knight_see(meet_k, 2, see_d, mr, mc)
                see_board[meet_k[0]][meet_k[1]] = 1 # knight_see에서 덮어쓰인 값을 다시 정정함
            # print()

            mr2 += dr2
            mc2 += dc2

        # 시야각을 탐색하면서, 시야 내 전사 수, 시야각 좌표 정보를 반환
        stone_cnt = 0
        sights = set()
        for i in range(N):
            for j in range(N):
                if see_board[i][j]==1:
                    sights.add((i,j))
                    if knights_board[i][j]:
                        stone_cnt += len(knights_board[i][j])

        # 시야 내 전사 수가 기존보다 커질 경우, 값 업데이트
        if m_see_info[0] < stone_cnt:
            m_see_info = (stone_cnt, sights)

        # print('m_see_info', m_see_info, see_board)
    return m_see_info

### 맨헤튼 거리 게산
def cal_dis(kr, kc, mr, mc):
    return abs(mr-kr) + abs(mc-kc)

### 기사 이동
def move_knight(k, mr, mc, d_list, sights):
    is_attacked = False
    is_moved = False
    kr, kc = knights[k]
    
    # 기준 거리
    standard = cal_dis(kr, kc, mr, mc)
    
    nkr, nkc = -1, -1
    for d in d_list:
        dr, dc = MOVE[d]
        nr, nc = dr+kr, dc+kc
        
        if in_range(nr, nc, N) and (nr, nc) not in sights and standard > cal_dis(nr, nc, mr, mc):
            nkr, nkc = nr, nc
            break
    
    if (nkr, nkc) != (-1, -1):
        is_moved = True

        knights[k] = (nkr, nkc)
        knights_board[kr][kc].remove(k)
        knights_board[nkr][nkc].add(k)

        if (nkr, nkc) == (mr, mc):
            is_attacked = True

    return is_moved, is_attacked

### see_board 디버깅용 업데이트
def debug_m_see(mr, mc, stone_cnt, sights):
    tmp_board = [ [0]*N for _ in range(N) ]

    for i, j in sights:
        tmp_board[i][j] = 1

    print('medusa: ', mr, mc)
    print('stone_cnt: ', stone_cnt)
    for i in range(N):
        print('\t'.join(map(str, tmp_board[i])))

    print('\n knights...')
    for i in range(N):
        print('\t'.join( map(str, [ x if x else -1 for x in knights_board[i] ]) ))

########################################################
##### 메인 로직
########################################################
def main():
    global m_route
    answer = []

    ######################
    ### 0단계: 데이터 입력 및 전처리
    ######################

    # 데이터 입력
    mr, mc, pr, pc, map_board = input_data()

    # 마녀 -> 공원 경로를 반환
    m_route = find_route_m_to_park(map_board, mr, mc, pr, pc)
    # print(m_route)

    # 마녀가 이동 불가할 경우, -1 반환 후 종료
    if not m_route:
        print(-1)
        return

    ######################
    ### 1단계: 메두사 이동
    ######################
    for m_nxt in m_route:
        mr, mc = m_nxt

        # 메두사가 공원에 도착하면 종료
        if (mr, mc) == (pr, pc):
            answer.append('0')
            break

        # 해당 경로에 전사가 있을 경우, 전사는 사라짐
        if knights_board[mr][mc]:
            k_set = set(knights_board[mr][mc])
            for k in k_set:
                remove_knight(k)

        # print()
        ######################
        ### 2단계: 메두사 시선
        ######################

        # 최우선순위의 시야 정보를 반환
        stone_cnt, sights = medusa_see(mr, mc)
        sights.remove((mr,mc))

        # debug_m_see(mr, mc, stone_cnt, sights)
        # print()

        ######################
        ### 3단계: 전사 이동
        ######################
        move_cnt = 0
        attack_knights = set()
        
        for k in knights:
            # 돌이 되었을 경우 pass
            kr, kc = knights[k]
            if (kr, kc) in sights: continue

            # 첫 번째 이동, 상하좌우
            is_moved, is_attacked = move_knight(k, mr, mc, [0, 4, 6, 2], sights)
            if is_moved: move_cnt += 1

            if is_attacked: attack_knights.add(k)
            else:
                # 두 번째 이동, 좌우상하
                is_moved, is_attacked = move_knight(k, mr, mc, [6, 2, 0, 4], sights)
                if is_moved: move_cnt += 1
                if is_attacked: attack_knights.add(k)
            # print()
        # debug_m_see(mr, mc, stone_cnt, sights)
        # print()

        ######################
        ### 4단계: 전사 공격
        ######################
        for k in attack_knights:
            remove_knight(k)

        answer_line = [move_cnt, stone_cnt, len(attack_knights)]
        answer.append(' '.join(map(str, answer_line)))

    print('\n'.join(answer))

main()