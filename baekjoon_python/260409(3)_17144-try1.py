'''
17144. <골드 4> 미세먼지 안녕!
https://www.acmicpc.net/problem/17144

문제 읽고 코드 작성: 1h 36m 55s
디버깅: 0s

총 풀이 시간: 1h 36m 55s
'''

###########################
#### 전역 변수 선언
###########################
N, M, T = 0, 0, 0 # 행:r, 열:c, 초:t
move = [(1,0), (-1,0), (0,1), (0,-1)]
###########################
#### 함수 선언
###########################

# 공기청정기 위치 찾기
def find_clear_pos(board):
    clear_pos = []

    for i in range(N):
        if board[i][0] == -1:
            clear_pos.append(i)

    return sorted(clear_pos)


# 확산 - 미세먼지를 리스트에 담음
def find_dust(board):
    dust_pos = [] # (i, j, 확산량)

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                value = board[i][j] // 5
                dust_pos.append((i, j, value))

    return dust_pos


# 확산 - 리스트 순회하며 계산
def move_dust(board, dust_pos):
    # 각 미세먼지에 대하여
    for ci, cj, value in dust_pos:

        # 확산량이 0 이하면 확산을 진행하지 않음
        if value <= 0:
            continue

        # 4방향에 대해서
        for di, dj in move:
            ni, nj = ci + di, cj + dj

            # 이동 가능, 공기청정기 없는지 확인 후
            if 0<=ni<N and 0<=nj<M and board[ni][nj] != -1:
                # 인접 좌표에 +, 자기 자신 좌표에 -
                board[ni][nj] += value
                board[ci][cj] -= value
            # print()

# 공기 청정 - 위쪽 순환 (-1 만나는 미세먼지는 소멸)
# (보드, 위쪽 공기청정기의 i 좌표)
def clear_dust_up(board, si):
    left, right = 0, M-1
    top, bottom = 0, si

    # 왼쪽
    j = 0
    for ni in range(bottom, top, -1):
        ci = ni - 1
        if board[ni][j] == -1: continue
        board[ni][j] = board[ci][j]
    # print()

    # 위쪽
    i = 0
    for nj in range(left, right, +1):
        cj = nj + 1
        if board[i][nj] == -1: continue
        board[i][nj] = board[i][cj]
    # print()

    # 오른쪽
    j = right
    for ni in range(top, bottom, +1):
        ci = ni + 1
        if board[ni][j] == -1: continue
        board[ni][j] = board[ci][j]
    # print()

    # 아래쪽
    i = bottom
    for nj in range(right, left, -1):
        cj = nj - 1
        if board[i][cj] == -1:
            board[i][nj] = 0
            continue
        board[i][nj] = board[i][cj]
    # print()

# 공기 청정 - 아래쪽 순환 (-1 만나는 미세먼지는 소멸)
# (보드, 아래쪽 공기청정기의 i 좌표)
def clear_dust_down(board, si):
    left, right = 0, M-1
    top, bottom = si, N-1

    # 왼쪽
    j = left
    for ni in range(top, bottom, +1):
        ci = ni + 1
        if board[ni][j] == -1: continue
        board[ni][j] = board[ci][j]

    # 아래쪽
    i = bottom
    for nj in range(left, right, +1):
        cj = nj + 1
        board[i][nj] = board[i][cj]

    # 오른쪽
    j = right
    for ni in range(bottom, top, -1):
        ci = ni - 1
        board[ni][j] = board[ci][j]

    # 위쪽
    i = top
    for nj in range(right, left, -1):
        cj = nj - 1
        if board[i][cj] == -1:
            board[i][nj] = 0
            continue
        board[i][nj] = board[i][cj]

# 전체 합 (-1 제외)
def sum_board(board):
    result = 0

    for i in range(N):
        result += sum(board[i])

    return result + 2 # 공기청정기때문에 빼진 값을 더함

###########################
#### 메인 로직
###########################
def main():
    global N, M, T, clear_pos

    N, M, T = map(int, input().split())

    # 초기 보드판 입력
    board = [ list(map(int, input().split())) for _ in range(N)]
    # 공기청정기 위치 찾기
    clear_pos = find_clear_pos(board)

    # T초 동안 진행
    for t in range(T):
        # 확산 - 미세먼지를 리스트에 담음
        # (i, j, 확산량)
        dust_pos = find_dust(board)

        # 확산 - 리스트 순회하며 계산
        move_dust(board, dust_pos)
        # print()

        # 공기 청정 - 위쪽 순환 (-1 만나는 미세먼지는 소멸)
        clear_dust_up(board, clear_pos[0])
        # 공기 청정 - 아래쪽 순환 (-1 만나는 미세먼지는 소멸)
        clear_dust_down(board, clear_pos[1])

        # print()

    # 전체 합 (-1 제외)
    sum_result = sum_board(board)

    print(sum_result)

main()