'''
미생물 연구: 2025 상반기 오후 1번

https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research

문제 분석: 24m 06s
1차 코드 작성: 1h 18m 36s
    - [시간 소요] get_neighbor_set에서 오른쪽, 아래쪽으로만 탐색하면 된다고 생각했다가, 뭔가 복잡해지는것같아서 익숙한 deque로 바꿈
    - [TC3 fail] if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and new_board[nr][nc]!=0 으로 미생물이 없는 칸에 bfs가 닿지 못함
                 근데 2차 코드 작성에서 visited때문에 인접한 미생물을 찾지 못한 줄 알고 visited를 빼버림
2차 코드 작성: 8m 25s
    - [TC19 error] get_neighbor_set에서 (0,0)이 0이고 다음 좌표에 미생물이 있을 때도 (0, num)과 같은 형태로 담김 ->
                score += (len(items[a].relatives)*len(items[b].relatives)) 에서 items[0] key error 발생
                -> 3차 코드 작성에서 new num, num이 0이 아닐 때 업데이트 하는 방어코드를 추가
      error를 고쳤지만 해당 테케 정답과 일치하지 않음
      -> 클로드 도움, visited 다시 추가, deque를 빼고 오른쪽과 아래로만 탐색하도록 수정

3차 코드 작성: 17m 01s

총 소요 시간: 2h 08m 10s
'''
from collections import deque, defaultdict
import heapq

# ====================================
# 전역 및 클래스
# ====================================
DEBUG = False
INF = float('inf')
N, Q = -1, -1
MOVE = [(1,0), (-1,0), (0,1), (0,-1)]

items = {}
board = []

class Item:
    def __init__(self, num, r, c, relatives):
        self.num = num
        self.standard = (r, c)
        self.relatives = relatives

# ====================================
# 보조 함수
# ====================================

def check_area(r, c, visited):
    target_num = board[r][c]
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and board[nr][nc] == target_num:
                visited[nr][nc] = True
                q.append((nr,nc))


def update_item(num):
    min_r = INF
    min_c = INF
    absolutes = []

    item = items[num]
    sr, sc = item.standard

    # 좌측 상단 기준, 절대좌표 탐색
    for rr, rc in item.relatives:
        ar, ac = rr+sr, rc+sc

        # 절대좌표 리스트, 최소 r,c 업데이트
        if board[ar][ac] == num:
            absolutes.append((ar,ac))
            min_r = min(min_r, ar)
            min_c = min(min_c, ac)

    # 상대좌표 업데이트
    relatives = [(ar-min_r, ac-min_c) for ar, ac in absolutes]

    item.standard = (min_r,min_c)
    item.relatives = relatives

def move_item(new_board, num):
    item = items[num]
    for sc in range(N):
        for sr in range(N):
            # 모든 절대좌표에 대해, 범위 내, 비어있는 칸
            if all([(0 <= rr + sr < N and 0 <= rc + sc < N and new_board[rr + sr][rc + sc] == 0) for rr, rc in
                    item.relatives]):
                for rr, rc in item.relatives:
                    new_board[rr + sr][rc + sc] = num
                    item.standard = (sr, sc)
                return True
    return False

def get_neighbor_set(new_board):
    n_set = set()
    # q = deque([(0,0)])
    # visited = [[False]*N for _ in range(N)]
    # visited[0][0] = True

    for cr in range(N):
        for cc in range(N):
            num = new_board[cr][cc]
            for dr, dc in [(0,1), (1,0)]:
                nr, nc = dr + cr, dc + cc
                if 0 <= nr < N and 0 <= nc < N:
                    new_num = new_board[nr][nc]

                    if new_num != num and num != 0 and new_num != 0:
                        n_set.add((min(num, new_num), max(num, new_num)))

    # while q:
    #     # cr, cc = q.popleft()
    #     num = new_board[cr][cc]
    #
    #     for dr, dc in MOVE:
    #         nr, nc = dr+cr, dc+cc
    #         # if 0<=nr<N and 0<=nc<N and new_board[nr][nc]!=0:
    #         if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
    #             visited[nr][nc] = True
    #             q.append((nr,nc))
    #
    #             new_num = new_board[nr][nc]
    #
    #             if new_num != num and num!=0 and new_num!=0:
    #                 n_set.add((min(num, new_num), max(num, new_num)))

    return n_set
# ====================================
# 메인 로직
# ====================================
def main():
    global N, Q, board
    answer = []

    N, Q = map(int, input().split())
    board = [[0]*N for _ in range(N)]

    for t in range(1, Q+1):
        # ==============
        # 1. 미생물 투입
        # ==============

        # 미생물 추가
        x1, y1, x2, y2 = map(int, input().split())
        tmp_rel = []
        for r in range(y1, y2):
            for c in range(x1, x2):
                board[r][c] = t
                tmp_rel.append((r-y1,c-x1))
        new_item = Item(t, y1, x1, tmp_rel)
        items[t] = new_item

        if DEBUG: print()

        # 영역 수 체크
        area_counter = defaultdict(int)
        visited = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if not visited[r][c] and board[r][c]!=0:
                    check_area(r, c, visited)
                    area_counter[board[r][c]] += 1


        # 영역 수 1이면, 좌측상단 및 상대위치 업데이트 후, heapq에 추가
        del_items = []
        hq = []
        for item in items.values():
            num = item.num
            if num not in area_counter:
                del_items.append(num)
            elif area_counter[num] > 1:
                del_items.append(num)
            else:
                update_item(num)
                heapq.heappush(hq, (-len(item.relatives), num))

        for num in del_items:
            del items[num]

        if DEBUG: print()

        # ==============
        # 2. 배양 용기 이동
        # ==============

        new_board = [[0]*N for _ in range(N)]
        while hq:
            _, num = heapq.heappop(hq)

            moved = move_item(new_board, num)

            if not moved:
                del items[num]

        if DEBUG: print()

        # ==============
        # 3. 실험 결과 기록
        # ==============

        # 인접 무리 set
        neighbor_set = get_neighbor_set(new_board)

        score = 0
        for a, b in neighbor_set:
            score += (len(items[a].relatives)*len(items[b].relatives))

        answer.append(score)

        if DEBUG: print()

        board = new_board

    print('\n'.join(map(str, answer)))

main()