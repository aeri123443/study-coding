'''
11559. <골드 4> Puyo Puyo
https://www.acmicpc.net/problem/11559

문제 읽고 분석: 8m 58s
코드 작성: 47m 13s
디버깅: 0s

총 풀이 시간: 56m 11s
'''

from collections import deque

#####################################
##### 전역변수 선언
#####################################

N, M = 12, 6 # 행, 열
answer = 0 # 연쇄 횟수
move = [(1,0), (-1,0), (0,1), (0,-1)]
block_map = { v:i for i, v in enumerate(['.', 'R', 'G', 'B', 'P', 'Y']) }

#####################################
##### 함수 구현
#####################################

## 값 입력받고 매핑하여 반환
# board = [ list(input().strip()) for _ in range(N)]
def input_board():
    board = []

    for _ in range(N):
        input_row = list(input().strip())
        new_row = []
        for y in input_row:
            new_row.append( block_map[y] )
        board.append( new_row )

    return board

# 4개 이상 붙어있는 색상 블록이 있을 경우 반환
def bfs_four_color(board, visited, si, sj):
    blocks = []

    q = deque()
    q.append((si, sj))
    target_color = board[si][sj]
    visited[si][sj] = True
    blocks.append((si, sj))


    while q:
        ci, cj = q.popleft()

        for di, dj in move:
            ni, nj =  ci + di, cj + dj

            if 0<=ni<N and 0<=nj<M and board[ni][nj] == target_color and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                blocks.append((ni, nj))

    if len(blocks) >= 4:
        return blocks
    else:
        return []


# 4개 이상의 색상이 붙어있는지 탐색
def find_same_color(board):
    group_pos = []
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] > 0:
                blocks = bfs_four_color(board, visited, i, j)
                group_pos.extend(blocks)
                # print(blocks)

    return group_pos

# 4개 이상인 블록 제거
def remove_block(board, group_pos):
    # group_pos 좌표에 해당하는 블록을 제거 (n->0)
    for i, j in group_pos:
        board[i][j] = 0

    return board

# 아래가 비어있으면 아래로 떨어짐
def move_down(board):
    for j in range(M):
        new_col = [0] * N
        idx = N-1

        # 비어있지 않으면 아래에서부터(거꾸로) new_col에 순차적으로 담음
        for i in range(N-1, -1, -1):
            if board[i][j] > 0:
                new_col[idx] = board[i][j]
                idx -= 1

        # new_col를 board에 넣음
        for i in range(N):
            board[i][j] = new_col[i]

    return board
#####################################
##### 메인 로직
#####################################

# 값 입력
# board = [ list(input().strip()) for _ in range(N)]
board = input_board()
# print()

# 더 터뜨릴 것이 없을 때까지 반복
while True:
    # 같은 색상 탐색
    group_pos = find_same_color(board)
    # print()

    # 터뜨릴 것이 있으면 연쇄 1 추가
    if len(group_pos) > 0:
        answer += 1
    # 더 터뜨릴 것이 없으면 종료
    else:
        print(answer)
        break

    # 4개 이상인 블록 제거
    board = remove_block(board, group_pos)
    # print()

    # 아래로 떨어짐
    board = move_down(board)
    # print()
    # break
