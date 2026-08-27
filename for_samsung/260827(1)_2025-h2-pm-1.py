'''
AI 로봇청소기: 2025 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ai-robot

문제 분석: 14m 25s
코드 작성: 1h 21m 04s
  - [시간 소요] bfs에서 자기 자신의 위치에 먼지가 있을경우 바로 리턴하는 코드를 작성하지 않음
최종 디버깅: 0m 0s

총 소요 시간: 1h 35m 30s
'''

from collections import deque

# ==================================
# 전역 선언
# ==================================

N, K, L = -1, -1, -1
INF = float('inf')
MOVE = [(0,+1), (+1,0), (0,-1), (-1,0)]

dust_board = []
item_board = [] # 청소기 위치
items = [] # (r,c)

# ==================================
# 보조 함수
# ==================================
def input_data():
    global N, K, L, dust_board, item_board

    N, K, L = map(int, input().split())
    dust_board = [list(map(int, input(). split())) for _ in range(N)]
    item_board = [[-1]*N for _ in range(N)]

    # 청소기
    for i in range(K):
        r, c = map(lambda x: int(x)-1, input().split())
        item_board[r][c] = i
        items.append((r,c))

def is_range(r, c):
    return 0<=r<N and 0<=c<N

def get_next_pos(idx):
    sr, sc = items[idx]

    if dust_board[sr][sc] > 0:
        return 0, sr, sc

    q = deque([(sr, sc)])
    visited = [[-1]*N for _ in range(N)]
    visited[sr][sc] = 0

    next_info = (INF, INF, INF)  # 이동 거리 최소, r 최소, c 최소

    while q:
        cr, cc = q.popleft()

        if next_info[0] < visited[cr][cc]:
            continue

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            if is_range(nr, nc) and visited[nr][nc]==-1 and dust_board[nr][nc] != -1 and item_board[nr][nc] in (-1, idx):
                new_cnt = visited[cr][cc] + 1
                if dust_board[nr][nc]==0:
                    q.append((nr,nc))
                    visited[nr][nc] = new_cnt
                else:
                    next_info = min(next_info, (new_cnt, nr, nc))

    return next_info

# 청소 방향 선정
def get_clear_dir(idx):
    sr, sc = items[idx]

    dis_info = (-INF, -INF, []) # 먼지량 최대(자기자신 제외), 방향 최소(-), 위치 정보
    for d in range(4):
        total = 0
        route =[]
        for dd in range(4):
            if (dd-2)%4 == d: continue

            dr, dc = MOVE[dd]
            nr, nc = dr+sr, dc+sc
            if is_range(nr, nc) and dust_board[nr][nc] > 0:
                total += min(20, dust_board[nr][nc])
                route.append((nr, nc, min(20, dust_board[nr][nc])))
            # print()
        dis_info = max(dis_info, (total, -d, route))

    return [*dis_info[2], (sr, sc, min(20, dust_board[sr][sc]))]

# 4. 먼지 확산
def extend_dust():
    sum_board = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if dust_board[r][c] == 0:
                total_four = 0

                for dr, dc in MOVE:
                    nr, nc = dr+r, dc+c
                    if is_range(nr, nc) and dust_board[nr][nc] > 0:
                        total_four += dust_board[nr][nc]

                sum_board[r][c] = total_four // 10

    for r in range(N):
        for c in range(N):
            dust_board[r][c] += sum_board[r][c]
# ==================================
# 메인 로직
# ==================================
def main():
    input_data()
    # print()

    ans = []
    for _ in range(L):
        # 1. 청소기 이동
        for idx in range(K):
            # 어디로 이동할지?
            dis, nr, nc = get_next_pos(idx)

            # 이동 가능하면 이동!
            if dis == INF: continue
            cr, cc = items[idx]
            item_board[cr][cc] = -1
            item_board[nr][nc] = idx
            items[idx] = (nr,nc)

        # print()

        # 2. 청소
        for idx in range(K):
            # 청소 방향 선정
            clear_route = get_clear_dir(idx)

            # 청소
            for nr, nc, amount in clear_route:
                dust_board[nr][nc] -= amount

        # print()

        # 3. 먼지 축적
        for r in range(N):
            for c in range(N):
                if dust_board[r][c] > 0 : dust_board[r][c] += 5

        # 4. 먼지 확산
        extend_dust()
        # print()

        # 5. 먼지량 합산
        total_dust = 0
        for r in range(N):
            for c in range(N):
                if dust_board[r][c] > 0:
                    total_dust += dust_board[r][c]
        ans.append(total_dust)
        # print()

    print('\n'.join(map(str, ans)))

main()