"""
여행
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4805/curated-cards/mock-travel/description

- 케이스 점검
    - 각 <여행 케이스>가 잘 수행되는지
    - 도착 불가할 경우 -1
        - 유료 도로망중에 숙소!=출발점
        - 유료 도로망이 도착점까지 가지 않음

N 구역 (1-N 번호) (10_000)
M개 도로 (20_000)

s번 구역 숙소


여행 케이스 고려
    - 유료 도로망 0개
        1) 무료 하나만 (S -> 무료 -> D)

    - 유료 도로망 1개
        2) 유료 하나만 S(유료s) -> 유료 -> D
        3) 무료 -> 유료(S -> 무료 -> 유료s -> 유료 -> D)

    - 유료 도로망 2개
        4) 무료 -> 유료 -> 유료 (S -> 무료 -> 유료s -> 유료 -> 유료s -> 유료 -> D)
        5) 유료 -> 유료 (S(유료s)-> 유료 -> 유료s -> 유료 D)



<전역>
N 도시 수
S 숙소

도로망들.. {}

도로망
    - 도로망 번호 ( 0 무료, 1~ 유료)
    - 출발점 s (무료는 숙소)
    - s -> n1 n2 n3... 다익스 결과물 (비용 정보) list
    - 도로 정보 graph dict

도로망 진입 최소 비용 [i][j] # 도로망 i -> 도로망 j의 시작도시 최소비용

def 도로망 추가 (도로망 번호, 출발점)
    - 도로 그래프 생성
    - 도로망에 추가

def 다익스
    - 나라의 출발점 -> N개 구역 다익스

def 전체 도로망 및 도로망 진입 최소 비용 업데이트
    ** 유료는 무료로 못감!!
    1) 전체 도로망 업데이트
        for 0~k번 도로망
            도로망 다익스 및 클래스 업데이트

    2) 도로망 진입 최소 비용 업데이트
        - i 도로망 -> j 도로망 (진입 구역)

Q일 (20_000)
1. 여행할 나라 정하기 (1)
    - 100 N M s x y w x y w ..
    - N구역, M개 도로
    - 무료
    - i번 도로: x, y 구역 연결, w 시간
    - 매일 s에서 출발
    1) 도로망 추가 (다익스 여기서 안함)
    2) 전체 도로망 업데이트 (다익스 여기서 함)


2. 도로망 이용 티켓 구매 (15)
    - 200 M s x y w x y w ...
    - i번 도로: x, y 구역 연결, w 시간
    - 유료
    - 유효기간 존재
    - 번호: 티켓 구매 순서대로 1부터
    - **입구 구역 s: 여기서 출발해야 함!!
    1) 도로망 추가
    2) 전체 도로망 업데이트

3. 티켓 만료
    - 300 k (15)
    - k번째 티켓 유효기간 만료 -> [?] 도로망 자체? 도로 하나? -> 도로망!! 전체
    1) 도로망 dict에서 제거

4. 숙소 변경
    - 400 s
    - 숙소 위치(출발점 s) 변경
    1)  S 변경
    2) 전체 도로망 업데이트

5. 여행 하기
    - 500 d
    - 도착점 d까지 최단
    - 규칙
        - 유료 도로망 이용 후 무료 도로망 이용 불가
        -  유료 -> 유료 도로 변경 1회 가능
        ** 도로망은 반드시 시작 도로망의 시작 구역으로 이동해야 함
        - 무료 도로만, 유료 도로만도 가능
    - 출력: 최소 시간
        ** 이동 불가시 -1

    ** 만료된 티켓 생각하기
    ** 유료는 무료로 못감!!
    1) 유료 도로망 개수에 따라 케이스 분리
    2) 각 케이스에 대한 최소 비용 반환
    3) 각 비용들 중 최솟값 출력
    4) 없으면 -1

"""

# # 문제 1회독, 예제 확인 5m 6s
# # 문제 2회독 10m 35s
# # 설계 43m 38s
# # 상태 표 9m 10s
# # non-fail pass.
# # 총 소요시간 2h 56m 32s

# - 케이스 점검
#     - 각 <여행 케이스>가 잘 수행되는지
#     - 도착 불가할 경우 -1
#         - 유료 도로망중에 숙소!=출발점
#         - 유료 도로망이 도착점까지 가지 않음

