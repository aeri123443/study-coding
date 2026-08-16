'''
마법의 숲 탐색: 2024 상반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration

문제 분석: 21m 11s
  - [시간 소요] 갑자기 예외 케이스 하나가 궁금해짐! 골렘의 아랫부분만 숲에 들어가고, 왼쪽 부분이 숲 밖으로 튀어나온 채로 걸친 모습인데, 이런 식으로 숲 밖에서는 좌우 이동이 자유로운지, 좌우 패딩도 적용해야하는지를 고민함.
            -> 이동 가능해서 우선순위에 의해 동쪽 안 살펴보고 서쪽으로 이동하지만, 숲 밖이어서 board 초기화하는 경우가 생길지 고민!
            -> 이런 케이스를 생각 안 해도 일전에 통과했었고, 관련된 문구가 문제에 있나 계속 찾아보다가 시간이 조금 소요됨
코드 작성: 1h 12m 10s
  - [시간 소요] 요정 bfs에서 요정이 정상적으로 내려오지 않아 디버깅해봄
            -> 출구 찾기에서 e_cr, e_cc = e_dr+cr, e_dc+cc로 잘못 적어서 출구가 잘못 나옴
            -> 다른 골렘으로 이동할 때는 q.append((nr, nc, board[nr][nc])) 해야했는데 복붙하느라 그냥 q.append((nr, nc, ck))를 넣어서 오류
               생각해보니 큐에 골렘 번호는 넣지 않아도 충분히 현재 위치 기준으로 추출해낼 수 있었는데, 일단 그렇게 코딩해버렸으니 걍 넘어감
최종 디버깅: 0m 0s

총 소요 시간: 1h 33m 21s
'''
from collections import deque

# ================================================
# 전역 선언 및 클래스
# ================================================
R, C, K = -1, -1, -1
MOVE = [(-1,0), (0,+1), (+1,0), (0,-1)] # 북동남서

ans = []
board = []
golems = {}

class Golem:
    def __init__(self, num, r, c, d):
        self.num = num
        self.r = r
        self.c = c
        self.d = d

# ================================================
# 보조 함수
# ================================================

# 숲 내부인지 확인
def is_range(r, c):
    return 3<=r<R+3 and 0<=c<C

# 골렘이 이동할 수 있는 최종 r, c, d 반환
def check_golem_move(c, d):
    cr, cc, cd = 0, c, d

    def is_range_golem(_r, _c):
        return 0<=_r<R+3 and 0<=_c<C

    while True:

        # 남쪽 이동 확인
        if all([is_range_golem(cr+dr, cc+dc) and board[cr+dr][cc+dc]==0
                for dr, dc in [(+1, -1), (+2, 0), (+1, +1)]]):
            cr, cc, cd = cr+1, cc, cd
            continue

        # 동쪽 이동 확인
        elif all([is_range_golem(cr+dr, cc+dc) and board[cr+dr][cc+dc]==0
                for dr, dc in [(-1, -1), (0, -2), (+1, -2), (+1, -1), (+2, -1)]]):
            cr, cc, cd = cr+1, cc-1, (cd-1)%4
            continue

        # 서쪽 이동 확인
        elif all([is_range_golem(cr+dr, cc+dc) and board[cr+dr][cc+dc]==0
                for dr, dc in [(-1, +1), (0, +2), (+1, +1), (+1, +2), (+2, +1)]]):
            cr, cc, cd = cr+1, cc+1, (cd+1)%4
            continue

        # 모든 이동이 안 되면 반복문 탈출
        break

    return cr, cc, cd


# bfs로 정령 이동 후 최종 r 위치 반환
def move_elf(k, sr, sc):
    max_r = sr

    visited = [[False]*C for _ in range(R+3)]
    visited[sr][sc] = True
    q = deque([(sr, sc, k)]) # 현재 위치와 현재 있는 골렘 번호

    while q:
        cr, cc, ck = q.popleft()

        # 현재 있는 골렘의 출구 좌표
        g = golems[ck]
        e_dr, e_dc = MOVE[g.d]
        e_cr, e_cc = e_dr+g.r, e_dc+g.c
        # print()
        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            if is_range(nr, nc) and not visited[nr][nc] and board[nr][nc] != 0:
                # 같은 골렘이면, 그냥 이동
                if board[nr][nc] == ck:
                    q.append((nr, nc, ck))
                    visited[nr][nc] = True
                    max_r = max(max_r, nr)
                # 다른 골렘이면 지금 출구에 있어야 이동 가능
                elif (e_cr, e_cc) == (cr, cc):
                    q.append((nr, nc, board[nr][nc]))
                    visited[nr][nc] = True
                    max_r = max(max_r, nr)

    return max_r



# ================================================
# 메인 로직
# ================================================
def main():
    global R, C, K, board, golems

    R, C, K = map(int, input().split())
    board = [[0]*C for _ in range(R+3)]

    for k in range(1, K+1):
        c, d = map(int, input().split())
        c -= 1

        # ======================
        # 1. 골렘 하강
        # ======================

        # 골렘이 이동할 수 있는 최종 r, c, d 반환
        kr, kc, kd = check_golem_move(c, d)

        # print()
        # 골렘이 숲 안에 있는지 확인, 아닐 경우 숲 초기화
        # 숲 내부에 있을 경우 골렘 객체 생성 및 업데이트
        if all([is_range(dr+kr, dc+kc) for dr, dc in [(0,0), (-1,0), (0,+1), (+1,0), (0,-1)]]):
            new_golem = Golem(k, kr, kc, kd)
            golems[k] = new_golem
            for dr, dc in [(0, 0), (-1, 0), (0, +1), (+1, 0), (0, -1)]:
                board[dr+kr][dc+kc] = k
        else:
            board = [[0]*C for _ in range(R+3)]
            golems = {}
            continue
        # print()

        # ======================
        # 2. 정령 이동
        # ======================

        # bfs로 정령 이동 후 최종 r 위치 반환
        max_r = move_elf(k, kr, kc)
        ans.append(max_r-2)
        # print()

    print(sum(ans))

main()