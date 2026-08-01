'''
미지의 공간 탈출: 2024 하반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/escape-unknown-space/description

문제 분석: 37m 14s
  - [시간 소요] 윗면 -> 옆면 계산에 오랜 시간 소요
코드 1차 작성: 3h 16m 11s
  - [시간 소요] 머리 너무 써서 그냥 코드 작성이 느렸음...
코드 1차 디버깅: 24m 27s
  - [TC3 fail] 옆면 -> 윗면을 고려하지 않음, 이에 해당 함수 추가
코드 2차 디버깅: 12m 20s:
  - [TC5 fail] 서쪽 옆면 -> 바닥 함수에서 잘못 계산한 게 있어서, 바닥으로 진입을 못함

총 소요 시간: 4h 30m 14s
'''

from collections import deque

################################################################
##### 전역 선언
################################################################

N, M, F = -1, -1, -1
floor_board = [] # 미지의 공간 평면도
wall_board = [[] for _ in range(5)] # 시간의 벽 단면도 (동0 서1 남2 북3 윗면4)
time_board = [] # 시간 이상 현상
# visited = [] # 방문 관리

INF = float('inf')
tm = {'r':-1, 'c':-1} # 타임머신 위치
cs = {'r':-1, 'c':-1, 'd':-1} # changed_side. 옆면 -> 바닥으로 가기 위한 유일한 좌표와
cf = {'r':-1, 'c':-1} # changed_floor. 옆면 -> 바닥으로 오기 위한 유일한 좌표
ex = {'r':-1, 'c':-1} # 탈출구 좌표
wall = {'sr':INF, 'er':-INF, 'sc':INF, 'ec':-INF} # 시간의 벽 양끝 좌표
MOVE = [(0,1), (0,-1), (1,0), (-1,0)] # 동서남북
################################################################
##### 기타 보조 함수
################################################################

## 시간의 벽 범위 확인
def is_range_wall(nr, nc):
    return 0<=nr<M and 0<=nc<M

