'''
코드트리 오마카세: 2023 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-omakase

문제 분석: 1h 10m 30s
  [시간 소요] 시간 복잡도를 통과할 만한 방법을 계속 고민
코드 작성: 2h 12m 19s
  [시간 소요] 고민하다가 초점을 잃어버렸는지, '각 사람이 몇 초에 떠났는지' 결과만 따지면 될 줄 알고 그렇게 풀었었는데,
            풀다가 생각해보니 스냅샷이 필요한 문제였음. -> 이에 멈추고 다시 계획하고 다시 풂
1차 디버깅: 1m 51s
  [TC5 error] 촬영 단계에서 손님이 오지 않았을 때를 고려하지 않음 -> for d in food[name]에서 key error 발생
  [TC11 timeover] 시간초과 미해결 상태

'''
from collections import defaultdict
from bisect import bisect_right

# ==========================================
# 전역 선언
# ==========================================
L, Q = -1, -1

people = {} # name: [t, x, n]
# seat = defaultdict(tuple) # name: (t, x, n)
food = {} # name: {b1: [t1, t2...], b2: [...], ...}
picture_time = []

# food[1] = defaultdict(tuple)
# food[1][2] = (3, 4)
# print()
# ==========================================
# 보조 함수
# ==========================================

# 모든 데이터를 우선 미리 받음
def input_data():
    global L, Q

    L, Q = map(int, input().split())
    lines = [list(input().split()) for _ in range(Q)]

    for line in lines:

        # 200: 손님 입장
        if line[0] == '200':
            t, x, name, n = int(line[1]), int(line[2]), line[3], int(line[4])
            people[name] = [t,x,n]

        # 300: 사진 촬영
        elif line[0] == '300':
            picture_time.append(int(line[1]))

    return lines

# t1초 이후, name(x) 앞에 오는 b 벨트의 초밥은 언제 도착하는지?
def cal_next_arrive_time(t1, name, b2):
    x = people[name][1]

    # 최근 초밥이 놓인 이후 또는 name이 입장한 이후로(t1) 좌석(x)과 벨트(b2)가 겹치는 첫 시간
    # t1 이후 b2 벨트는 언제 x 좌석으로 오는지? 를 계산!

    # t1초에 x 좌석 앞에 있는 벨트 번호(b1)는?
    b1 = (x - t1) % L

    # 만약 지금 도착했을 경우, 현재 시간을 반환
    if b1 == b2: return t1

    # b1이 지나가고 목표인 b2가 오는데 걸리는 시간은?
    after_t = (b1 - b2) % L

    # 최종적으로 b가 도착하는 시간은 t1 + after_t
    return t1 + after_t

# ==========================================
# 메인 로직
# ==========================================
def main():
    people_now = set() # 지금 당장 매장에 존재하는 사람 목록
    total_cnt = 0 # 총 남은 초밥 수
    answer = []

    lines = input_data()

    for line in lines:
        # 100: 초밥 추가
        if line[0] == '100':
            total_cnt += 1

            t, x, name = int(line[1]), int(line[2]), line[3]
            # t초 후 x 앞에 있는 벨트 b
            b = (x-t) % L

            if not name in food:
                food[name] = {}

            if not b in food[name]:
                food[name][b] = defaultdict(int) # key 초에 value개의 초밥을 먹을 수 있음

            # 지금 초밥은 언제 먹을 수 있는지 계산
            max_t = max(people[name][0], t) # max(name 오는 시간, 초밥 투입 시간)
            nxt_arrive = cal_next_arrive_time(max_t, name, b) # nxt_arrive초 이후면 먹은거임!!

            # 이 반영사항은 몇 번째 촬영에서 드러나는가?
            pic_idx = bisect_right(picture_time, nxt_arrive-1)
            pic_time = picture_time[pic_idx] if pic_idx < len(picture_time) else -1

            food[name][b][pic_time] += 1
            # print()
        # 200: 손님 입장
        elif line[0] == '200':
            people_now.add(line[3])
        # 300: 사진 촬영
        elif line[0] == '300':
            t = int(line[1])
            eat_cnt = 0

            # 각 name-b에 대해서, t초가 있는지만 찾으면 됨!
            leave_peoples = set()
            for name in people_now:
                # 사람은 왔는데 초밥이 아직 오지 않은 경우 pass (어차피 못 떠남)
                if not name in food: continue

                for d in food[name]:
                    if t in food[name][d]:
                        eat_cnt += food[name][d][t]
                        people[name][2] -= food[name][d][t]

                        # 퇴장 여부 판단
                        if people[name][2] <= 0:
                            leave_peoples.add(name)

            people_now -= leave_peoples
            total_cnt -= eat_cnt
            answer.append(f'{len(people_now)} {total_cnt}')

            # print()

    # print()
    print('\n'.join(answer))

main()