'''
루돌프의 반란: 2023 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rudolph-rebellion

[시간 소요 포인트] MOVE에서 대각선 이동 정도 잘못 적어서 오류 발생, 이걸로 디버깅 시간 좀 씀
[TC3 fail] 산타 턴에서 충돌 시 밀려나는 걸 D-1로 한번에 계산했는데, 이 과정에서 D-1 = 0이 되었을 때 로직에 오류 발생
[TC4 fail] 조기 종료 조건 넣으려고 한 걸 깜빡해서 에러 발생
'''
from collections import deque

# =============================================
# 전역 변수 및 클래스
# =============================================
INF = float('inf')
MOVE = [(-1,0), (0,1), (+1,0), (0,-1), (-1,1), (1,1), (1,-1), (-1,-1)] # 상 우 하 좌 우상 우하 좌하 좌상

N, M, P, C, D = -1, -1, -1, -1, -1

out_cnt = 0
s_list = []
board = []

class Santa:
    def __init__(self, num, r, c):
        self.num = num
        self.r = r
        self.c = c
        self.score = 0
        self.status = 0 # 0 정상, -1 아웃?, 1부터 복귀 턴 수

# =============================================
# 보조 함수
# =============================================
# 초기 데이터 입력
def input_data():
    global N, M, P, C, D, s_list, board

    N, M, P, C, D = map(int, input().split())
    s_list = [None]*(P+1) # 0 패딩
    board = [ [0]*N for _ in range(N) ] # 0 빈칸 1~ 산타
    rr, rc = map(lambda x:int(x)-1, input().split())

    for _ in range(P):
        num, r, c = map(int, input().split())
        r, c = r-1, c-1
        new_santa = Santa(num, r, c)
        board[r][c] = num
        s_list[num] = new_santa

    return rr, rc

# 거리 계산 함수
def cal_dis(r1, c1, r2, c2):
    return (r1-r2)**2 + (c1-c2)**2

# 격자 범위 측정 함수
def is_range(r, c):
    return 0<=r<N and 0<=c<N

# 가장 가까운 산타 찾기
def find_near_santa(rr, rc):
    ans = (INF, INF, INF, INF) # 거리, -r, -c, 산타 번호

    for idx in range(1, P+1):
        san = s_list[idx]
        # 탈락한 산타에게는 가지 않음
        if san.status == -1 : continue
        dis = cal_dis(san.r, san.c, rr, rc)
        ans = min(ans, (dis, -san.r, -san.c, san.num))

    return ans[3]

# 루돌프 이동
def move_ru(san_num, rr, rc, t):

    # 산타 좌표 추출
    san = s_list[san_num]
    r, c = san.r, san.c

    # 루돌프 이동 좌표 선정
    ru_nxt = (INF, INF, INF, INF) # dis, r, c, d
    for d in range(8): # 8방향 이동
        dr, dc = MOVE[d]
        nr, nc = dr+rr, dc+rc
        if is_range(nr, nc):
            dis = cal_dis(r, c, nr, nc)
            ru_nxt = min(ru_nxt, (dis, nr, nc, d))
            # if t==6:
            #     print()
    # print()

    # 이동
    return ru_nxt[1], ru_nxt[2], ru_nxt[3]

# 산타 이동 방향
def find_move_santa(san, rr, rc, t):
    sr, sc = san.r, san.c
    default_dis = cal_dis(sr, sc, rr, rc)
    santa_next = (default_dis, INF, INF, INF) # 거리, 방향, r, c

    for d in range(4): # 상우하좌
        dr, dc = MOVE[d]
        nr, nc = dr+sr, dc+sc
        # 격자 내, 다른 산타 없음
        if is_range(nr, nc) and board[nr][nc] == 0:
            dis = cal_dis(nr,nc, rr,rc)
            santa_next = min(santa_next, (dis, d, nr, nc))
            # if t==6:
            #     print()
    # print()
    return (santa_next[1], santa_next[2], santa_next[3]) if santa_next[1]!=INF else (-1, -1, -1)

# 상호작용하며 산타 이동
# fr,fc: 첫 번째
def move_santa(s_san, d, turn):
    global out_cnt

    # 루돌프의 턴이었을 경우, 해당 방향으로 C만큼
    if turn == 'r':
        dr, dc = MOVE[d]
        q = deque([(s_san, C)])
    # 산타의 턴이었을 경우, 반대 방향으로 D만큼
    else:
        dr, dc = MOVE[(d+2)%4]
        q = deque([(s_san, D-1)]) # 앞으로 한 칸, 뒤로 D만큼이므로 한번에 D-1 처리
    # 이후 연쇄 반응
    while q:
        c_san, m_cnt = q.popleft()

        # 제자리일 경우 넘어감
        if m_cnt==0: continue

        cr, cc = c_san.r, c_san.c
        nr, nc = cr+dr*m_cnt, cc+dc*m_cnt
        # print()

        # 범위 밖으로 넘어가면 아웃
        if is_range(nr, nc):
            # 이동 위치에 다른 산타가 있을 경우, 큐에 넣음
            if board[nr][nc] != 0:
                nxt_num = board[nr][nc]
                q.append((s_list[nxt_num], 1))
            board[nr][nc] = c_san.num
            c_san.r, c_san.c = nr, nc

        else:
            c_san.status = -1
            out_cnt += 1

        # 이전 위치에 업데이트된 바가 없을 경우, 보드 업데이트
        # 이동했든 탈락했든 그 위치에서 사라지는 건 같음
        if board[cr][cc] == c_san.num:
            board[cr][cc] = 0

        # =============================================
# 메인 로직
# =============================================
def main():
    # ======================
    # 0. 초기 데이터 입력
    # ======================
    rr, rc = input_data()
    # print()

    for t in range(M): # 턴 진행
        # ======================
        # 1. 루돌프 움직임
        # ======================
        # 가장 가까운 산타 찾기
        target_san_num = find_near_santa(rr, rc)
        # 해당 방향으로 이동
        rr, rc, rd = move_ru(target_san_num, rr, rc, t)
        # 해당 방향에 다른 산타가 있을 경우, 점수 획득 및 연쇄 시작
        if board[rr][rc] != 0:
            san_num = board[rr][rc]
            san = s_list[san_num]
            san.score += C
            san.status = t+2
            move_santa(san, rd, 'r')

        # print()

        # ======================
        # 2. 산타 이동
        # ======================
        for num in range(1, P+1):
            # 기절했거나 탈락했을 경우 pass
            san = s_list[num]
            if san.status == -1: continue
            if san.status == 0 or san.status <= t:
                # num 산타의 다음 좌표
                nd, nr, nc = find_move_santa(san, rr, rc, t)
                if nr==-1: continue

                # 루돌프가 있을 경우
                if nr==rr and nc==rc:
                    # 충돌 점수, 기절
                    san.score += D
                    san.status = t+2
                    # 상호작용하며 이동
                    move_santa(san, nd, 's')
                else:
                    board[san.r][san.c] = 0
                    san.r, san.c = nr, nc
                    board[nr][nc] = num

                # print()

        # ======================
        # 3. 턴 종료 및 점수 획득
        # ======================
        for num in range(1, P+1):
            san = s_list[num]
            if san.status > -1:
                san.score += 1
        # print()

        # 모든 산타가 탈락하면, 조기 종료
        if out_cnt == P:
            break

    # ======================
    # 4. 최종 점수 출력
    # ======================
    ans = []
    for idx in range(1, P+1):
        ans.append(s_list[idx].score)

    print(' '.join(map(str, ans)))

main()