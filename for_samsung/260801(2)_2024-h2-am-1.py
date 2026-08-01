'''
미지의 공간 탈출: 2024 하반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/escape-unknown-space/description

문제 분석: 17m 45s
코드 1차 작성: 2h 01m 08s
  - [시간 소요] move_in_3d 매핑하기..
최종 디버깅: 2m 50s
  - [TC2 fail] 시간의 벽 탐색하는데 i,j range를 N으로 잡아버림 (오타..)

총 소요 시간: 2h 21m 43s
'''

from collections import deque

#######################################################
##### 전역 선언
#######################################################
N, M, F = -1, -1, -1

board_2d = [] # 미지의 공간
board_3d = [] # 시간 이상
time_board = [] # 시간이상 기록

INF = float('inf')
MOVE = [(0,+1), (0,-1), (+1,0), (-1,0)] #동서남북
WR, WC = -1, -1 # 미지의 공간 기준, 시간의 벽 시작 좌표

#######################################################
##### 보조 함수
#######################################################

### 범위 내 여부 확인
def is_range(r, c, n):
    return 0<=r<n and 0<=c<n

### 데이터 입력
def input_data():
    global N, M, F, board_2d, board_3d, time_board

    N, M, F = map(int, input().split())
    board_2d = [list(map(int, input().split())) for _ in range(N)]
    board_3d = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]

    # 시간 이상 현상 해결
    time_board = [[INF]*N for _ in range(N)]
    for _ in range(F):
        r, c, d, v = map(int, input().split())
        time_board[r][c] = 0

        dr, dc = MOVE[d]
        nr, nc = dr+r, dc+c
        nv = v

        while is_range(nr, nc, N):
            # 장애물이 아니고, 탈출구가 아닌 경우에만 수행
            if board_2d[nr][nc] in (1,3,4):
                break

            time_board[nr][nc] = min(time_board[nr][nc], nv)
            nr += dr
            nc += dc
            nv += v

### 시간의 벽 시작점 업데이트
def find_3d_start_in_2d():
    global WR, WC

    for i in range(N):
        for j in range(N):
            if board_2d[i][j] == 3:
                WR, WC = i, j
                return

### 시간의 벽에서의 이동
def move_in_3d(nr, nc, cd):
    rev = lambda a: M-a-1

    # 윗면에서
    if cd == 4:
        if nr == -1:     return 0, rev(nc), 3        # 북쪽으로
        elif nc == -1:   return 0, nr, 1             # 서쪽으로
        elif nr == M: return 0, nc, 2             # 남쪽으로
        elif nc == M: return 0, rev(nr), 0        # 동쪽으로
    # 동쪽에서
    elif cd == 0:
        if nr == -1:     return rev(nc), M-1, 4      # 윗면으로
        elif nc == -1:   return nr, M-1, 2           # 남쪽으로
        elif nr == M: return WR+rev(nc), WC+M, 5  # 바닥으로
        elif nc == M: return nr, 0, 3             # 북쪽으로
    # 서쪽에서
    elif cd == 1:
        if nr == -1:         return nc, 0, 4         # 윗면으로
        elif nc == -1:       return nr, M-1, 3       # 북쪽으로
        elif nr == M:   return WR+nc, WC-1, 5   # 바닥으로
        elif nc == M:   return nr, 0, 2         # 남쪽으로
    # 남쪽에서
    elif cd == 2:
        if nr == -1:         return  M-1, nc, 4      # 윗면으로
        elif nc == -1:       return nr, M-1, 1       # 서쪽으로
        elif nr == M:   return WR+M, WC+nc, 5   # 바닥으로
        elif nc == M:   return nr, 0, 0         # 동쪽으로
    # 북쪽에서
    elif cd == 3:
        if nr == -1:         return 0, M-1-nc, 4     # 윗면으로
        elif nc == -1:       return nr, M-1, 0       # 동쪽으로
        elif nr == M:   return WR-1, WC+rev(nc), 5 # 바닥으로
        elif nc == M:   return nr, 0, 1         # 서쪽으로

    return -1, -1, -1

