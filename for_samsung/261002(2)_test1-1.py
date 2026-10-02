'''
모의고사 1회 - 1번
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4801/curated-cards/mock-special-bucket/description

문제 분석: 37m 19s
코드 1차 작성: 1h 6m 34s
1차 디버깅, 클로드 도움: 20m 56s

총 소요 시간: 2h 4m 51s
'''
from collections import deque

# ==========================================
# 전역 및 클래스
# ==========================================
DEBUG = False
INF = float('inf')
MOVE = [(0,+1), (1,0), (0,-1), (-1,0)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

# ==========================================
# 보조 함수
# ==========================================
def get_person_next_pos():
    sr, sc, d = map(int, input().split())
    sr, sc = sr - 1, sc - 1

    visited = {(sr, sc)}
    q = deque([(sr, sc)])
    max_info = (board[sr][sc], -sr, -sc) # 해산물 최대, r 최소, c최소

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if 0<=nr<N and 0<=nc<M and not (nr, nc) in visited and (abs(sr-nr)+abs(sc-nc)) <= d:
                max_info = max(max_info, (board[nr][nc], -nr, -nc))
                q.append((nr,nc))
                visited.add((nr, nc))

    return max_info[0], -max_info[1], -max_info[2]

def get_path(r1, c1, r2, c2, a):
    path = [(r1, c1, board[r1][c1])]
    visited = {(r1,c1)}

    cr, cc = r1, c1
    d = 0
    while True:
        dr, dc = MOVE[d]
        nr, nc = cr+dr, cc+dc
        if r1<=nr<=r2 and c1<=nc<=c2 and not (nr,nc) in visited:
            path.append((nr, nc, board[nr][nc]))
            visited.add((nr, nc))
            cr, cc = nr, nc
        else:
            d = (d+1)%4

        if (nr, nc) == (r1, c1): # 시작점으로 돌아오면 종료
            break

    if a > 0: # 시계
        tmp = path[-a:]
        path = tmp + path
    else: # 반시계
        tmp = path[:-a]
        path.extend(tmp)

    return path

def rotate_board(path, path_len, a):
    if a > 0:
        i = 0
    else:
        i = -a

    for _ in range(path_len):
        cr, cc, cur = path[i]
        nr, nc, nxt = path[i+a]
        board[nr][nc] = cur
        i += 1
# ==========================================
# 메인 로직
# ==========================================
def main():
    answer = []
    for _ in range(Q):
        # ============================
        # 1. 해산물 채취 : 전역 포함 21m 35s
        # ============================

        # 해산물 위치 반환
        item_cnt, npr, npc = get_person_next_pos()
        remain = item_cnt // 2
        answer.append(item_cnt - remain)
        board[npr][npc] = remain

        if DEBUG: print()

        # ============================
        # 2. 해류 발생 44m 59s
        # ============================
        r1, c1, r2, c2, a = map(int, input().split())
        r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
        path_len = (r2-r1)*2 + (c2-c1)*2

        if a > 0:
            a %= path_len
        else:
            a = - (abs(a) % path_len)


        path = get_path(r1, c1, r2, c2, a)
        # path = get_path(0, 0, 1, 1, -1)
        if DEBUG: print()

        rotate_board(path, path_len, a)
        if DEBUG: print()
        # print(item_cnt - remain)
    print('\n'.join(map(str, answer)))

main()
