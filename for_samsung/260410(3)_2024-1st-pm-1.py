'''
마법의 숲 탐색: 2024 상반기 오후 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration/description

문제 분석: 27m 14s
코드 작성: 1h 34m 18s
디버깅: 0s

총 소요 시간: 2h 01m 32s
'''

####################################
#### 모듈 선언 및 전역 관리
####################################
from collections import deque

N, M, K = -1, -1, -1
S_DIR = [ (+1, -1), (+2, 0), (+1, +1)] # 남쪽 좌표 확인
W_DIR = [ (-1, -1), (0, -2), (+1, -2), (+1, -1), (+2, -1) ] # 서쪽 좌표 확인
E_DIR = [ (-1, +1), (0, +2), (+1, +2), (+1, +1), (+2, +1) ] # 동쪽 좌표 확인
MOVE = [ (-1, 0), (0, +1), (+1, 0), (0, -1)] # 북 동 남 서
####################################
#### 함수 선언
####################################

# 이 방향으로 이동 가능한지 확인
def check_dir(board, si, sj, d_num):

    # 방향 저장
    if d_num == 1: move = E_DIR # 동쪽
    elif d_num == 2: move = S_DIR # 남쪽
    else: move = W_DIR # d == 3, 서쪽

    for di, dj in move:
        ni, nj = si+di, sj+dj
        # print()
        # 일단 i는 0보다 작아도 됨
        # 이동 가능, 장애물 없음 -> 패스
        if ni<N and 0<=nj<M:
            # i가 0보다 작으면 일단 장애물이 없다고 판단 (해당 공간에는 골렘이 존재해서는 안되기 때문)
            if ni < 0: continue

            # i가 0 이상이면 장애물 살피기
            elif board[ni][nj][0] < 0: continue
            else: return False
        else:
            return False

    return True

# 골렘 최종 도착 좌표, d 반환
def find_best_pos(board, c, d):
    best_dir = d
    ci, cj = -2, c
    while True:
        # 남쪽 확인 -> 도착 좌표 업데이트
        if check_dir(board, ci, cj, 2):
            ci += 1
            # best_dir = d
        # 서쪽 확인 -> 도착 좌표, d 업데이트
        elif check_dir(board, ci, cj, 3):
            ci += 1
            cj -= 1
            best_dir = (best_dir-1)%4
        # 동쪽 확인 -> 도착 좌표, d 업데이트
        elif check_dir(board, ci, cj, 1):
            ci += 1
            cj += 1
            best_dir = (best_dir+1)%4
        else:
            # 셋 다 안되면 break
            return ci, cj, best_dir

# 골렘 이동 (board 업데이트)
def move_robot(board, i, j, d_num, k):
    # 골렘 위치 지정
    board[i][j][0] = k
    board[i-1][j][0] = k
    board[i+1][j][0] = k
    board[i][j-1][0] = k
    board[i][j+1][0] = k

    # 출구 기록
    di, dj = MOVE[d_num]
    board[i+di][j+dj][1] = True

# 골렘이 숲 안에 있는지 확인
def check_robot_in(i, j):
    if 0 <= i-1 and i+1 < N and 0 <= j-1 and j+1 < M:
        return True
    return False


# 정령 이동
def move_elf(board, si, sj):
    # 디버깅 용으로 좌표 전부 저장
    max_i_pos = (si, sj)

    visited = [ [False]*M for _ in range(N) ]
    q = deque( [ (si, sj) ] )
    visited[si][sj] = True

    while q:
        ci, cj = q.popleft()

        for di, dj in MOVE:
            ni, nj = ci+di, cj+dj

            # 이동가능, 미방문
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and board[ni][nj][0] >= 0:
                # 골렘 번호 같음 -> 이동 가능!
                if board[ci][cj][0] == board[ni][nj][0]:
                    visited[ni][nj] = True
                    q.append( (ni,nj) )
                    if max_i_pos[0] < ni:
                        max_i_pos = (ni, nj)
                # 골렘 번호 달라짐 -> 현재 위치가 출구인지?
                elif board[ci][cj][1]:
                    visited[ni][nj] = True
                    q.append( (ni,nj) )
                    if max_i_pos[0] < ni:
                        max_i_pos = (ni, nj)

    return max_i_pos
####################################
#### 메인 로직
####################################
def main():
    global N, M, K

    # 초기값 입력 및 초기화
    N, M, K = map(int, input().split())
    board = [ [ [-1, False] for _ in range(M) ] for _ in range(N) ] # 숲 [골렘 번호, 출구 여부]
    score = 0

    # 요정 출발~
    for k in range(K):
        c, d = map(int, input().split())
        c -= 1 # 0 기준 좌표로 변환

        # 골렘 최종 도착 좌표, d 반환
        best_i, best_j, best_dir = find_best_pos(board, c, d)

        # 골렘이 숲 안에 있는지 확인 -> 벗어났으면 board 비우고 넘어감
        if not check_robot_in(best_i, best_j):
            board = [ [ [-1, False] for _ in range(M) ] for _ in range(N) ]
            continue

        # 골렘 이동 (board 업데이트)
        move_robot(board, best_i, best_j, best_dir, k)

        # 정령 이동
        max_i_pos = move_elf(board, best_i, best_j)

        # 점수 업데이트 (+1 잊지 말기)
        score += (max_i_pos[0]+1)

    print(score)
if __name__ == '__main__':
    main()