"""
누렁이의 풀 뜯기
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4805/curated-cards/mock-cow-grass/description
    시간복잡도 : print(150 * 250 * 250 * 2) = 18750000

    [?] 누렁이가 있는 위치가 돌이 된다면? -> 그런 경우 없다고 써있넴

    케이스 확인
        - 자기 자신 위치에 그대로 있는 경우
        - 모두 0밖에 없을 경우: 0이라도 먹음

    N(2~250), 1-idx
    누렁이 위치 (,)
    목장
        - 풀의 양 X_ij
        - 하루에 A_ij만큼 자람
        풀: X, A
        돌: -1, -1

    풀, 돌
    Q일(1~150)
        1. 아침: 목장 관리
            1-1. 돌 제거 및 풀 심기
                - 100, r, c, x, a
            1-2. 풀 제거 및 돌 심기
                - 200, r, c
        2. 낮: 누렁이 식사
            - 누렁이 이동
                - [!] 자기 자신 위치 포함
                - 이동 가능: 풀밭 구역
                - 풀의 양 최대, 행 최소, 열 최소
            - 식사
                - 풀 모두 먹음 -> 풀의 양 0, 성장 속도는 그대로
            - 누렁이 위치 갱신
            - 누렁이가 먹은 풀의 양 합산
        3. 밤: 풀 성장
            - 풀밭구역 풀의 양이 i,j만큼 증가

    출력: 최종, 누렁이가 먹은 풀의 총량



    # 1회독 3m 16s
    # 2회독 15m 13s 특별히 생각해봐야 할 문제가 없어 보여서 바로 문제로 들어감
    # 총 소요 시간 44m 15s
"""

# 케이스 확인
# - 자기 자신 위치에 그대로 있는 경우 -> 예제 테케에 있음
# - 모두 0밖에 없을 경우: 0이라도 먹음 -> 통과
    # 3 1 3
    # 20 3 -1 -1 0 3
    # -1 -1 -1 -1 0 8
    # 0 7 0 3 0 1
    # 1
    # 100 2 2 0 5

from collections import deque

DEBUG = False
INF = float('inf')
MOVE = [(1,0), (0,1), (-1,0), (0,-1)]

N, R, C = map(int, input().split())
R -= 1; C-=1
board = []

def input_board_data(): # 9m 38s
    for _ in range(N):
        line = list(map(int, input().split()))
        row = []
        for idx in range(N):
            x, a = line[2*idx], line[2*idx+1]
            row.append([x,a])
        board.append(row)

# 1. 누렁이 이동
# - [!] 자기 자신 위치 포함
def get_nu_next():
    max_info = (board[R][C][0], -R, -C) # - 풀의 양 최대, 행 최소, 열 최소

    q = deque([(R, C)])
    visited = [[False]*N for _ in range(N)]
    visited[R][C] = True

    while q:
        cr,cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            # 이동 가능: 풀밭 구역
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and board[nr][nc][0] != -1:
                max_info = max(max_info, (board[nr][nc][0], -nr, -nc))
                q.append((nr,nc))
                visited[nr][nc] = True

    return max_info[0], -max_info[1], -max_info[2]

def main():
    global R, C

    input_board_data()
    # if DEBUG: print()

    answer = []
    for _ in range(int(input())):
        # ========================================
        # 1. 아침: 목장 관리 4m 33s
        # ========================================
        cmd, *line = map(int, input().split())

        # 1-1. 돌 제거 및 풀 심기
        if cmd == 100:
            r, c, x, a = line
            board[r-1][c-1] = [x,a]
        # 1-2. 풀 제거 및 돌 심기
        elif cmd == 200:
            r, c = line
            board[r-1][c-1] = [-1,-1]

        # if DEBUG: print()

        # ========================================
        # 2. 낮: 누렁이 식사 09m 48s
        # ========================================

        # 누렁이 이동
        amount, nr, nc = get_nu_next()

        # 식사
        board[nr][nc][0] = 0
        R, C = nr, nc
        answer.append(amount)

        # if DEBUG: print()

        # ========================================
        # 3. 밤: 풀 성장 1m 43s
        # ========================================
        for r in range(N):
            for c in range(N):
                if board[r][c][0] > -1:
                    board[r][c][0] += board[r][c][1]

    if DEBUG: print()
    print(str(sum(answer)))
    # 출력: 최종, 누렁이가 먹은 풀의 총량

main()