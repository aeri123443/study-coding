'''
아기 바다거북의 대모험: 해저 화산 지대: 2026 상반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/

문제 분석: 18m 40s
코드 작성: 1h 17m 01s
최종 디버깅: 0m 0s

총 소요 시간: 1h 35m 41s
'''

from collections import deque

# ==========================================
# 전역 선언 및 클래스
# ==========================================

N, M, K = -1, -1, -1
MOVE = [(0,+1), (+1,0), (0,-1), (-1,0)] # 우하좌상

class Mountain:
    def __init__(self, num, r, c, p):
        self.num = num
        self.pos = (r,c)
        self.p = p # 임계치
        self.status = 0 # 현재 압력

class Turtle:
    def __init__(self, num, r, c):
        self.num = num
        self.pos = (r, c)
        self.escape = 0 # 탈출 시 탈출 시간(1~), 화석 -1

move_board = []
mountain_board = []

turtles = [Turtle(-1, -1, -1)] # 0 패딩
mountains = [Mountain(-1,-1,-1,-1)]  # 0 패딩

# ==========================================
# 보조 함수
# ==========================================

def input_data():
    global N, M, K, move_board, mountain_board

    N, M, K = map(int, input().split())

    # 산호초 1 -> -1 변환
    move_board = [list(map(lambda x: int(x) * -1, input().split())) for _ in range(N)]

    # 거북이
    for i in range(1, M+1):
        tr, tc = map(int, input().split())
        move_board[tr][tc] = i

        new_turtle = Turtle(i, tr, tc)
        turtles.append(new_turtle)

    # 화산
    mountain_board = [[0]*N for _ in range(N)]
    for k in range(1, K+1):
        mr, mc, mp = map(int, input().split())

        new_mountain = Mountain(k, mr, mc, mp)
        mountains.append(new_mountain)

        mountain_board[mr][mc] = k

def is_range(r, c):
    return 0<=r<N and 0<=c<N

# 최단경로 찾기 (역 bfs)
def find_route(t):
    num = t.num
    sr, sc = t.pos

    def rev_bfs():
        q = deque([(N-1, N-1)])
        visited = [[-1]*N for _ in range(N)]
        visited[N-1][N-1] = 0

        while q:
            cr, cc = q.popleft()

            for dr, dc in MOVE:
                nr, nc = dr+cr, dc+cc

                if is_range(nr,nc) and visited[nr][nc] == -1 and move_board[nr][nc] in (0, num):
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))

                    if (nr,nc) == (sr,sc): return visited

        return visited

    visited = rev_bfs()

    cnt = visited[sr][sc]
    if cnt == -1 : return -1, -1

    for dr, dc in MOVE:
        nr, nc = dr+sr, dc+sc
        if is_range(nr, nc) and visited[nr][nc] == cnt-1:
            return nr, nc

    return -1, -1


# 화산 분출 및 연쇄
def active_mountain(new_actives):
    fire = [[0]*N for _ in range(N)]
    q = deque([*new_actives])
    active_set = {*new_actives}

    while q:
        m_num = q.popleft()
        m = mountains[m_num]
        sr, sc = m.pos

        # 4방향 분출 (열기 업데이트)
        f = m.p
        fire[sr][sc] += f
        for dr, dc in MOVE:

            cr, cc = dr+sr, dc+sc
            cur_f = f // 2
            while is_range(cr, cc):
                if cur_f<=0 or move_board[cr][cc] == -1: break

                fire[cr][cc] += cur_f

                # 해당 위치에 화산이 있고, 분출하는지 판단 후 큐에 넣음
                if mountain_board[cr][cc] > 0 and mountain_board[cr][cc] != m.num and not mountain_board[cr][cc] in active_set:
                    other_m = mountains[mountain_board[cr][cc]]
                    if fire[cr][cc] + other_m.status >= other_m.p:
                        active_set.add(other_m.num)
                        q.append(other_m.num)

                cr += dr
                cc += dc
                cur_f //= 2

    return active_set, fire

# ==========================================
# 메인 로직
# ==========================================
def main():
    # 0: 초기 데이터 입력
    input_data()
    # print()

    remain_turtle = M
    for turn in range(1, 101):
        # 1. 바다거북 이동
        for m in range(1, M+1):
            t = turtles[m]
            if t.escape != 0 : continue

            # 최단경로 찾기
            nr, nc = find_route(t)

            # 최단경로 존재시 이동, 탈출 여부 확인
            if nr == -1: continue

            cr, cc = t.pos
            move_board[cr][cc] = 0

            if (nr,nc) == (N-1, N-1):
                t.escape = turn
                remain_turtle -= 1
            else:
                move_board[nr][nc] = t.num
                t.pos = (nr,nc)
        # print()

        # 조기 종료: 모든 거북이 탈출
        if remain_turtle <= 0: break

        # 2. 화산 압력 증가
        new_actives = set()
        for k in range(1, K+1):
            mo = mountains[k]
            mo.status += 10

            if mo.status >= mo.p:
                new_actives.add(mo.num)
        # print()

        # 3. 화산 분출 및 연쇄
        if not new_actives: continue

        active_set, fire = active_mountain(new_actives)

        # 4. 화석화
        for t_num in range(1, M+1):
            t = turtles[t_num]

            if t.escape != 0 : continue

            tr, tc = t.pos
            if fire[tr][tc] >= 20:
                t.escape = -1
                move_board[tr][tc] = -2
                remain_turtle -= 1

        # print()

        # 조기 종료: 모든 거북이 탈출
        if remain_turtle <= 0: break

        # 5. 환경 초기화
        for m_num in active_set:
            mo = mountains[m_num]
            mo.status = 0

    # 6. 최종 탈출 시간 출력
    ans = [-1] * (M+1)
    for t_num in range(1, M+1):
        t = turtles[t_num]
        if t.escape > 0:
            ans[t_num] = t.escape

    print('\n'.join(map(str, ans[1:])))

main()