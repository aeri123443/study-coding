'''
택배 하차: 2025 하반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description

문제 분석: 10m 36s
1차 코드 작성: 1h 18m 46s
    - [시간 소요] 처음엔 하강 후보들을 큐에 담아 반환하려고 했는데, 코딩하다보니 '단순히 큐에 담고 빼기만 하면 중력 하강에서 오류가 없을지' 의문이 생김
      -> 이에 반례 케이스 찾아보고, 반례 발견 후 heapq로 반환하는 방향으로 설계를 다시 함.
최종 디버깅: 0m 0s
총 소요 시간: 1h 29m 22s
'''

from collections import deque, defaultdict
import heapq

# =================================
# 전역 및 클래스
# =================================
# DEBUG = False
N, M = -1, -1
items = {}
board = []

class Item:
    def __init__(self, num, sc, w, h):
        self.num = num
        self.sr = -1
        self.sc = sc
        self.w = w
        self.h = h

    # num, sr, sc, w, h
    def get_info(self):
        return self.num, self.sr, self.sc, self.w, self.h

# =================================
# 보조 함수
# =================================

# 중력 하강: 중력으로 내려갔을 때 최종 sr 반환
def gravity(item):
    num, sr, sc, w, h = item.get_info()
    er, ec = sr+h-1, sc+w-1

    # 그럴리없지만 이미 바닥에 있으면 현재 값 반환
    if er == N-1: return sr

    # 다음 줄이 범위 내, 장애물 없음
    line = er+1
    while line < N:
        if all([board[line][c]==0 for c in range(sc, ec+1)]):
            line += 1
        else: break

    return line-h


# 바뀐 상태를 반영하여 보드에 기입
def add_in_board(item):
    num, sr, sc, w, h = item.get_info()

    for r in range(sr, sr+h):
        for c in range(sc, sc+w):
            board[r][c] = num

def remove_from_board(item):
    num, sr, sc, w, h = item.get_info()

    for r in range(sr, sr+h):
        for c in range(sc, sc+w):
            if board[r][c] == num:
                board[r][c] = 0

# 하차할 번호를 반환
def get_out_item_num(is_left=True):
    side = defaultdict(int)

    for r in range(N):
        if is_left:
            for c in range(N):
                if board[r][c]!=0:
                    side[board[r][c]] += 1
                    break
        else: # right
            for c in range(N-1, -1, -1):
                if board[r][c]!=0:
                    side[board[r][c]] += 1
                    break

    out_item_num = float('inf')
    for i, v in side.items():
        if v != items[i].h: continue
        if out_item_num > i: out_item_num = i

    return out_item_num


# 하차 번호 기준, 하강 후보들을 우선순위큐에 담아 반환
def get_down_candidate(start_num):
    candi_set = set()
    candi_hq = [] # er 큰 순서 (밑에있는 순서)

    q = deque([start_num])

    while q:
        num = q.popleft()
        item = items[num]
        sr, sc, w = item.sr, item.sc, item.w

        # 맨 위에 있으면 위에 있는 택배는 없음
        if sr == 0 : continue

        r = sr-1
        # 시작줄 기준, 윗줄에 뭐라도 있으면
        for c in range(sc, sc+w):
            new_num = board[r][c]
            if new_num != 0 and new_num not in candi_set:
                q.append( new_num )
                candi_set.add(new_num)

                new_item = items[new_num]
                heapq.heappush(candi_hq, (-(new_item.sr + new_item.h - 1), new_num))

    return candi_hq

def out_item(d):
    # 하차할 번호를 반환
    if d == 'left':
        out_num = get_out_item_num()
    else:
        out_num = get_out_item_num(False)

    # 하차 번호 기준, 하강 후보들을 큐에 담아 반환
    candi_hq = get_down_candidate(out_num)

    # 하차
    remove_from_board(items[out_num])
    del items[out_num]

    # 하강 큐 순서대로 하강 진행, 하강하지 않을 경우 그냥 둠
    while candi_hq:
        _, down_num = heapq.heappop(candi_hq)
        down_item = items[down_num]
        down_sr = gravity(down_item)
        if down_sr != down_item.sr:
            remove_from_board(down_item)
            down_item.sr = down_sr
            add_in_board(down_item)

    return out_num
# =================================
# 메인 로직
# =================================
def main():
    global N, M, board

    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]

    # ======================
    # 1. 택배 투입
    # ======================
    for _ in range(M):
        k, h, w, c = map(int, input().split())
        c -= 1

        new_item = Item(k, c, w, h)
        items[k] = new_item

        # 중력 하강: 중력으로 내려갔을 때 최종 sr 반환
        sr = gravity(new_item)
        new_item.sr = sr

        # 바뀐 상태를 반영하여 보드에 기입
        add_in_board(new_item)

    # if DEBUG: print()

    answer = []
    while items:
        # ======================
        # 2. 택배 하차(좌)
        # ======================
        out_num = out_item('left')
        answer.append(out_num)

        if not items: break

        # ======================
        # 2. 택배 하차(우)
        # ======================
        out_num = out_item('right')
        answer.append(out_num)

        # if DEBUG: print()
    print('\n'.join(map(str, answer)))
main()