### 3d -> 2d 유일한 통로 찾기
def find_exit_3d_to_2d():
    for r in range(WR, WR+M):
        for c in range(WC, WC+M):
            # WR, WC 기준 주변 탐색
            for dr, dc in MOVE:
                nr, nc = dr+r, dc+c
                # 0이 나오면 탐색 종료
                if is_range(nr, nc, N) and board_2d[nr][nc] == 0:
                    return nr, nc

    return -1, -1

### 시간의 벽 시작점 반환
def find_3d_start_in_3d():
    board = board_3d[4]

    for i in range(M):
        for j in range(M):
            if board[i][j] == 2:
                return i, j

    return -1, -1

### 시간의 벽 탈출
def bfs_3d(er, ec):

    # 시작점 찾기
    def find_start():
        board = board_3d[4]

        for i in range(M):
            for j in range(M):
                if board[i][j] == 2:
                    board[i][j] = 0
                    return i, j

        return -1, -1

    visited = [[[-1]*M for _ in range(M)] for _ in range(5)]
    sr, sc = find_start()
    visited[4][sr][sc] = 0
    q = deque([(sr, sc, 4)])

    while q:
        cr, cc, cd = q.popleft()
        cnt = visited[cd][cr][cc]

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            if is_range(nr, nc, M):
                if board_3d[cd][nr][nc]!=1 and visited[cd][nr][nc]==-1:
                    visited[cd][nr][nc] = cnt + 1
                    q.append((nr,nc,cd))
            else:
                nr, nc, nd = move_in_3d(nr, nc, cd)
                if nd == 5:
                    if is_range(nr, nc, N) and (nr,nc)==(er,ec):
                        return cnt + 1
                else:
                    if is_range(nr, nc, M) and visited[nd][nr][nc]==-1 and board_3d[nd][nr][nc]!=1:
                        visited[nd][nr][nc] = cnt + 1
                        q.append((nr,nc,nd))

    return -1

### 미지의 공간 탈출
def bfs_2d(sr, sc, scnt):
    visited = [[-1]*N for _ in range(N)]
    visited[sr][sc] = scnt
    q = deque([(sr, sc)])

    while q:
        cr, cc = q.popleft()
        cnt = visited[cr][cc]

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if is_range(nr, nc, N) and visited[nr][nc]==-1 and board_2d[nr][nc] not in (1, 3) and (cnt+1) < time_board[nr][nc]:
                if board_2d[nr][nc] == 4:
                    return cnt + 1

                visited[nr][nc] = cnt+1
                q.append((nr, nc))
    return -1

#######################################################
##### 메인 로직
#######################################################
def main():

    ####################################
    ### 0: 데이터 입력 및 전처리
    ####################################

    # 데이터 기본 입력
    input_data()

    # 시간의 벽 시작점 업데이트
    find_3d_start_in_2d()

    # 3d -> 2d 유일한 통로 찾기
    ex_2d_r, ex_2d_c  = find_exit_3d_to_2d()
    
    ####################################
    ### 1: 시간의 벽 탈출
    ####################################

    # ex_2d_r, ex_2d_c 도달하는 데 걸리는 시간 반환
    cnt_3d_to_2d = bfs_3d(ex_2d_r, ex_2d_c)

    # 탈출 불가할 경우 -1 출력
    if cnt_3d_to_2d == -1 or cnt_3d_to_2d >= time_board[ex_2d_r][ex_2d_c]:
        print(-1)
        return

    # print()

    ####################################
    ### 2: 미지의 공간 탈출
    ####################################

    # 미지의 공간 탈출까지 걸리는 시간 반환
    cnt_2d_to_out = bfs_2d(ex_2d_r, ex_2d_c, cnt_3d_to_2d)
    # print()
    # 탈출 불가할 경우, -1 반환
    if cnt_2d_to_out == -1:
        print(-1)
    # 탈출 가능할 경우, cnt 합 반환
    else:
        print(cnt_2d_to_out)

main()

