'''
모의고사 1회 - 2번
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4801/curated-cards/mock-special-bucket/description

문제 분석: 36m 14s
코드 1차 작성: 55m 9s
 - fail 없이 바로 all pass.

총 소요 시간: 1h 31m 23s
'''
from itertools import product

# ======================================
# 전역
# ======================================
DEBUG = False
N, M = -1, 4
MOVE = [(), (-1,0), (-1,-1), (0,-1), (1,-1), (+1,0), (1,1), (0,1), (-1,1)]
BLOCK_INFO = [-1]

# ======================================
# 메인 로직
# ======================================
def input_data():
    global N, M, BLOCK_INFO

    n = int(input())
    N = n + 1
    for i in range(1, 9):
        BLOCK_INFO.append(list(map(int, input().split())))

    blocks = []
    zero_list = [] # (i)
    for i in range(n):
        k, c = map(int, input().split())
        c -= 1
        if c == -1:
            zero_list.append(i)
        blocks.append([k, c])

    block_tc = []
    for c_tu in product([0,1,2,3], repeat=len(zero_list)):
        tmp = blocks[:]
        for i in range(len(zero_list)):
            b_idx = zero_list[i]
            tmp[b_idx] = [tmp[b_idx][0], c_tu[i]]
        block_tc.append(tmp)

    return block_tc

def gravity_item(board, k, sc): # 9m 23s
    r = 0
    while 0 <= r < N:
        if board[r][sc] != 0:
            break
        r += 1

    board[r-1][sc] = k
    return r-1

def check_line(board, r):
    for c in range(M):
        if board[r][c] == 0:
            return False
    return True

def gravity_all(board): # 7m 49s
    new_board = [[0] * 4 for _ in range(N)]

    for c in range(M):
        stack = []
        for r in range(N):
            if board[r][c] != 0:
                stack.append(board[r][c])

        r = N-1
        while stack and 0 <= r:
            new_board[r][c] = stack.pop()
            r -= 1

    return new_board

def move_blocks(board): # 9m 35s
    new_board = [[0] * 4 for _ in range(N)]

    for r in range(N):
        for c in range(M):
            k = board[r][c]
            if k == 0: continue

            for d in BLOCK_INFO[k]:
                dr, dc = MOVE[d]
                nr, nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M:
                    if new_board[nr][nc] != 0:
                        new_board[nr][nc] = min(new_board[nr][nc], k)
                    else:
                        new_board[nr][nc] = k
                    break

    return new_board

# ======================================
# 보조 함수
# ======================================
def main():
    block_tc = input_data() # 20m 46s

    answer = 0
    for blocks in block_tc:
        score = 0
        board = [[0] * 4 for _ in range(N)]
        for k, sc in blocks:
            # ==================================
            # 1. 블록 투입
            # ==================================

            sr = gravity_item(board, k, sc)

            is_full = check_line(board, sr)
            if is_full:
                board[sr] = [0,0,0,0]
                score += 1

                board = gravity_all(board)
            if DEBUG: print()

            # ==================================
            # 2. 블록 이동
            # ==================================
            board = move_blocks(board)
            board = gravity_all(board)

            if DEBUG: print()

            is_deleted = False
            for r in range(N):
                is_full = check_line(board, r)
                if is_full:
                    board[r] = [0, 0, 0, 0]
                    score += 1
                    is_deleted = True
            if is_deleted:
                board = gravity_all(board)
            if DEBUG: print() # 4m 9s
        answer = max(answer, score)

    print(answer)

main()