'''
루돌프의 반란: 2023 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rudolph-rebellion

문제 분석: 15m 30s
코드 작성: 1h 25m 14s
최종 디버깅: 0m 0s

총 소요 시간: 1h 40m 45s
'''

from collections import deque

# =================================================
# 전역 선언 및 클래스
# =================================================

INF = float('inf')
N, M, P, C, D = -1, -1, -1, -1, -1
MOVE = [(-1, 0), (0, +1), (+1, 0), (0, -1), (-1, +1), (+1, +1), (+1, -1), (-1, -1)]

out_santa_cnt = 0 # 조기 종료 판정 용
ru = (-1, -1) # 루돌프 위치
santa_list = [] # 패딩 적용
board = []

class Santa:
    def __init__(self, num, r, c):
        self.num = num
        self.r = r
        self.c = c
        self.score = 0 # 점수
        self.status = 0 # -1 탈락, 0 정상, 1~ 기절 후 깨어나는 턴 수

# =================================================
# 보조 함수
# =================================================

# 초기 데이터 입력
def input_data():
    global N, M, P, C, D, ru, santa_list, board

    N, M, P, C, D = map(int, input().split())

    santa_list = [None]*(P+1)
    board = [[0]*N for _ in range(N)]

    # 루돌프
    rr, rc = map(lambda x: int(x)-1, input().split())
    ru = (rr, rc)
    board[rr][rc] = -1

    # 산타
    for _ in range(P):
        p, r, c = map(int, input().split())
        r, c = r-1, c-1

        santa_list[p] = Santa(p,r,c)
        board[r][c] = p

# 거리 계산
def cal_dis(r1, c1, r2, c2):
    return (r1-r2)**2 + (c1-c2)**2

# 범위 확인
def is_range(r, c):
    return 0<=r<N and 0<=c<N

# 가장 가까운 산타 찾기
def find_near_santa():
    santa_info = (INF, INF, INF, INF) # 거리 최소, r 최대, c 최대, 산타 번호
    rr, rc = ru
    for s_num in range(1, P+1):
        san = santa_list[s_num]

        if san.status == -1: continue

        san_r, san_c = san.r, san.c
        dis = cal_dis(rr, rc, san_r, san_c)
        santa_info = min(santa_info, (dis, -san_r, -san_c, s_num))

    return santa_info[3]

# 루돌프 다음 위치 반환
def get_ru_next_pos(san_num):
    global ru

    rr, rc = ru
    san = santa_list[san_num]
    san_r, san_c = san.r, san.c
    standard_dis = cal_dis(rr, rc, san_r, san_c)

    next_info = (INF, INF, INF, INF) # 거리 최소, nr, nc, 이동 방향

    for d in range(8):
        dr, dc = MOVE[d]
        nr, nc = dr+rr, dc+rc
        dis = cal_dis(nr, nc, san_r, san_c)

        if is_range(nr, nc) and dis < standard_dis:
            next_info = min(next_info, (dis, nr, nc, d))

    return next_info[1], next_info[2], next_info[3]

# 산타 연쇄 이동
def move_santa(start_san_num, d, turn):
    global out_santa_cnt

    if turn == 'ru':
        dr, dc = MOVE[d]
        q = deque([(start_san_num, C)]) # 이동하는 산타, 이동 칸 수
    else:
        dr, dc = MOVE[(d+2)%4]
        q = deque([(start_san_num, D-1)]) # 이 산타는 앞으로 갔다가 다시 뒤로 가기 때문에, -1 적용

    # 큐에 산타들을 담고 빼면서 board에서 산타를 지워나감
    moved_santa = []
    while q:
        san_num, dis = q.popleft()
        san = santa_list[san_num]

        cr, cc = san.r, san.c
        board[cr][cc] = 0

        nr, nc = cr + dr*dis, cc + dc*dis

        # 범위를 넘어가면 산타 아웃
        if not is_range(nr, nc):
            san.status = -1
            out_santa_cnt += 1
            continue

        # 아웃되지 않은 산타는 이동 목록에 추가
        moved_santa.append((san_num, dis))

        # 다음 위치에 다른 산타가 있으면, 그 산타는 1칸 밀려남
        if board[nr][nc] > 0:
            q.append((board[nr][nc], 1))

    # 새 좌표 기록
    for san_num, dis in moved_santa:
        san = santa_list[san_num]
        nr, nc = san.r + dis*dr, san.c + dis*dc
        san.r, san.c = nr, nc
        board[nr][nc] = san.num

