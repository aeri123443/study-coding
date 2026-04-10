'''
21609. <골드 1> 상어 중학교
https://www.acmicpc.net/problem/21609

문제 분석: 17m 14s
코드 작성: 1h 18m 18s
디버깅: 0s

총 풀이 시간: 1h 36m 0s
'''
from collections import deque

############################################
#### 전역 관리
############################################
N, M = 0, 0
MOVE = [(1,0), (-1,0), (0,1), (0,-1)]

############################################
#### 함수 선언
############################################

# 무지개 블록 위치 찾기
def find_rainbow(board):
    pos = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                pos.append((i, j))

    return pos

# 그룹화
def grouping(board, visited, rainbow_pos, si, sj):
    # 일반블록 컬러, 블록 좌표
    num = board[si][sj] # 일반블록 색상
    group_pos = [] # 그룹 전체 좌표
    visited_rainbow = [] # 방문한 무지개블록 좌표
    default_block = (si, sj) # 기준 블록 좌표 (일반 블록)

    # bfs 초기 설정
    visited[si][sj] = True
    q = deque( [(si, sj)] )
    group_pos.append( (si, sj) )

    while q:
        ci, cj = q.popleft()

        for di, dj in MOVE:
            ni, nj = ci+di, cj+dj

            # 이동 가능 좌표, 미방문, 검정 블록(-1), 빈공간(-2) 아님
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and board[ni][nj] >= 0:
                # 무지개 블록이거나 동일 색상 블록일 때
                if board[ni][nj] == 0 or board[ni][nj] == num:
                    # 무지개 블록이면 visited_rainbow에도 업데이트
                    if board[ni][nj] == 0:
                        visited_rainbow.append((ni, nj))
                    # 일반 블록이면 r, c가 작은 값을 기준 블록으로 업데이트
                    else:
                        default_block = min(default_block, (ni, nj))
                    visited[ni][nj] = True
                    group_pos.append( (ni,nj) )
                    q.append((ni, nj))

    # 무지개 블록의 좌표는 다시 visited를 false로 설정해야, 이후 다시 탐색할 수 있다.
    for ri, rj in visited_rainbow:
        visited[ri][rj] = False

    # 반환: 크기, 무지개 개수, 기준블록 r, 기준블록 c, 그룹 좌표 리스트
    return len(group_pos), len(visited_rainbow), default_block[0], default_block[1], group_pos

# 그룹화 및 타겟 그룹 선정(업데이트), 해당 그룹의 좌표를 반환
def find_group_pos(board, rainbow_pos):
    # 크기, 무지개 개수, 기준블록 r, 기준블록 c, 그룹 좌표 리스트
    # 어차피 비교는 기준블록 c에서 끝날 것이므로, 그룹 좌표 리스트를 넣어도 괜찮음!
    group_info = ( -1, -1, -1, -1, [] )
    visited = [[False] * N for _ in range(N)]

    # 방문하지 않은 좌표중에서, 일반블록
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                # 반환: 크기, 무지개 개수, 기준블록 r, 기준블록 c, 그룹 좌표 리스트
                tmp_group_info = grouping(board, visited, rainbow_pos, i, j)
                if tmp_group_info[0] >= 2:
                    group_info = max(group_info, tmp_group_info)
                # print()

    return group_info[-1]

# 타겟 그룹의 블록들을 제거
def remove_blocks(board, group_pos):
    for i, j in group_pos:
        board[i][j] = -2

# 중력 적용
def move_down(board):

    for j in range(N):
        col = [-2] * N
        idx = N-1

        for i in range(N-1, -1, -1):
            # -2면 넘어감
            if board[i][j] == -2:
                continue
            # -1이면 해당 위치에 -1 넣고, idx 업데이트
            elif board[i][j] == -1:
                col[i] = -1
                idx = i-1
            # 그 이상이면 다음 col에 값 넣고 idx 업데이트
            else:
                col[idx] = board[i][j]
                idx -= 1

        # 보드 업데이트
        for i in range(N):
            board[i][j] = col[i]

# 반시계 회전
def rotate(board):
    new_board = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[N-j-1][i] = board[i][j]

    return new_board
############################################
#### 메인 로직
############################################

def main():
    global N, M

    # 입력
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 점수
    score = 0

    while True:
        # 무지개 블록 위치 찾기
        rainbow_pos = find_rainbow(board)

        # 그룹화 및 타겟 그룹 선정(업데이트), 해당 그룹의 좌표를 반환
        group_pos = find_group_pos(board, rainbow_pos)
        # print()

        # 타겟 그룹이 없으면 종료
        if len(group_pos) == 0:
            print(score)
            return

        # 타겟 그룹의 블록들을 제거, 점수 업데이트
        remove_blocks(board, group_pos)
        score += (len(group_pos)*len(group_pos))
        # print()

        # 중력 적용
        move_down(board)
        # print()

        # 반시계 회전
        board = rotate(board)
        # print()

        # 중력 적용
        move_down(board)
        # print()

if __name__ == "__main__":
    main()
