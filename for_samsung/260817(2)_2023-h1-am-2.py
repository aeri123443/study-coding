'''
토끼와 경주: 2023 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rabit-and-race/description

'''

# ===================================================
# 전역, 클래스
# ===================================================
# A: 동일 방향일 때, 토끼가 다시 돌아오기까지의 이동거리 텀
# B: 반대 방향일 때, 토끼가 다시 돌아오기까지의 최소 이동거리
NA, NB, MA, MB = -1, -1, -1, -1

Q, N, M, P = -1, -1, -1, -1
INF = float('inf')
MOVE = [(0,+1), (+1,0), (0,-1), (-1,0)]

rabbits = {}

class Rabbit:
    def __init__(self, num, dis):
        self.num = num
        self.dis = dis
        self.pos = (0,0)
        self.cnt = 0 # 점프 횟수

# ===================================================
# 보조 함수
# ===================================================
# 디버깅, 토끼 위치
def debug_print():
    print_board = [[set() for _ in range(M)] for _ in range(N)]
    print()
    for r in rabbits.values():
        print(f'num:{r.num}, dis:{r.dis}, pos:{r.pos}, cnt:{r.cnt}')
        rr, rc = r.pos
        print_board[rr][rc].add(r.num)

    for pb in print_board:
        print('\t\t\t'.join(map(str, pb)))

# 초기 데이터 입력
def input_data(line):
    global N, M, P, NA, NB, MA, MB

    N, M, P = line[1], line[2], line[3]

    for i in range(P):
        idx = i*2 + 4
        num, dis = line[idx], line[idx+1]
        rabbits[num] = Rabbit(num, dis)

    # A: 동일 방향일 때, 토끼가 다시 돌아오기까지의 이동거리 텀
    # B: 반대 방향일 때, 토끼가 다시 돌아오기까지의 최소 이동거리
    NA, NB = (N-1)*2, (N-2)*2
    MA, MB = (M-1)*2, (M-2)*2

# 도착 좌표 계산
def cal_arrive_pos(cr, cc, dis, d):
    nr, nc = -1, -1
    # start에서 n만큼 더해갔을 때,  dis보다 작지만 dis와 가장 가까운 값 반환
    def get_min_near_dis(st, n):
        q = (dis-st) // n
        return q * n + st

    # 좌우 이동(M)
    if d in (0, 2):
        # 양끝까지의 이동거리 중, dis보다 작지만 dis와 가장 가까운 값은?
        if d == 0:
            e = M - cc - 1
            s = e + (M-1)
        else:
            s = cc
            e = s + M - 1

        if cc == 0: s = 0
        elif cc == M-1: e = 0

        s = get_min_near_dis(s, (M-1)*2)
        e = get_min_near_dis(e, (M-1)*2)

        s_diff, e_diff = dis-s, dis-e

        # s가 더 가까울 경우, + 방향으로 s_diff만큼 이동
        if s_diff < e_diff:
            nr, nc = cr, cc + s_diff
        # e_diff가 더 가까울 경우, - 방향으로 e_diff만큼 이동
        else:
            nr, nc = cr, cc - e_diff

    # 상하 이동 (N)
    else:
        # 양끝까지의 이동거리 중, dis보다 작지만 dis와 가장 가까운 값은?
        if d == 1:
            s = N - 1 - cr
            e = s + N - 1
        else:
            s = cr
            e = s + N - 1

        if cr == 0:
            s = 0
        elif cr == N - 1:
            e = 0
        print()
        s = get_min_near_dis(s, (N - 1) * 2)
        e = get_min_near_dis(e, (N - 1) * 2)

        s_diff, e_diff = dis - s, dis - e

        # s가 더 가까울 경우, + 방향으로 s_diff만큼 이동
        if s_diff < e_diff:
            nr, nc = cr + s_diff, cc
        # e_diff가 더 가까울 경우, - 방향으로 e_diff만큼 이동
        else:
            nr, nc = cr - e_diff, cc

    print()

    return nr, nc
# 움직일 토끼와 도착 좌표 반환
def move_rabbit():

    # 움직일 토끼 선정
    rabbit_info = (INF, INF, INF, INF, INF)

    for r in rabbits.values():
        num, dis, cnt = r.num, r.dis, r.cnt
        rr, rc = r.pos
        rabbit_info = min(rabbit_info, (cnt, (rr+rc), rr, rc, num))

    num = rabbit_info[4]
    dis = rabbits[num].dis
    rr, rc = rabbits[num].pos

    print()

    # 이동 방향 선정
    pos_info = (-INF, -INF, -INF) # 최종 좌표 기준

    for d in range(4):
        cal_arrive_pos(rr, rc, dis, d)

# ===================================================
# 메인 로직
# ===================================================
def main():
    global Q

    Q = int(input())

    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 경주 준비
        if cmd == 100:
            input_data(line)
        # 경주 진행
        elif cmd == 200:
            k, s = line[1], line[2]
            # K턴 경주 진행
            for _ in range(k):
                # 움직일 토끼와 도착 좌표 반환
                move_rabbit()
                # 토끼 이동
                # 토끼 움직인 횟수, 누적합 업데이트
                debug_print()
            # 최종 점수 부여
        # 이동거리 변경
        # 가장 높은 점수 출력
        debug_print()
        print()

main()