# 산타 다음 이동 방향 (이동 가능 여부 확인)
def find_santa_next_pos(san_num):
    san = santa_list[san_num]
    sr, sc = san.r, san.c
    rr, rc = ru
    standard_dis = cal_dis(rr,rc, sr,sc)

    move_info = (INF, INF, INF, INF) # 거리 최소, 방향 최소, nr, nc

    # 4방향 이동
    for d in range(4):
        dr, dc = MOVE[d]
        nr, nc = dr+sr, dc+sc
        dis = cal_dis(nr, nc, rr, rc)
        if is_range(nr, nc) and board[nr][nc] in (-1, 0) and dis < standard_dis:
            move_info = min(move_info, (dis, d, nr, nc))

    # 이동 가능 여부 확인
    can_move = move_info[0] != INF

    return can_move, move_info
# =================================================
# 메인 로직
# =================================================
def main():
    global ru

    # 0. 초기 데이터 입력
    input_data()
    # print()

    for t in range(M):
        # =======================
        # 1. 루돌프 이동
        # =======================

        # 가장 가까운 산타 찾기
        target_santa_num = find_near_santa()

        # 루돌프 다음 위치 반환 (8방향)
        nxt_rr, nxt_rc, nxt_rd = get_ru_next_pos(target_santa_num)

        # 충돌 시 점수 획득 및 상호작용 발생
        if board[nxt_rr][nxt_rc] > 0:
            san_num = board[nxt_rr][nxt_rc]
            san = santa_list[san_num]

            san.score += C
            san.status = t + 2

            move_santa(san_num, nxt_rd, 'ru')

        # 루돌프 위치 업데이트
        rr, rc = ru
        board[rr][rc] = 0
        board[nxt_rr][nxt_rc] = -1
        ru = (nxt_rr, nxt_rc)

        # print()
        # 모든 산타 탈락 시 조기 종료
        if out_santa_cnt == P:
            break

        # =======================
        # 2. 산타 이동
        # =======================
        rr, rc = ru

        for san_num in range(1, P+1):
            san = santa_list[san_num]

            # 기절하거나 탈락한 산타는 움직일 수 없음
            if san.status == -1 or san.status > t:
                continue

            # 산타 다음 이동 방향 (이동 가능 여부 확인)
            can_move, (dis, d, nr, nc) = find_santa_next_pos(san_num)

            # 이동 가능할 경우, 충돌 시 점수 획득(기절) 및 상호작용 발생
            if can_move:
                # 충돌하면 상호작용
                if (nr, nc) == (rr, rc):
                    san.score += D
                    san.status = t+2

                    move_santa(san_num, d, 'san')

                # 충돌하지 않으면 그냥 위치 업데이트
                else:
                    cr, cc = san.r, san.c
                    board[cr][cc] = 0
                    board[nr][nc] = san_num
                    san.r, san.c = nr, nc
        # print()

        # 모든 산타 탈락 시 조기 종료
        if out_santa_cnt == P:
            break

        # 탈락하지 않은 산타는 1점씩 추가 획득
        for san_num in range(1, P+1):
            san = santa_list[san_num]
            if san.status != -1:
                san.score += 1

        # print()

    # =======================
    # 2. 최종 점수 출력
    # =======================
    ans = []
    for san_num in range(1, P+1):
        ans.append( santa_list[san_num].score )

    print(' '.join(map(str, ans)))

main()