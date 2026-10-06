"""
# 2024 상반기 오후 1번 · 마법의 숲 탐색
정령 K: 북을 통해서만 진입
골렘: 십자5칸 중 출구 1칸

class 골렘
    - num
    - 중앙 위치
    - 출구 방향

골렘 board [] : 0 빈칸, k 골렘, -k 골렘 출구

def 골렘 다음 위치 확인 (현재 중앙 위치, 방향)
def 가능할 경우 골렘 이동, 출구 변화
def 정령 범위 패딩 미적용된 범위 내에 있는지 확인

def 골렘이 패딩 미적용된 범위 내에 있는지 확인
    정령 범위 함수 활요하기

for K
1. 골렘 이동
    ** 숲의 바깥에서 시작
    1} 남쪽 하강: 다음 칸 확인 -> 있으면 내려감, 없으면 다음단계
    2) 불가시 서쪽 회전 하강
        - 왼쪽, 아래로
        - 출구 반시계
    3) 불가시 동쪽 회전 하강
        - 동쪽, 아래로
        - 출구 시계
    4) 불가시 종료
    if 골렘의 몸 일부가 숲 밖
        - 숲 초기화
        - 해당 턴 정령은 답에 포함하지 않음
        - 총합은 누적??

2. 정령 이동
    - 지금 있는 출구가 다른 골렘에 인접 -> 다음 골렘으로 이동 가능
        - 다음 위치가 같은 골렘 내 -> 이동 가능
        - 다음 위치가 다른 골렘 -> 현재 위치가 출구여야 함
    - 가장 남쪽으로 이동
        - 최대 행 번호 업데이트
    - 행 번호 반환

3. 최종 행의 총합 출력

# 1회독 3m 23s
# 2회독 12m 9s
# 설계 10m 40s
# 상태변화 표 작성 5m 4s
# non-fail pass.
# 총 소요시간: 1h 32m 48s
"""


from collections import deque

DEBUG = False
MOVE = [(-1,0), (0,1), (1,0), (0,-1)]
N, M, K = map(int, input().split())
golems = {}
board = [[0]*M for _ in range(N+3)] # 골렘 board [] : 0 빈칸, k 골렘, -k 골렘 출구

class Golem:
    def __init__(self, num, r, c, d):
        self.num = num
        self.pos = (r, c)
        self.d = d # 향후 제거

# 전역 입력 5m 49s



# 골렘 다음 위치 확인 (현재 중앙 위치, 방향)
def check_golem_move(cr, cc, d):
    if d == 2: d_list = [(+2,0),(+1,-1),(+1,+1)]
    elif d == 3: d_list = [(-1,-1),(0,-2),(+1,-2),(+1,-1),(+2,-1)]
    else: d_list = [(-1,+1),(0,+2),(+1,+1),(+1,+2),(+2,+1)] # 동쪽(1)

    for dr, dc in d_list:
        nr, nc = cr+dr, cc+dc
        # 범위 내, 다른 골렘 없음
        if not (0<=nr<(N+3) and 0<=nc<M and board[nr][nc] == 0):
            return False, -1, -1

    dr, dc = MOVE[d]
    return True, cr+dr, cc+dc

def is_range_without_padding(r, c):
    return 3<=r<N+3 and 0<=c<M

def add_golem(g_num, cr, cc, d):
    new_gol = Golem(g_num, cr, cc, d)
    golems[g_num] = new_gol
    board[cr][cc] = g_num
    for d_idx in range(4):
        dr, dc = MOVE[d_idx]
        nr, nc = cr+dr, cc+dc
        if d_idx == d: board[nr][nc] = -g_num # 출구일 경우
        else: board[nr][nc] = g_num

# 정령 이동
def move_elf(sr, sc):
    q = deque([(sr, sc)])
    visited = [[False]*M for _ in range(N+3)]
    visited[sr][sc] = True
    max_row = -1

    while q:
        cr, cc = q.popleft()
        cur_gol = abs(board[cr][cc])

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            # 미패딩 범위 내, 미방문, 장애물
            if is_range_without_padding(nr,nc) and not visited[nr][nc] and board[nr][nc] != 0:
                nxt_gol = abs(board[nr][nc])
                can_next = False
                # 다음 위치가 같은 골렘 내 -> 이동 가능
                if cur_gol == nxt_gol: can_next = True
                # 다음 위치가 다른 골렘 -> 현재 위치가 출구여야 함
                elif (cur_gol != nxt_gol) and (board[cr][cc] < 0): can_next = True

                if can_next:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    max_row = max(max_row, nr)
    return max_row

def main():
    global board, golems

    answer = []
    for g_num in range(1, K+1):
        # ======================
        # 1. 골렘 이동 45m 55s
        # ======================
        c, d = map(int, input().split())

        # 어디까지 내려갈 수 있나?
        cr, cc = 0, c-1
        while True:
            move_flag = True
            for down_d in [2, 3, 1]: # 남-서-동
                moved, nr, nc = check_golem_move(cr, cc, down_d)
                if moved:
                    cr, cc = nr, nc
                    move_flag = False

                    # 회전 업데이트
                    if down_d == 3: d = (d-1)%4 # 서쪽 -> 반시계
                    elif down_d == 1: d = (d+1)%4 # 동쪽 -> 시계

                    break

            if move_flag: break

        # 골렘이 숲 안으로 모두 들어왔는지?
        if all([is_range_without_padding(cr+dr, cc+dc) for dr,dc in MOVE]):
            add_golem(g_num, cr, cc, d)

        # 아닐 경우 숲 초기화, 정령 이동x
        else:
            board = [[0] * M for _ in range(N + 3)]  # 골렘 board [] : 0 빈칸, k 골렘, -k 골렘 출구
            golems = {}
            continue

        # if DEBUG: print()


        # ======================
        # 2. 정령 이동 8m 52s
        # ======================
        max_r = move_elf(cr, cc)
        answer.append(max_r-2) # 패딩 제거, 1-idx
        if DEBUG: print()

    print(sum(answer))

main()