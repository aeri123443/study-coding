'''
예술성: 2022 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/artistry/solutions

문제 분석: 15m 59s
코드 1차 작성: 1h 9m 2s

all tc passed.
총 소요 시간: 1h 25m 2s
'''
from collections import defaultdict, deque

# ===========================================
# 전역 선언
# ===========================================
DEBUG = False
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MOVE = [(0,1), (1,0), (-1,0), (0,-1)]

# ===========================================
# 보조 함수
# ===========================================

def grouping(visited, g_num, sr, sc):
    color = board[sr][sc]
    g_cnt = 1
    g_pos = [(sr,sc)]

    q = deque([(sr, sc)])
    visited[sr][sc] = g_num

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<N and board[nr][nc] == color and visited[nr][nc] == 0:
                q.append((nr, nc))
                g_cnt += 1
                visited[nr][nc] = g_num
                g_pos.append((nr,nc))

    return g_cnt, color, g_pos

def get_wall(g_board, g_num, g_pos):
    wall = defaultdict(int)

    for r, c in g_pos:
        for dr, dc in MOVE:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and g_board[nr][nc] != g_num:
                wall[g_board[nr][nc]] += 1

    return wall

def cross_rotate(new_board, cross_pos):
    for r, c in cross_pos:
        new_board[N-c-1][r] = board[r][c]

def area_rotate(mid, new_board, sr, sc, area):
    tmp = [[0]*mid for _ in range(mid)]
    for ar, ac in area:
        rr, rc = ar-sr, ac-sc
        tmp[rr][rc] = board[ar][ac]

    tmp_rotated = [x[::-1] for x in zip(*tmp)]
    for ar, ac in area:
        rr, rc = ar-sr, ac-sc
        new_board[ar][ac] = tmp_rotated[rr][rc]

# ===========================================
# 메인 로직
# ===========================================
def main():
    global board

    answer = 0

    # 영역 나누기
    mid = N//2

    cross_pos = []
    for r in range(N): cross_pos.append((r, mid))
    for c in range(N): cross_pos.append((mid, c))

    a1 = [(r,c) for r in range(mid) for c in range(mid)]
    a2 = [(r,c) for r in range(mid) for c in range(mid+1, N)]
    a3 = [(r,c) for r in range(mid+1, N) for c in range(mid+1, N)]
    a4 = [(r,c) for r in range(mid+1, N) for c in range(mid)]
    area_4_pos = {
        (0,0): a1,
        (0,mid+1): a2,
        (mid+1,mid+1): a3,
        (mid+1, 0): a4
    }

    # 4회 반복
    for rot in range(4):
        visited = [[0]*N for _ in range(N)]
        walls = {}
        groups = {}
        g_num = 1

        # 그룹화
        for r in range(N):
            for c in range(N):
                if visited[r][c] == 0:
                    g_cnt, g_color, g_pos = grouping(visited, g_num, r, c)
                    groups[g_num] = (g_cnt, g_color, g_pos)
                    g_num += 1

        # 맞닿은 변 정보 업데이트
        for g in groups.keys():
            g_cnt, g_color, g_pos = groups[g]
            wall = get_wall(visited, g, g_pos)
            walls[g] = wall
        if DEBUG: print()

        total = 0
        # 조화 점수 계산
        for a in walls.keys():
            a_cnt, a_color, _ = groups[a]
            for b, w in walls[a].items():
                b_cnt, b_color, _ = groups[b]
                combi = (a_cnt+b_cnt) * a_color * b_color * w
                total += combi

        # 예술 점수 계산
        answer += total//2
        if DEBUG: print()

        new_board = [[0]*N for _ in range(N)]
        # 십자 회전
        cross_rotate(new_board, cross_pos)
        # 4영역 회전
        for (sr,sc), area in area_4_pos.items():
            area_rotate(mid, new_board, sr, sc, area)
        if DEBUG: print()

        board = new_board
    print(answer)
main()