# 여행 케이스 고려
#     - 유료 도로망 0개
#         1) 무료 하나만 (S -> 무료 -> D)
#
#     - 유료 도로망 1개
#         2) 유료 하나만 S(유료s) -> 유료 -> D
#         3) 무료 -> 유료(S -> 무료 -> 유료s -> 유료 -> D)
#
#     - 유료 도로망 2개
#         4) 무료 -> 유료 -> 유료 (S -> 무료 -> 유료s -> 유료 -> 유료s -> 유료 -> D)
#         5) 유료 -> 유료 (S(유료s)-> 유료 -> 유료s -> 유료 D)

import heapq

DEBUG = False
INF = float('inf')
Q = int(input())
N, S = -1, -1 # N 도시 수, S 숙소

streets = {} # 도로망들
street_num = 0 # 다음 도로망 번호
used = [0] # 도로망 사용 현황

# 도로망
class Street:
    def __init__(self, num, s, graph):
        self.num = num # 도로망 번호 ( 0 무료, 1~ 유료)
        self.s = s # 출발점 s (무료는 숙소)
        self.cost = [] # s -> 구역들 다익스 결과물 (비용 정보) list[b] = b 구역까지의 최단비용
        self.graph = graph # 도로 정보 graph dict {출발지 {도착지: 비용}}

# 도로망 진입 최소 비용 [i][j] # 도로망 i -> 도로망 j의 시작도시 최소비용
low_costs = []

# 전역 입력 7m 27s

# 도로망 추가 (출발점, 도로 개수, 도로 정보)
def add_street(s, m, line): # 17m 56s
    global street_num

    # 1. 도로 그래프 생성 graph dict {출발지 {도착지: 비용}}
    graph = {}

    for idx in range(m):
        x, y, w = line[idx*3: (idx+1)*3]

        if x not in graph: graph[x] = {}
        if y not in graph: graph[y] = {}

        if y not in graph[x]:
            graph[x][y] = w
            graph[y][x] = w
        # 한 도로망에서 출발지 - 도착지 도로가 여러개일 경우, 최소 비용으로 업데이트
        else:
            min_w = min(w, graph[x][y])
            graph[x][y] = min_w
            graph[y][x] = min_w

    # 2) 도로망에 추가
    streets[street_num] = Street(street_num, s, graph)
    street_num += 1

# 다익스트라: 도로망 시작점 -> N개 도시 최단 비용
# return cost... cost[b] = b 구역까지의 최단비용
def get_street_costs(s, graph):
    costs = [INF]*(N+1)
    costs[s] = 0
    q = [(0, s)] # 비용 최소, 도시 정보

    while q:
        cur_cost, cur_city = heapq.heappop(q)

        if cur_city!=s and cur_cost >= costs[cur_city]:
            continue

        costs[cur_city] = cur_cost

        for next_city, next_cost in graph[cur_city].items():

            if costs[next_city] > cur_cost + next_cost:
                heapq.heappush(q, (cur_cost + next_cost, next_city))

    return costs

#  전체 도로망 및 도로망 진입 최소 비용 업데이트
# ** 유료는 무료로 못감!!
def update_all_streets(): # 26m 44s
    global low_costs

    # 1) 전체 도로망 업데이트
    for street in streets.values():
        # 도로망 다익스 및 클래스 업데이트
        street_costs = get_street_costs(street.s, street.graph)
        street.costs = street_costs

    # 2) 도로망 진입 최소 비용 업데이트
    # i 도로망 -> j 도로망 (진입 구역)
    lc = [[INF]*street_num for _ in range(street_num)]
    for a in streets.values():
        for b in streets.values():
            if a.num == b.num: lc[a.num][b.num] = 0
            elif a.num!=0 and b.num==0: continue   # 유료 -> 무료 불가
            else:
                sb = b.s
                lc[a.num][b.num] = a.costs[sb]

    low_costs = lc

