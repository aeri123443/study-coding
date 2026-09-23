'''
나무박멸: 2022 상반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-kill-all/description

문제 분석: 26m 45s
코드 1차 작성: 48m 51s
  - [TC5 error] 나무가 모두 제초되었을 경우 check_kill_point에서 INF, INF 반환 -> 이후 제초 작업에서 인덱스 에러 발생
      2차 작성에서 조기 탈출 코드 작성
코드 2차 작성: 3m 17s
  - [TC7 fail] 클로드 도움: 제초 과정에서 -1(벽)을 고려하지 않고 0으로 덮어씀
      3차 작성에서 방어코드 추가
코드 3차 작성: 22m 13s

총 소요 시간: 1h 41m 8s
'''

# ==================================
# 전역 선언
# ==================================
INF = float('inf')
DEBUG = False

MOVE1 = [(0,1),(1,0),(-1,0),(0,-1)]
MOVE2 = [(1,1),(1,-1),(-1,1),(-1,-1)]

N, M, K, C = -1, -1, -1, -1

tree_board =[]
dead_board = []

# ==================================
# 보조 함수
# ==================================

def input_data():
    global N, M, K, C, tree_board, dead_board

    N, M, K, C = map(int,input().split())
    tree_board = [list(map(int,input().split())) for _ in range(N)]
    dead_board = [[0]*N for _ in range(N)]

def grow_tree():
    sum_board = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if tree_board[r][c] > 0:
                for dr, dc in MOVE1:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<N and 0<=nc<N and tree_board[nr][nc] > 0:
                        sum_board[r][c] += 1

    return sum_board

def add_tree(sum_board):
    for r in range(N):
        for c in range(N):
            if sum_board[r][c] > 0 and tree_board[r][c] != -1 :
               tree_board[r][c] += sum_board[r][c]

def extent_tree(m):
    sum_board = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if tree_board[r][c] > 0:

                add_pos = []
                for dr, dc in MOVE1:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<N and 0<=nc<N and tree_board[nr][nc]==0 and dead_board[nr][nc] < m:
                        add_pos.append((nr,nc))

                if add_pos:
                    add_num = tree_board[r][c] // len(add_pos)
                    for ar, ac in add_pos:
                        sum_board[ar][ac] += add_num

    return sum_board

# sr, sc: 제초제 뿌릴 위치
def kill_tree(sr, sc):
    result = tree_board[sr][sc]
    kill_pos = [(sr, sc)]

    for dr, dc in MOVE2:
        nr, nc = dr+sr, dc+sc
        k = 0
        while 0<=nr<N and 0<=nc<N and k < K:
            if tree_board[nr][nc] > 0:
                result += tree_board[nr][nc]
            kill_pos.append((nr,nc))

            if tree_board[nr][nc] <= 0:
                break

            nr += dr
            nc += dc
            k += 1

    return result, kill_pos

def check_kill_point():
    info = (-INF, -INF, -INF) # 킬카운트 최대, r 최소, c 최소

    for r in range(N):
        for c in range(N):
            if tree_board[r][c] > 0:
                kill_cnt, _ = kill_tree(r, c)
                info = max(info, (kill_cnt, -r, -c))

    return -info[1], -info[2]

# ==================================
# 메인 로직
# ==================================
def main():
    input_data()
    if DEBUG: print()

    answer = 0
    for m in range(1, M+1):
        # ===============
        # 1. 나무 성장
        # ===============
        sum_board = grow_tree()
        add_tree(sum_board)
        if DEBUG: print()

        # ===============
        # 2. 나무 번식
        # ===============
        sum_board = extent_tree(m)
        add_tree(sum_board)
        if DEBUG: print()

        # ===============
        # 3. 제초
        # ===============
        kr, kc = check_kill_point()
        if kr == INF:
            break
        kill_count, kill_pos = kill_tree(kr, kc)
        for r, c in kill_pos:
            if tree_board[r][c] > 0:
                tree_board[r][c] = 0
            dead_board[r][c] = m+C

        if DEBUG: print()
        answer += kill_count
    print(answer)

main()