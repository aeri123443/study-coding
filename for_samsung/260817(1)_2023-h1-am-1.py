'''
포탑 부수기: 2023 상반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/destroy-the-turret/

문제 분석: 23m 39s
코드 작성: 1h 23m 18s
1차 디버깅: 15m 34s
  - [TC3 Fail] 1. info 오타: (a, -recent, r+c, c, (r,c)) -> (a, -recent, -(r+c), -c, (r,c)) 수정
               2. 시작 좌표를 영향 포탑 set에서 제대로 빼주는 로직을 추가
2차 디버깅: 9m 47s
  - [TC5 Fail] (gemini 도움) 인접할 경우 레이저 공격에서 []를 반환하는데, 이때 '공격할 수 없음'으로 판정되어 포탄 공격 진행
               -> 공격 여부와 영향을 받은 포탑을 함께 반환
총 소요 시간: 2h 12m 20s
'''
from collections import deque

# ===============================
# 전역 / 클래스
# ===============================
N, M, K = -1, -1, -1
INF = float('inf')
MOVE = [(0,+1), (+1,0), (0,-1), (-1,0), (-1,+1), (+1,+1), (+1,-1), (-1,-1)] # 우 하 좌 상 우상 우하 좌하 좌상

board = [] # 디버깅 편의상 그냥 공격력 담음
items = {} # 남은 포탑들. (r,c) : class

class Item:
    def __init__(self, r, c, a):
        self.key = (r, c)
        self.a = a          # 공격력
        self.recent = 0     # 최근 공격

# ===============================
# 보조 함수
# ===============================

# 초기 데이터 입력
def input_data():
    global N, M, K

    N, M, K = map(int, input().split())

    for r in range(N):
        line = list(map(int, input().split()))
        for c, a in enumerate(line):
            if a > 0:
                items[(r,c)] = Item(r, c, a)

        board.append(line)

# 공격자 및 방어자 선정
# O(N)으로 충분히 가능하다고 판단, 우선순위큐를 사용하지 않고 min/max만 확인
def choose_items():
    attack = (INF, INF, INF, INF, INF) # 최소 공격력, 최대 최근공격, 최대 행열합, 최대 열, key
    defense = (-INF, -INF, -INF, -INF, -INF)  # 최대 공격력, 최소 최근공격, 최소 행열합, 최소 열, key

    for r in range(N):
        for c in range(M):
            if board[r][c] <= 0 : continue

            item = items[(r,c)]
            a, recent = item.a, item.recent
            info = (a, -recent, -(r+c), -c, (r,c))

            attack = min(attack, info)
            defense = max(defense, info)

    return attack[4], defense[4]

# 보정이 더해진 다음 경로를 반환
def get_next_pos(cr, cc, d):
    dr, dc = MOVE[d]
    nr, nc = cr+dr, cc+dc

    if not (0<=nr<N):
        if nr == -1: nr = N - 1
        else: nr = 0

    if not (0<=nc<M):
        if nc == -1: nc = M - 1
        else: nc = 0

    return nr, nc

# 역 bfs -> 방문 배열 반환
def rev_bfs(sr, sc, er, ec):
    q = deque([(er, ec)])
    visited = [[-1] * M for _ in range(N)]
    visited[er][ec] = 0

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = get_next_pos(cr, cc, d)

            if visited[nr][nc] == -1 and board[nr][nc] > 0:
                visited[nr][nc] = visited[cr][cc] + 1

                if (nr, nc) == (sr, sc):
                    return visited

                q.append((nr, nc))

    return visited

# 레이저 공격, 경로(영향 받는 피해 포탑) 반환
def laser_attack(ak, dk):
    sr, sc = ak
    er, ec = dk

    # 역 bfs로 최단 경로 찾고
    visited = rev_bfs(sr, sc, er, ec)
    cnt = visited[sr][sc]
    if cnt == -1:
        return False, []

    # 우선순위 이동하며 경로 담음
    route = set()
    cr, cc = sr, sc

    while cnt > 0:
        for d in range(4):
            nr, nc = get_next_pos(cr, cc, d)
            if cnt-1 == visited[nr][nc]:
                cr, cc = nr, nc
                cnt -= 1

                # 피해를 받는 포탑만 기록
                if board[nr][nc] > 0:
                    route.add((nr, nc))
                break

    # 마지막은 도착지이므로 뺀다
    route.remove((er, ec))
    return True, route

# 포탄 공격, 영향 받는 주변 포탑 반환
def bomb_attack(dk):
    sr, sc = dk
    near_items = set()

    for d in range(8):
        nr, nc = get_next_pos(sr, sc, d)
        if board[nr][nc] > 0:
            near_items.add((nr, nc))

    return near_items

# 공격력 업데이트, 파괴 검사 밑 업데이트
# da: 공격력 변화량
def update_a_val(r, c, da):
    item_key = (r,c)
    item = items[item_key]

    new_val = board[r][c] + da
    item.a = new_val
    board[r][c] = new_val

    # 공격력이 0 이하가 되면 파괴됨
    if da < 0 and item.a <= 0:
        del items[item_key]

# ===============================
# 메인 로직
# ===============================
def main():

    # 초기 데이터 입력
    input_data()
    # print()

    # K회 반복, 포탑이 1개 이하면 조기 종료
    for k in range(1, K+1):
        if len(items) <= 1: break

        # 공격자 및 방어자 선정
        attack_key, defense_key = choose_items()
        # print()

        # 레이저 공격, 경로 반환
        laser_attacked, effected_items = laser_attack(attack_key, defense_key)
        # 레이저 공격이 안 되면 포탄 공격
        if not laser_attacked:
            effected_items = bomb_attack(defense_key)

        ar, ac = attack_key
        if (ar, ac) in effected_items:
            effected_items.remove((ar,ac))

        # print()

        # 공격자 공격력 및 최근 공격 업데이트

        a_item = items[attack_key]
        a_item.recent = k

        update_a_val(ar, ac, N + M)

        # 타겟 공격
        dr, dc = defense_key
        update_a_val(dr, dc, -a_item.a)

        # 주변 공격
        half_a_val = a_item.a // 2
        for r, c in effected_items:
            update_a_val(r, c, -half_a_val)

        # print()

        # 포탑 정비
        for item in items.values():
            r, c = item.key

            # 공격받지 않았으며, 공격자 본인이 아닐 경우 공격력 1 증가
            if (r, c) not in ((ar, ac), (dr, dc)) and (r, c) not in effected_items:
                update_a_val(r, c, 1)

        # print()

    # 남은 포탑 중 가장 높은 공격력 출력
    max_a = -1
    for item_key in items:
        r, c = item_key
        max_a = max(max_a, board[r][c])
    print(max_a)

main()