## 미지의 공간 범위 확인
def is_range_floor(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

## 윗면 -> 옆면 이동
# 윗면에서 범위를 벗어날 때 선언, 다음 좌표 반환
def ceil_to_side(cr, cc, nr, nc):

    # 위 -> 동
    if nc >= M:
        return 0, M-cr-1, 0
    # 위 -> 서
    elif nc < 0:
        return 0, cr, 1
    # 위 -> 남
    elif nr >= M:
        return 0, cc, 2
    # 위 -> 북
    elif nr < 0:
        return 0, M-cc-1, 3

    return -1, -1, -1

## 옆면 -> 윗면 이동
def side_to_ceil(cr, cc, cd):
    # 공통: nr이 0보다 작아질 때 수행
    # 동 -> 위
    if cd == 0:
        return M-cc-1, M-1
    # 서 -> 위
    elif cd == 1:
        return cc, 0
    # 남 -> 위
    elif cd == 2:
        return M-1, cc
    # 북 -> 위
    else:
        return 0, M-cc-1
## 옆면 -> 밑면 이동
# 옆면에서 범위를 벗어날 때 선언, 다음 좌표 반환
def side_to_floor(cr, cc, side_d):
    sr, sc, er, ec = wall['sr'], wall['sc'], wall['er'], wall['ec']

    # 동 -> 바닥
    if side_d == 0:
        nr, nc = er-cc-1, ec
    # 서 -> 바닥
    elif side_d == 1:
        nr, nc = sr+cc, sc-1
    # 남 -> 바닥
    elif side_d == 2:
        nr, nc = er, sc+cc
    # 북 -> 바닥
    else:
        nr, nc = sr-1, ec-1-cc

    return (nr, nc) if is_range_floor(nr, nc) else (-1, -1)

## 옆면 -> 옆면 이동
# r은 그대로, c만 변화
def side_to_side(cr, cc, cd):
    # 우측 이동 (반시계, 동-북-서-남)
    if cc == M-1:
        nd_list = [3,2,0,1]
        nd = nd_list[cd]
        return cr, 0, nd
    # 좌측 이동 (시계)
    else:
        nd_list = [2,3,1,0]
        nd = nd_list[cd]
        return cr, M-1, nd


## 데이터 입력
def input_data():
    global N, M, F, floor_board, wall_board, time_board, visited

    N, M, F = map(int, input().split())

    # 미지의 공간
    floor_board = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 3: 시간의 벽
            if floor_board[r][c] == 3:
                wall['sr'] = min(wall['sr'], r)
                wall['er'] = max(wall['er'], r+1)
                wall['sc'] = min(wall['sc'], c)
                wall['ec'] = max(wall['ec'], c+1)
            # 4: 탈출구 위치
            elif floor_board[r][c] == 4:
                ex['r'], ex['c'] = r, c

    # 시간의 벽
    # (동0 서1 남2 북3 윗면4)
    for d in range(5):
        wall_board[d] = [list(map(int, input().split())) for _ in range(M)]
        # 윗면(4)에서 타임머신 찾기(2)
        if d==4:
            for r in range(M):
                for c in range(M):
                    if wall_board[d][r][c] == 2:
                        tm['r'], tm['c'] = r, c
                        wall_board[d][r][c] = 0

    # 시간 이상 현상
    time_board = [[INF]*N for _ in range(N)]
    for _ in range(F):
        r, c, d, v = map(int, input().split())

        time_board[r][c] = min(time_board[r][c], 0)

        # 시작 위치에서 , 언제 장애물이 되는지를 기록
        dr, dc = MOVE[d]
        nr, nc = r+dr, c+dc
        t = v
        while 0<=nr<N and 0<=nc<N:
            # 장애물이나 탈출구, 시간의 벽을 만나면 종료
            if floor_board[nr][nc] in (1, 3, 4):
                break

            # 이미 기록된 시간이상이 있으면 더 작은 값으로
            time_board[nr][nc] = min(time_board[nr][nc], t)

            nr += dr
            nc += dc
            t+=v

## 시간의 벽 -> 미지의 공간 통로 찾기
def find_side_to_floor():
    global cs, cf
    # 시간의 벽 주변 탐색
    for d in range(4):
        for c in range(M):
            nr, nc = side_to_floor(2, c, d)
            if is_range_floor(nr,nc) and floor_board[nr][nc] in (0, 4):
                cs['r'], cs['c'], cs['d'] = 2, c, d
                cf['r'], cf['c'] = nr, nc
                return

    # 그 주변 좌표가 0이면 유일한 통로임!

################################################################
##### 메인 로직
################################################################
def main():
    ##########################
    ### 0단계: 초기 데이터 처리
    ##########################

    # 데이터 입력
    input_data()

    # 시간의 벽 -> 미지의 공간 통로 찾기
    find_side_to_floor()
    # print('tm: ', tm, 'cs: ', cs, 'cf: ', cf, 'ex: ', ex, 'wall: ', wall)

    # print()
    ##########################
    ### 1단계: 이동 (bfs)
    ##########################
    visited_floor = [[-1]*N for _ in range(N)]
    visited_wall = [[[-1]*M for _ in range(M)] for _ in range(5)]

    tr, tc = tm['r'], tm['c']
    q = deque([ (tr, tc, 4, 0)   ]) # r, c, d, t
    visited_wall[4][tr][tc] = 0 # 시작은 시간의 벽 윗면

    def append_q(_nr, _nc, _nd, _nt):
        # 미지의 공간
        if _nd == 5:
            visited_floor[_nr][_nc] = _nt
        # 시간의 벽
        else:
            visited_wall[_nd][_nr][_nc] = _nt
        q.append((_nr, _nc, _nd, _nt))
        # print_visited_by_q(cr, cc, nr, nc, _nd, ct + 1)

    # 어떤 상황에서 어떤 다음으로 넘어갔는지 출력
    def print_visited_by_q(_cr, _cc, _nr, _nc, _nd, _nt):
        print()
        print(f'cr:{_cr}, cc:{_cc}, nr:{_nr}, nc:{_nc}, nt:{_nt}')

        for _d in range(5):
            if _d == 0: print('\n동:')
            elif _d == 1: print('\n서:')
            elif _d == 2: print('\n남:')
            elif _d == 3:print('\n북:')
            else: print('\n윗면:')

            for i in range(M):
                print(' '.join(map(str, visited_wall[_d][i])))

        print('\n미지의 공간:')
        for i in range(N):
            print(' '.join(map(str, visited_floor[i])))

    while q:
        # d: 0동 1서 2남 3북 4윗면 5바닥(미지공간)
        cr, cc, cd, ct = q.popleft()

        # print()
        # 시간 이상에 걸렸을 경우 패스
        if cd==5 and ct >= time_board[cr][cc]: continue
        # 탈출구일 경우 종료
        if cd==5 and (cr, cc) == (ex['r'], ex['c']): break

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            # 현재 미지 공간일 경우
            if cd == 5:
                if is_range_floor(nr, nc) and visited_floor[nr][nc] == -1 and floor_board[nr][nc] in (0,4):
                    append_q(nr, nc, cd, ct + 1)
                # print(f'-----cr:{cr}, cc:{cc}, nr:{nr}, nc:{nc}, cd:{cd} end-----')
            # 현재 시간 벽일 경우
            else:
                if is_range_wall(nr, nc):
                    # 미방문, 장애물, 시간이상(시간의 벽은 해당 안됨)
                    if visited_wall[cd][nr][nc] == -1 and wall_board[cd][nr][nc] != 1:
                        append_q(nr, nc, cd, ct+1)
                    # print(f'-----cr:{cr}, cc:{cc}, nr:{nr}, nc:{nc}, cd:{cd} end-----')
                else:
                    # 윗면일 경우 옆면으로
                    if cd == 4:
                        nr, nc, nd = ceil_to_side(cr, cc, nr, nc)
                        if visited_wall[nd][nr][nc] == -1 and wall_board[nd][nr][nc]==0:
                            append_q(nr, nc, nd, ct+1)
                        # print(f'-----cr:{cr}, cc:{cc}, cd:{cd}, nr:{nr}, nc:{nc}, nd:{nd} end-----')
                    # 옆면일 경우 다른 옆면 또는 아랫면, 또는 윗면
                    else:
                        # 옆면으로 (c가 범위 밖)
                        if not 0<=nc<M:
                            nr, nc, nd = side_to_side(cr, cc, cd)
                            if visited_wall[nd][nr][nc] == -1 and wall_board[nd][nr][nc] != 1:
                                append_q(nr, nc, nd, ct + 1)
                            # print(f'-----cr:{cr}, cc:{cc}, nr:{nr}, nc:{nc}, nd:{nd} end-----')
                        # 아랫면으로 (r이 M 이상)
                        elif nr >= M:
                            nr, nc = side_to_floor(cr, cc, cd)
                            nd = 5
                            if is_range_floor(nr,nc) and visited_floor[nr][nc] == -1 and floor_board[nr][nc] not in (1, 3):
                                append_q(nr, nc, nd, ct + 1)
                            # print(f'-----cr:{cr}, cc:{cc}, cd:{cd}, nr:{nr}, nc:{nc}, nd:{nd} end-----')
                        # 윗면으로 (r이 0 미만)
                        elif nr < 0:
                            nr, nc = side_to_ceil(cr, cc, cd)
                            nd = 4
                            if visited_wall[nd][nr][nc] == -1 and wall_board[nd][nr][nc] != 1:
                                append_q(nr, nc, nd, ct + 1)
    # print()
    print(visited_floor[ex['r']][ex['c']])

main()

