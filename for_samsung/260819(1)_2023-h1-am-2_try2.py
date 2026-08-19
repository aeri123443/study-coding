'''
토끼와 경주: 2023 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rabit-and-race/description

문제 분석: 11m 19s
코드 1차 작성: 1h 03m 52s
디버깅 및 코드 2차 작성: 31m 51s
  [TC2 MLE] 최대 케이스에 대해 디버깅용 board를 그대로 넣어서 메모리 초과 발생, board를 빼고 돌려봐도 시간이 너무 오래 걸림
           -> 시간복잡도 계산 미스로 기존의 토끼를 하나하나 보며 경주 우선순위를 정했던 방식이 시간 초과를 유발함을 확인, heapq 추가
                & 기존에 매 200마다 있었던 prefix&total을 전역으로 뺀 후 400에서 일괄 계산 코드를

총 소요 시간: 1h 47m 02s
'''
from collections import defaultdict
import heapq

# ========================================
# 전역 선언 및 클래스
# ========================================
Q, P, N, M = -1, -1, -1, -1
LN, LM = -1, -1 # 연장된 좌표
INF = float('inf')
MOVE = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

rabbits = {}
prefix_dict = defaultdict(int) # 누적합
prefix_total = 0
q = []


class Rabbit:
    def __init__(self, pid, dis):
        self.pid = pid
        self.dis = dis
        self.pos = (0,0) # 초기 위치
        self.jump = 0 # 초기 점프 횟수
        self.score = 0  # 초기 점수

    # 우선순위 비교를 위한 정보 반환
    def get_info(self):
        r, c = self.pos
        return self.pid, r, c, self.jump

# ========================================
# 보조 함수
# ========================================
def init_data(line):
    global LN, LM, N, M, P

    N, M, P = line[1:4]
    LN = 2*N - 2
    LM = 2*M - 2

    for idx in range(P):
        pid = line[idx * 2 + 4]
        dis = line[idx * 2 + 5]

        rabbits[pid] = Rabbit(pid, dis)
        heapq.heappush( q, (0, 0, 0, 0, pid) )


# 달릴 토끼 선정
# pid 반환
def choose_run_rabbit():
    ra_info = (INF, INF, INF, INF, INF) # min... jump, r+c, r, c, pid

    for ra in rabbits.values():
        pid, r, c, jump = ra.get_info()
        tmp_info = (jump, r+c, r, c, pid)
        ra_info = min(ra_info, tmp_info)

    return ra_info[4]

# 다음 위치 계산
def cal_next_pos(nr, nc):
    if 0<=nr<N and 0<=nc<M: return nr, nc

    # 기본적으로 연장된 길이 기준으로 계산 후
    lr, lc = nr%LN, nc%LM

    # 기존 범위 넘어갈 경우 보정된 값을 반환
    new_nr = lr if 0<=lr<N else LN - lr
    new_nc = lc if 0<=lc<M else LM - lc

    return new_nr, new_nc

# 다음 위치 선정
def choose_next_pos(run_pid):
    pos_info = (-INF, -INF, -INF) # max... r+c, r, c
    ra = rabbits[run_pid]
    sr, sc = ra.pos
    dis = ra.dis

    for dr, dc in MOVE:
        nr, nc = cal_next_pos(sr+dr*dis, sc+dc*dis)
        tmp_info = (nr+nc, nr, nc)
        pos_info = max(pos_info, tmp_info)

    return pos_info


# 토끼 점수 업데이트
def update_score(total, prefix, s):
    ra_info = (-INF, -INF, -INF, -INF) # max... r+c, r, c, pid

    # prefix 점수 업데이트 및 우선순위 토끼 선정
    for pid, val in prefix.items():
        ra = rabbits[pid]
        ra.score += (total-val)

        r, c = ra.pos
        tmp_info = (r+c, r, c, pid)
        ra_info = max(ra_info, tmp_info)

    rabbits[ra_info[3]].score += s

# 최고의 토끼 선정
def find_winner(run_rabbit_set, s):
    ra_info = (-INF, -INF, -INF, -INF)  # max... r+c, r, c, pid

    for pid in run_rabbit_set:
        ra = rabbits[pid]
        r, c = ra.pos
        tmp_info = (r + c, r, c, pid)
        ra_info = max(ra_info, tmp_info)

    rabbits[ra_info[3]].score += s

def find_best_score():
    max_score = 0

    for ra in rabbits.values():
        pid, score = ra.pid, ra.score
        score += (prefix_total - (prefix_dict[pid] if pid in prefix_dict else 0))

        max_score = max(max_score, score)

    return max_score

# ========================================
# 메인 로직
# ========================================
def main():
    global Q, prefix_total

    Q = int(input())

    for _q in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 경주 시작 준비
        if cmd == 100:
            init_data(line)
        # 경주 진행
        elif cmd == 200:
            k, s = line[1:]

            # k번 진행
            run_rabbit_set = set()
            for _k in range(k):
                # 달릴 토끼 선정
                _, _, _, _, run_pid = heapq.heappop(q)
                # run_pid = choose_run_rabbit()

                # 다음 위치 선정
                _sum, nr, nc = choose_next_pos(run_pid)

                # 달린 토끼 정보 업데이트: (r+c) 누적, total 누적 -> 나중에 빼는 용도
                run_rabbit_set.add(run_pid)

                rabbits[run_pid].jump += 1
                rabbits[run_pid].pos = (nr, nc)
                heapq.heappush(q, (rabbits[run_pid].jump, nr+nc, nr, nc, run_pid))

                prefix_dict[run_pid] += (nr+nc+2)
                prefix_total += (nr+nc+2)
                # print()

            # 토끼 점수 업데이트
            # update_score(total, prefix, s)

            # 최고의 토끼 선정 및 점수 부여
            find_winner(run_rabbit_set, s)

        # 이동거리 변경
        elif cmd == 300:
            pid, dis = line[1:]
            rabbits[pid].dis *= dis

        # 최고의 토끼 선정
        elif cmd == 400:
            best_score = find_best_score()
            print(best_score)

        # print()

main()