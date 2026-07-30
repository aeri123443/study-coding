'''
메두사와 전사들: 2024 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/medusa-and-warriors/

'''

from collections import deque

##################################################
#### 전역 변수 및 클래스
##################################################
INF = float('inf')
MOVE = [(-1,0), (+1,0), (0,-1), (0,+1)] # 상하좌우

N, M = -1, -1
map_board = [] # 도로 정보
see_board = [] # 시야각 정보
knights_board = [] # 기사 위치 정보, 둘 이상이 올 수 있으므로 내부는 set으로 관리
# visited = []
knights ={} # 전사 dict
medusa = None # 메두사 객체

class Person:
    def __init__(self, uid, r, c):
        self.uid = uid # 메두사: -1
        self.r = r
        self.c = c

##################################################
#### 보조 함수
##################################################
### 기초 정보 입력
# 역bfs를 위해 공원 정보 반환
def input_data():
    global N, M, map_board, see_board, knights_board, knights, medusa

    N, M = map(int, input().split())
    sr, sc, er, ec = map(int, input().split())
    line = list(map(int, input().split()))

    # 기사
    knights_board = [ [set() for _ in range(N)] for _ in range(N)]
    for i in range(0, M*2, 2):
        uid = i//2
        kr, kc = line[i: i+2]
        knights[uid] = Person(uid, kr, kc)
        knights_board[kr][kc].add(uid)


    # 메두사
    medusa = Person(-1, sr, sc)

    # 보드 정보
    map_board = [list(map(int, input().split())) for _ in range(N)]
    map_board[er][ec] = 2 # 공원
    see_board = [[0]*N for _ in range(N)]

    return er, ec

# 역방향 최단거리 탐색 (역 bfs)
# dir_infos : 방향 정보(순서)
def rev_bfs(uid, sr, sc, er, ec, dir_infos):
    visited = [[False]*N for _ in range(N)]
    visited[sr][sc] = True
    q = deque([(sr, sc)])

    while q:
        cr, cc = q.popleft()

        for dk in dir_infos:
            dr, dc = MOVE[dk]
            nr, nc = cr+dr, cc+dc

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                # 메두사일 경우 도로가 아니면 이동 불가
                if uid==-1 and map_board[nr][nc] == 1:
                    continue
                # 기사일 경우 메두사의 시야가 있으면 이동 불가
                if uid!=-1 and see_board[nr][nc] == 1:
                    continue

                # 다음 좌표가 목적지면 직전 좌표 반환
                if nr==er and nc==ec:
                    return cr, cc

                visited[nr][nc] = True
                q.append((nr,nc))

    # 이동 불가시 -1, -1
    return -1, -1

# 대각선 상하 방향의 시야
# 위치 정보(set)를 반환
def look_diag_ud(sr, sc, tdr, tdc):
    pos_set = set()

    idx = 1
    nc = sc + tdc
    while 0<=nc<N:
        nr = sr + (tdr*idx)

        while 0<=nr<N:
            pos_set.add((nr,nc))
            nr += tdr

        nc += tdc
        idx += 1
    return pos_set

# 대각선 좌우 방향의 시야
# 위치 정보(set)를 반환
def look_diag_lr(sr, sc, tdr, tdc):
    pos_set = set()

    idx = 1
    nr = sr + tdr
    while 0<=nr<N:
        nc = sc + (tdc*idx)

        while 0<=nc<N:
            pos_set.add((nr,nc))
            nc += tdc

        nr += tdr
        idx += 1

    return pos_set

# 직선 방향의 시야
# 위치 정보(set)를 반환
def look_straight(sr, sc, dr, dc):
    pos_set = set()

    nr, nc = sr+dr, sc+dc
    while 0<=nr<N and 0<=nc<N:
        pos_set.add((nr,nc))
        nr += dr
        nc += dc

    return pos_set

