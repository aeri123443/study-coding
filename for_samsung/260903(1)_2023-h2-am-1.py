'''
왕실의 기사 대결: 2023 하반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/royal-knight-duel

문제 분석: 08m 06s
1차 코드 작성: 1h 11m 50s
최종 디버깅: 0m 0s

총 소요 시간: 1h 19m 58s
'''
from collections import deque

# ===================================
# 전역 및 클래스
# ===================================
DEBUG = False

L, N, Q = -1, -1, -1
MOVE = [(-1,0), (0,+1), (+1,0), (0,-1)]

map_board = []
knights_board = []
knights = []

class Knight:
    def __init__(self, num, r, c, h, w, k):
        self.num = num
        self.pos = (r, c)
        self.size = (h, w)
        self.k = k
        self.dam = 0

# ===================================
# 보조 함수
# ===================================
def init_data():
    global L, N, Q, map_board, knights_board, knights

    L, N, Q = map(int, input().split())

    map_board = [list(map(int, input().split())) for _ in range(L)]
    knights_board = [[0]*L for _ in range(L)]
    knights = [None] * (N+1)

    for num in range(1, N+1):
        r, c, h, w, k = map(int, input().split())
        r, c = r-1, c-1

        for nr in range(r, r+h):
            for nc in range(c, c+w):
                knights_board[nr][nc] = num

        new_knight = Knight(num, r, c, h, w, k)
        knights[num] = new_knight


# 연쇄 이동 및 가능 여부 반환
def check_move(q_num, q_d):
    dr, dc = MOVE[q_d]
    moved_knights = {q_num}
    q = deque([q_num])

    while q:
        cur_num = q.popleft()

        ck = knights[cur_num]
        (sr, sc), (h, w) = ck.pos, ck.size
        er, ec = sr+h-1, sc+w-1

        # 위쪽 이동
        if q_d == 0:
            check_pos = { (sr+dr, nc) for nc in range(sc, ec+1)}
        # 오른쪽 이동
        elif q_d == 1:
            check_pos = { (nr, ec+dc) for nr in range(sr, er+1)}
        # 아래 이동
        elif q_d == 2:
            check_pos = { (er+dr, nc) for nc in range(sc, ec+1)}
        # 왼쪽 이동
        else:
            check_pos = { (nr, sc+dc) for nr in range(sr, er+1)}

        for nr, nc in check_pos:
            # 벽이 있으면 이동할 수 없음
            if not(0<=nr<L and 0<=nc<L) or map_board[nr][nc] == 2:
                return False, set()

            if knights_board[nr][nc]>0 and knights_board[nr][nc] not in moved_knights:

                moved_knights.add(knights_board[nr][nc])
                q.append(knights_board[nr][nc])

    return True, moved_knights

def remove_knight_in_board(k_num):
    k = knights[k_num]
    (sr, sc), (h, w) = k.pos, k.size
    for r in range(sr, sr + h):
        for c in range(sc, sc + w):
            knights_board[r][c] = 0

def move_and_damage(q_num, q_d, moved_knights):

    dr, dc = MOVE[q_d]

    # 기사들 보드에서 지움
    for k_num in moved_knights:
        remove_knight_in_board(k_num)

    # 다시 추가하면서, 클래스 업데이트 하고, 대미지 확인

    for k_num in moved_knights:
        k = knights[k_num]
        (sr, sc), (h, w) = k.pos, k.size
        for r in range(sr, sr+h):
            for c in range(sc, sc+w):
                nr, nc = r+dr, c+dc

                # 공격 명령을 받은 기사가 아닌데, 새 위치에 함정이 있을 경우
                if k_num != q_num and map_board[nr][nc] == 1:
                    k.dam += 1

                knights_board[nr][nc] = k_num
        k.pos = (sr + dr, sc + dc)

        # 사망한 기사면 다시 보드에서 지운다
        if k.k <= k.dam:
            remove_knight_in_board(k_num)


# ===================================
# 메인 로직
# ===================================
def main():
    init_data()
    if DEBUG: print()

    for _ in range(Q):
        q_num, q_d = map(int, input().split())

        q_k = knights[q_num]
        if q_k.k <= q_k.dam: continue

        # 연쇄 이동 및 가능 여부 반환
        moved, moved_knights = check_move(q_num, q_d)

        if not moved: continue

        move_and_damage(q_num, q_d, moved_knights)

        if DEBUG: print()

    ans = 0
    for k in knights[1:]:
        if k.k > k.dam:
            ans += k.dam

    print(ans)
main()