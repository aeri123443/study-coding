'''
모의고사 1회 - 1번
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4801/curated-cards/mock-special-bucket/description

문제 분석: 25m 44s
코드 1차 작성: 1h 39m 14s

- tc fail 없이 통과
총 소요 시간: 2h 4m 58s
'''


# 분석 25m 44s
from itertools import product

# ===============================================
# 전역 및 클래스 4m  12s
# ===============================================
DEBUG = False
N = int(input())
MOVE = [(-1,0), (0,1), (1,0), (0,-1)]
change_d = { 1: [1,0,3,2], 2: [3,2,1,0] }

# items = {} # num: (r,c,d)
# ===============================================
# 보조 함수
# ===============================================

def input_data(): # 12m 13s + 20m 54s
    board = [list(map(int, input().split())) for _ in range(N)]

    # 3인 곳좌표
    three = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 3:
                three.append((r,c))

    # 보드 경우의 수
    l = len(three)
    boards = []
    for tu in product([0,1,2], repeat=l):
        tmp_board = [board[r][:] for r in range(N)]
        for idx in range(l):
            r, c = three[idx]
            v = tu[idx]
            tmp_board[r][c] = v
        boards.append(tmp_board)

    # 초기 구슬 상태
    items = {}
    arr = list(map(int, input().split()))
    for i in range(0,N):
        r, c, d = -1, i%N, 2
        if arr[i] == 1: items[i] = (r, c, d)

    for i in range(N,N*2):
        r, c, d = i%N, N, 3
        if arr[i] == 1: items[i] = (r, c, d)

    for i in range(N*2,N*3):
        r, c, d = N, (N-i%N-1), 0
        if arr[i] == 1: items[i] = (r, c, d)

    for i in range(N*3,N*4):
        r, c, d = (N-i%N-1), -1, 1
        if arr[i] == 1: items[i] = (r, c, d)

    return boards, items

# cur
def is_not_conflict(bar_type, prev_items, conflict_candidates, r, c):
    real_pos = [[list() for _ in range(2)] for _ in range(2)]

    for num in conflict_candidates:
        cd = prev_items[num][2]
        if bar_type == 1:
            if cd in (1, 2): real_pos[0][0].append(num)
            else: real_pos[0][1].append(num)
        else:
            if cd in (0, 1): real_pos[1][0].append(num)
            else: real_pos[1][1].append(num)

    alive_items = []
    for r in range(2):
        for c in range(2):
            if len(real_pos[r][c]) == 1:
                alive_items.append(real_pos[r][c][0])

    return alive_items

def move_items(board, items): # 54m 31s (갈아엎음 중간에)

    # 다음 위치 기록
    item_board = [[list() for _ in range(N)]for _ in range(N)]
    escape = 0
    for num, (cr, cc, cd) in items.items():
        dr, dc = MOVE[cd]
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<N:
            item_board[nr][nc].append(num)
            # if board[nr][nc] == 0:
            #     # 빈 공간, 구슬 없음
            #     if item_board[nr][nc] == -1:
            #         new_items[num] = (nr,nc,cd)
            #         item_board[nr][nc] = num
            #     # 빈 공간, 구슬 있음 -> 사라짐
            #     elif item_board[nr][nc] >= 0: # (구슬 있음):
            #         del new_items[item_board[nr][nc]]
            #         item_board[nr][nc] = -2
            #     # -2인 경우 사라지고 특별히 영향을 주지 않음
            # if board[nr][nc] in (1,2):
            #     # 슬래시, 구슬 없음
            #     if item_board[nr][nc] == -1:
            #         nd = change_d[board[nr][nc]][cd]
            #         new_items[num] = (nr,nc,nd)
            #         item_board[nr][nc] = num
            #     # 슬래시, 구슬 있음
            #     # 벽 기준으로도 충돌하지 않는지 확인
            #     else:
            #         is_bar_conflict()
                # -2dlfEo
        else: # 탈출
            escape += 1

    # 충돌 탐지 및 남은 아이템 업데이트
    new_items = {}
    for r in range(N):
        for c in range(N):
            if len(item_board[r][c]) == 1:
                num = item_board[r][c][0]
                d = items[num][2]

                if board[r][c] == 0: # 빈공간
                    nd = d
                else: # 방향 전환
                    nd = change_d[board[r][c]][d]

                new_items[num] = (r,c, nd)

            # elif len(item_board[r][c]) > 1: # 충돌

                # 빈공간 -> 바로 소멸
                # 바 있음 -> 방향에 따라 소멸 여부 결정
                # if board[r][c] in (2,3):
                #     alive_items = is_not_conflict(board[r][c], items, item_board[r][c], r, c)
                #     # 소멸되지 않을 경우, 방향 전환
                #     for num in alive_items:
                #         d = items[num][2]
                #         nd = change_d[board[r][c]][d]
                #         new_items[num] = (r,c,nd)

    return escape, new_items
# ===============================================
# 메인 로직
# ===============================================
def main():
    boards, origin_items = input_data()
    # if DEBUG: print()

    answer = 0
    for board in boards:
        escape = 0
        items = {i:v for i,v in origin_items.items()}
        if DEBUG: print()

        # ====================
        # 구슬 이동
        # ====================
        while items:
            new_escape, new_items = move_items(board, items)
            items = new_items
            escape += new_escape
            if DEBUG: print()

        answer = max(answer, escape)

    print(answer)

    # open tc 1 디버깅 (7m24s)
    # 바(1,2)가 있으면 진입 방향에 따라 충돌 여부가 달라질거라고 생각해서 풀었는데 아니었음

main()