# 메두사의 시선: 시선 방향과 돌이 되는 기사 정보를 반환
def medusa_see():
    global see_board

    # 돌이 된 기사 수, 방향, 돌이 된 기사 정보(set)
    medusa_look_info = (INF, INF, None)

    # 시야각 정보도 반환해야 함
    see_board_candidate = [[0]*N for _ in range(N)]

    # 메두사의 시야
    for md in range(4):
        mdr, mdc = MOVE[md]

        # 시야각 보드 리셋
        for i in range(N):
            for j in range(N):
                see_board[i][j] = 0

        pos_set = set()
        if mdc == 0:
            pos_set.update(look_diag_ud(medusa.r, medusa.c, mdr, -1))
            pos_set.update(look_diag_ud(medusa.r, medusa.c, mdr, 1))
        else:
            pos_set.update(look_diag_lr(medusa.r, medusa.c, -1, mdc))
            pos_set.update(look_diag_lr(medusa.r, medusa.c, 1, mdc))

        # 직선 방향
        pos_set.update(look_straight(medusa.r, medusa.c, mdr, mdc))

        # 시야를 탐색할 기사 정보
        looked_knight = set()
        for r, c in pos_set:

            if knights_board[r][c]:
                looked_knight.update(knights_board[r][c])
            see_board[r][c] = 1

        # 메두사의 시야에 들어올 가능성이 있는 기사 목록 중, 기사들의 시야각을 탐색
        # 가려진 기사 목록 업데이트
        hidden_knights = set()
        for lk in looked_knight:
            knight = knights[lk]
            kr, kc = knight.r, knight.c

            knight_pos = look_straight(kr, kc, mdr, mdc)  # 직선방향 기본
            # 메두사가 상하 방향으로 볼 경우
            if mdc == 0:
                tdr = mdr
                if kc > medusa.c:
                    tdc = 1
                    knight_pos.update(look_diag_ud(kr, kc, tdr, tdc))
                elif kc < medusa.c:
                    tdc = -1
                    knight_pos.update(look_diag_ud(kr, kc, tdr, tdc))
            # 메두사가 좌우 방향으로 볼 경우
            else:
                tdc = mdc
                if kr > medusa.r:
                    tdr = 1
                    knight_pos = look_diag_lr(kr, kc, tdr, tdc)
                elif kr < medusa.r:
                    tdr = -1
                    knight_pos = look_diag_lr(kr, kc, tdr, tdc)

            for r, c in knight_pos:
                # 메두사의 시야각일 경우, 2로 업데이트
                if see_board[r][c] == 1:
                    # 해당 위치에 다른 기사가 있을 경우, hidden_knight 업데이트
                    if knights_board[r][c]:
                        hidden_knights.update(knights_board[r][c])
                    see_board[r][c] = 2

        # 돌이 된 기사
        stone_knight = looked_knight - hidden_knights
        tmp_medusa_look_info = ( -len(stone_knight), md, stone_knight )
        if medusa_look_info > tmp_medusa_look_info:
            medusa_look_info = tmp_medusa_look_info
            for i in range(N):
                for j in range(N):
                    see_board_candidate[i][j] = see_board[i][j]

    # 시선 방향, 돌 수, 돌 기사 정보
    see_board = see_board_candidate
    return medusa_look_info[1], -medusa_look_info[0], medusa_look_info[2]
##################################################
#### 메인 로직
##################################################
def main():
    answer = []

    ### 0단계: 기초 정보 입력
    er, ec = input_data()
    # print()

    # 메두사가 도착할 때까지 턴 진행
    while medusa.r != er or medusa.c != ec:

        #################################################
        ### 1단계: 메두사 이동
        #################################################

        # 메두사 위치 -> 공원 최단거리
        # 방향 우선순위: 우좌하상
        nr, nc = rev_bfs(-1, er, ec, medusa.r, medusa.c,[3,2,1,0])
        # 이동 불가할 경우 -1을 출력하고 종료
        if nr == -1:
            answer.append('-1')
            break
        # 목적지에 도착했을 경우 0을 출력하고 종료
        elif nr==er and nc==ec:
            answer.append('0')
            break
        # 이동 방향에 전사가 있으면 해당 전사는 사라짐
        elif knights_board[nr][nc]:
            k_set = set(knights_board[nr][nc])
            for k in k_set:
                del knights[k]
                knights_board[nr][nc].remove(k)

        # 메두사 이동
        medusa.r, medusa.c = nr, nc

        #################################################
        ### 2단계: 메두사 시선
        #################################################
        # 시선 방향(디버깅용), 돌 수, 돌이 된 기사 정보 반환
        md, stone_cnt, stone_knights = medusa_see()

        #################################################
        ### 3단계: 기사 이동 및 공격
        #################################################
        attack_set = set()
        move_cnt = 0
        for uid, knight in knights.items():
            # 돌이 되었을 경우 넘어감
            if uid in stone_knights: continue

            sr, sc = knight.r, knight.c

            ### 기사 1차 이동 좌표 확인
            nr, nc = rev_bfs(uid, medusa.r, medusa.c, sr, sc, [3,2,1,0])
            # print()
            # 이동할 수 없을 경우 넘어감
            if nr == -1: continue
            # 이동 위치에 메두사가 있을 경우 사라지고, 메두사를 공격한 전사 수를 업데이트
            move_cnt += 1
            if medusa.r==nr and medusa.c==nc:
                attack_set.add(uid)
                continue
            ### 기사 2차 이동 좌표 확인
            nnr, nnc = rev_bfs(uid, medusa.r, medusa.c, nr, nc, [1,0,3,2])
            move_cnt += 1
            if nnr != -1 and nnc !=-1:
                if medusa.r == nnr and medusa.c == nnc:
                    attack_set.add(uid)
                else:
                    nr, nc = nnr, nnc
            ### 기사 실제 이동
            if uid not in attack_set: # 계속 생존해있을 경우
                knights_board[sr][sc].remove(uid)
                knights_board[nr][nc].add(uid)
                knight.r, knight.c = nr, nc

            # print()
        for uid in attack_set:
            knight = knights[uid]
            kr, kc = knight.r, knight.c
            knights_board[kr][kc].remove(uid)
            del knights[uid]
        answer_line = [move_cnt, len(stone_knights), len(attack_set)]
        answer.append(' '.join(map(str, answer_line)))
        # print()
    print('\n'.join(answer))
main()