# 여행 하기
# - 도착점 d까지 최단
# - 규칙
#     - 유료 도로망 이용 후 무료 도로망 이용 불가
#     -  유료 -> 유료 도로 변경 1회 가능
#     ** 도로망은 반드시 시작 도로망의 시작 구역으로 이동해야 함
#     - 무료 도로만, 유료 도로만도 가능
# - 출력: 최소 시간
#     ** 이동 불가시 -1
#
# ** 만료된 티켓 생각하기
#     ** 유료는 무료로 못감!!
# =========================================
def travel(d):
    # [1] 유료 도로망 개수에 따라 케이스 분리
    # [2] 각 케이스에 대한 최소 비용 반환

    # - 유료 도로망 0개 이상
    #     1) 무료 하나만 (S -> 무료 -> D)
    cases = [streets[0].costs[d]]

    # - 유료 도로망 1개 이상 (총 도로망 2개 이상)
    #     2) 유료 하나만 S(유료s) -> 유료 -> D
    #     3) 무료 -> 유료(S -> 무료 -> 유료s -> 유료 -> D)
    if len(streets) >= 2:
        for street in streets.values():
            if street.num == 0 : continue
            if street.s == S: cases.append(street.costs[d])
            cases.append( low_costs[0][street.num] + street.costs[d] )

    # - 유료 도로망 2개 이상
    #     4) 무료 -> 유료 -> 유료 (S -> 무료 -> 유료s -> 유료 -> 유료s -> 유료 -> D)
    #     5) 유료 -> 유료 (S(유료s)-> 유료 -> 유료s -> 유료 D)
    if len(streets) >= 3:
        #  (무료 ->) a -> b
        for a_street in streets.values():
            if a_street.num == 0 : continue
            for b_street in streets.values():
                if b_street.num == 0: continue
                if a_street.num == b_street.num: continue

                # a -> b 진입 비용
                cost_a_to_b = low_costs[a_street.num][b_street.num]
                if cost_a_to_b == INF: continue
                cost_a_b_end =  cost_a_to_b + b_street.costs[d]

                if a_street.s == S: cases.append(cost_a_b_end)
                cases.append(low_costs[0][a_street.num] + cost_a_b_end)

    return min(cases)

def main():
    global N, S
    answer = []
    for _ in range(Q):
        cmd, *line = map(int, input().split())

        # =========================================
        # 1. 여행할 나라 정하기
        #     - 100 N M s x y w x y w ..
        #     - N구역, M개 도로
        #     - 무료
        #     - i번 도로: x, y 구역 연결, w 시간
        #     - 매일 s에서 출발
        # =========================================
        if cmd == 100:
            N, m, S = line[:3]

            # 1) 도로망 추가 (다익스 여기서 안함)
            add_street(S, m, line[3:])
            # 2) 전체 도로망 업데이트 (다익스 여기서 함)
            update_all_streets()

        # =========================================
        # 2. 도로망 이용 티켓 구매 # 5m 32s (사실상 add_street, update_all_streets 디버깅 시간)
        # - 200 M s x y w x y w ...
        # - i번 도로: x, y 구역 연결, w 시간
        # - 유료
        # - 유효기간 존재
        # - 번호: 티켓 구매 순서대로 1부터
        # - **입구 구역 s: 여기서 출발해야 함!!
        # =========================================
        elif cmd == 200:
            m, s = line[:2]
            # 1) 도로망 추가
            add_street(s, m, line[2:])
            # 2) 전체 도로망 업데이트
            update_all_streets()

        # =========================================
        # 3. 티켓 만료 00:44
        # =========================================
        elif cmd == 300:
            # 1) 도로망 dict에서 제거
            del streets[line[0]]

        # =========================================
        # 4. 숙소 변경 2:00
        # =========================================
        elif cmd == 400:
            # 1) S 변경
            S = line[0]
            streets[0].s = S # 해당 부분추가 놓쳐서 디버깅 3m 51s
            # 2) 전체 도로망 업데이트
            update_all_streets()

        # =========================================
        # 5. 여행 하기 43 48s
        # - 500 d
        # - 도착점 d까지 최단
        # - 규칙
        #     - 유료 도로망 이용 후 무료 도로망 이용 불가
        #     -  유료 -> 유료 도로 변경 1회 가능
        #     ** 도로망은 반드시 시작 도로망의 시작 구역으로 이동해야 함
        #     - 무료 도로만, 유료 도로만도 가능
        # - 출력: 최소 시간
        #     ** 이동 불가시 -1
        #
        # ** 만료된 티켓 생각하기
        #     ** 유료는 무료로 못감!!
        # =========================================
        elif cmd == 500:
            min_cost = travel(line[0])
            answer.append(min_cost if min_cost!=INF else -1) # 없으면 -1

        if DEBUG: print()
    print('\n'.join(map(str, answer)))

main()