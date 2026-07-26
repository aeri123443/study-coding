'''
택배 하차: 2025 하반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description

1h 22m 23s
오래 걸린 이유: items[ni].r가 변화되면서 큐에 담을 때 상태가 꼬이고 연쇄 적용이 되지 않음 -> 큐에 이전 r을 담음
'''

from collections import deque, defaultdict

###########################
#### 전역 변수 및 클래스
###########################
INF = float('inf')

N, M = -1, -1
items = {} # {num: Item}
board = []

class Item:
    def __init__(self, num, h, w, c):
        self.num = num
        self.r = -1
        self.c = c
        self.h = h
        self.w = w

###########################
#### 보조 함수
###########################
# num, sr, sc, w, h = item.num, item.r, item.c, item.w, item.h
# er, ec = sr+h-1, sc+w-1

# 보드에서 아이템 제거
def remove_from_board(item):
    sr, sc, w, h = item.r, item.c, item.w, item.h

    for r in range(sr, sr+h):
        for c in range(sc, sc+w):
            board[r][c] = 0

# 중력 하강
def gravity(item):
    num, sr, sc, w, h = item.num, item.r, item.c, item.w, item.h
    er, ec = sr+h-1, sc+w-1

    # 어디까지 하강할 수 있는지를 확인
    nr = er
    while nr < N-1:
        nr += 1
        flag = False
        for c in range(sc, sc+w):
            if board[nr][c] != 0:
                flag = True
                break

        if flag:
            nr -= 1
            break
    # print()

    # 하강
    # 초기 투입시엔 보드에서 지우지 않음
    if sr != -1: remove_from_board(item)
    # 위치 업데이트
    sr = nr - h + 1
    item.r = sr
    for r in range(sr, sr+h):
        for c in range(sc, sc+w):
            board[r][c] = num

# 양측 제거 후보 탐색
# 좌측: l, 우측: r
def find_side_out_item(s):
    side_counter = defaultdict(int)

    if s=='left': # left
        sc, ec, dc = 0, N, +1
    else: # right
        sc, ec, dc = N-1, -1, -1

    for r in range(N):
        for c in range(sc, ec, dc):
            if board[r][c] != 0:
                side_counter[ board[r][c] ] += 1
                break

    # print()
    min_out_item = INF

    for num, cnt in side_counter.items():
        item = items[num]
        if cnt == item.h:
            min_out_item = min(min_out_item, num)

    return min_out_item

# 아이템 하차
def out_item(answer, item):
    # 해당 아이템을 제거
    remove_from_board(item)
    answer.append(str(item.num))

    # 제거 대상 아이템 기준, 새롭게 하강할 수 있는 아이템들이 있을지 확인
    q = deque([(item.num, item.r)]) # 아이템 넘버 num, 중력 적용 전위치 sr

    while q:
        cur_num, cur_r = q.popleft()

        # 방어코드: 이미 제거되었을 경우 패스 (처음 제거된 아이템은 논외)
        if cur_num not in items and cur_num!=item.num: continue
        cur_item = items[cur_num]
        sr = cur_r
        sc, w = cur_item.c, cur_item.w

        # r 시작점 기준, 바로 위에 다른 아이템이 있는지 확인
        if sr == 0: continue # 맨위에 있는 아이템이라면 탐색할 필요 없음

        next_items = set()
        r = sr-1
        for c in range(sc, sc+w):
            if board[r][c] > 0:
                next_items.add(board[r][c])

        # 해당 아이템들에 대해 연쇄적으로 중력 적용
        for ni in next_items:
            q.append((ni, items[ni].r))
            gravity(items[ni])
        # print()
    del items[item.num]

###########################
#### 메인 로직
###########################
def main():
    global N, M, items, board

    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    answer = []

    # 1단계: 택배 투입
    for _ in range(M):
        k, h, w, c = map(int, input().split())
        c -= 1
        new_item = Item(k, h, w, c)
        items[k] = new_item

        gravity(new_item)
    # print()

    while items:
        # 좌측 하강
        out_item_num = find_side_out_item('left')
        out_item(answer, items[out_item_num])
        # print()

        if not items: break

        # 우측 하강
        out_item_num = find_side_out_item('right')
        out_item(answer, items[out_item_num])
        # print()

    # 정답 출력
    print('\n'.join(answer))

if __name__ == '__main__':
    main()