'''
알록달록 테트리스 | 모의고사 3회 - 2번
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4803/curated-cards/mock-colorful-tetris/description

총 소요 시간: 3h 34m 28s
'''


# 문제 이해 51m 09s
# 문제 분석 18m 18s

# ==============================================
# 전역 및 클래스 5m 33s
# ==============================================
DEBUG = False
INF = float('inf')
N, M = map(int, input().split())
C, K = map(int, input().split())
MOVE = [(-1,0), (0,-1), (1,0), (0,1)]
TYPE = [None, (1,1), (2,1), (1,2)] # (h, w)
# board = [[0]*N for _ in range(N)]

blocks = {}

class Block:
    def __init__(self, num, color, t):
        self.num = num
        self.color = color
        self.type = t

# ==============================================
# 보조 함수
# ==============================================
def get_block_arrive(board, block, sc, er): # 20m 07s
    h, w = TYPE[block.type]

    nr = er + 1
    while nr < N:
        # 다음줄 확인
        # w만큼 모두 비어있을 경우 n 증가
        if all([board[nr][c] == 0 for c in range(sc, sc+w)]):
            nr += 1
        else: break

    return nr - 1

def down_block(board, block, er, sc): # 11m 43s
    h, w = TYPE[block.type]

    # 블록이 어디까지 내려 올 수 있는지 확인
    nxt_er = get_block_arrive(board, block, sc, er)

    if nxt_er - h + 1 < 0: return False, -1

    # 블록 하강
    sr = nxt_er - h + 1
    ec = sc + w - 1
    num = block.num
    # print()
    for r in range(sr, nxt_er+1):
        for c in range(sc, ec+1):
            board[r][c] = num

    return True, nxt_er

def all_gravity(board):
    new_board = [[0]*N for _ in range(N)]

    # 바닥부터, 블록 하강 순서 탐색
    down_list = []
    block_checked = set()
    for r in range(N-1, -1, -1):
        for c in range(N):
            if board[r][c] != 0 and board[r][c] not in block_checked:
                down_list.append((board[r][c], r, c))
                block_checked.add(board[r][c])

    for num, er, sc in down_list:
        down_block(new_board, blocks[num], er, sc)

    board = new_board
    return board

def check_line_full(board, r):
    for c in range(N):
        if board[r][c] == 0:
            return False
    return True

def get_score(line_block):
    score = 0
    color_set = set()

    for num in line_block:
        color = blocks[num].color
        if color not in color_set:
            score += 1
            color_set.add(color)
    return score

# 점수 연쇄 획득
def repeat_get_score(board): # 31m 28s
    # 줄 별 점검
    score = 0
    got = False
    for r in range(N):
        is_full = check_line_full(board, r)
        if is_full:
            # 점수 획득
            line_block = set(board[r])

            score += get_score(line_block)
            # 줄 비우기
            board[r] = [0]*N
            # 높이가 있을 경우 타입 변경, 그 외는 아이템에서 제거
            for num in line_block:
                if blocks[num].type == 2:
                    blocks[num].type = 1
                else:
                    del blocks[num]

            got = True
    # 전체 중력 적용
    if got:
        board = all_gravity(board)
        board, more = repeat_get_score(board)
        score += more
    return board, score


# 이러면안되는거아는데 설계잘못해서 각 블록의 시작 좌표 찾기...
def find_start_pos(board):
    start_pos = {}
    for r in range(N):
        for c in range(N):
            num = board[r][c]
            if num != 0 and num not in start_pos:
                start_pos[num] = (r, c)
    return start_pos

def add_block_in_board(board, block, sr, sc):
    h, w = TYPE[block.type]
    for r in range(sr, sr + h):
        for c in range(sc, sc + w):
            board[r][c] = block.num

def get_rainbow_d(r, c, rot):
    dist = [r, c, N-r-1, N-c-1]   # 현재 보드 기준 상,좌,하,우
    d = min(range(4), key=lambda a: (dist[(a+rot)%4], a))   # a: 실제 방향
    return (d+rot) % 4

def can_move(board, block, nr, nc):
    h, w = TYPE[block.type]

    for r in range(nr, nr+h):
        for c in range(nc, nc+w):
            if not (0 <= r < N and 0 <= c < N and board[r][c] in (0, block.num)):
                return False

    return True
def rainbow(board, rr, rc, rot):
    board[rr][rc] = 0

    move_set = set() # 십자 모양에 있는 블록 리스트
    for r in range(N):
        if board[r][rc] != 0: move_set.add(board[r][rc])
    for c in range(N):
        if board[rr][c] != 0: move_set.add(board[rr][c])

    # 이동 방향 정하기
    d = get_rainbow_d(rr, rc, rot)
    dr, dc = MOVE[d]

    fixed = set() # 고정된 목록

    # 블록 동시 이동(C회)
    for _ in range(C):
        start_pos = find_start_pos(board)
        # 이번 턴에 움직일 후보
        movers = {num for num in blocks if num in move_set and num not in fixed}

        # 안 움직이는 블록만 올린 보드로 막힘 판정, 새로 막힌 게 없을 때까지 반복
        while True:
            stay = [[0]*N for _ in range(N)]
            for num, block in blocks.items():
                if num not in movers:
                    sr, sc = start_pos[num]
                    add_block_in_board(stay, block, sr, sc)
            stuck = set()
            for num in movers:
                sr, sc = start_pos[num]
                if not can_move(stay, blocks[num], sr+dr, sc+dc):
                    stuck.add(num)
            if not stuck: break
            movers -= stuck
            fixed |= stuck

        # 실제 이동 반영
        new_board = [[0]*N for _ in range(N)]
        for num, block in blocks.items():
            sr, sc = start_pos[num]
            if num in movers:
                sr, sc = sr+dr, sc+dc
            add_block_in_board(new_board, block, sr, sc)
        board = new_board

    board = all_gravity(board)
    return board


# ==============================================
# 메인 로직
# ==============================================
def main():
    board = [[0]*N for _ in range(N)]
    score = 0
    for num in range(1, M+1):
        # 블록 놓기
        t, sc, color = map(int, input().split())
        sc -= 1
        new_block = Block(num, color, t)
        downed, nxt_er = down_block(board, new_block, -1, sc)
        if downed:
            # 무지개 블록일 경우
            if color == 0:
                rot = (num - 1) // K % 4
                board = rainbow(board, nxt_er, sc, rot)
            else: blocks[num] = new_block

        # if DEBUG: print()


        # 점수 연쇄 획득 (블록 하강한 경우에만)
        if downed:
            board, new_score = repeat_get_score(board)
            score += new_score
        # if DEBUG: print()

        # 중력 회전 및 중력 적용 21m 42s
        if num%K == 0:
            new_board = [list(line) for line in zip(*board)]
            board = new_board[::-1]
            # 타입 변경
            for block in blocks.values():
                if block.type == 2: block.type =3
                elif block.type == 3: block.type = 2

            board = all_gravity(board)
            board, new_score = repeat_get_score(board)
            score += new_score
        # if DEBUG: print()

    print(score)

main()