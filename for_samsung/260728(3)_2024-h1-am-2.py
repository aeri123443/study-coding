'''
코드트리 투어: 2024 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-tour/description

문제 분석: 29m 27s
  - [시간 소요] 최단 거리 알고리즘의 사용과, 500 출발지 변경에서 아예 q를 리셋하는 방향이 시간복잡도에서 문제가 될지 점검 후 코드 작성에 들어감
코드 1차 작성: 1h 7m 39s
  - [시간 소요] 처음엔 그래프를 {a: {b1:w1, b2:w2}, ...} 이런 식으로 최단 간선을 업데이트 하고 싶었는데, 그게 잘 안 되어서 그냥 리스트로 직진함
최종 디버깅: 0m 0s

총 소요 시간: 1h 37m 7s
'''

import heapq
from collections import defaultdict

##########################################################
#### 전역 변수 및 클래스
##########################################################

INF = float('inf')
Q, N, M = -1, -1, -1
items = {} # 관리중인 상품 목록
item_q = [] # 관리중인 상품 큐
distance = [] # 거리 배열
graph = defaultdict(list)

class Item:
    def __init__(self, num, r, d):
        self.num = num
        self.r = r
        self.d = d

##########################################################
#### 보조 함수
##########################################################
def cal_distance(s_node):
    # 거리 초기화
    for i in range(N):
        distance[i] = INF

    q = []
    heapq.heappush(q, (0, s_node)) # 비용, 다음 출발지
    distance[s_node] = 0

    while q:
        cost, node = heapq.heappop(q)

        if 0 < cost >= distance[node]:
            continue

        distance[node] = cost

        for neighbor, w in graph[node]:
            new_cost = cost+w
            if new_cost < distance[neighbor]:
                heapq.heappush(q, (new_cost, neighbor))

# 상품을 큐에 추가
def add_item_in_q(item):
    # num, r, d = line[1:]
    # item = Item(num, r, d)
    num, r, d = item.num, item.r, item.d
    # 이득이 발생할 경우, 상품 목록과 상품 큐에 모두 넣음
    # 이득이 발생하지 않을 경우, 상품 목록에만 넣음
    if distance[d] <= r:
        heapq.heappush(item_q, (distance[d] - r, num))  # -이득, 상품 번호
    # items[num] = item

# item_q 리셋
def reset_q():
    global item_q

    item_q = []
    for num, item in items.items():
        add_item_in_q(item)


##########################################################
#### 메인 로직
##########################################################

def main():
    global Q, N, M, distance, item_q

    Q = int(input())
    answer = []

    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 초기 건설
        if cmd == 100:
            N, M = line[1], line[2]
            distance = [INF]*N

            # 그래프 생성
            for i in range(M):
                idx = 3 + i*3
                a, b, w = line[idx:idx+3]
                # 자기 자신으로 돌아오는 경우, 어차피 최단에서 제외되므로 그래프에 나타내지 않음.
                if a == b: continue
                # 이미 동일한 목적지가 존재할 때에는 일단 넣고 향후 처리
                graph[a].append([b, w])
                graph[b].append([a, w])

            # 거리 맵 초기화
            cal_distance(0)
        # 상품 생성
        elif cmd == 200:
            num, r, d = line[1:]
            item = Item(num, r, d)
            # 이득이 발생할 경우, 상품 목록과 상품 큐에 모두 넣음
            # 이득이 발생하지 않을 경우, 상품 목록에만 넣음
            # if distance[d] <= r:
            #     heapq.heappush(item_q, (distance[d]-r, num)) # -이득, 상품 번호
            items[num] = item
            add_item_in_q(item)
        # 상품 취소
        elif cmd == 300:
            num = line[1]
            if num in items:
                del items[num]
        # 최적 상품
        elif cmd == 400:

            result_id = -1
            while item_q:
                rev_b, num =  heapq.heappop(item_q)
                b = -rev_b

                # 존재하는 상품이면 반환
                # 삭제된 번호면 다시 뽑음
                if num in items:
                    result_id = num
                    del items[num] # 해당 상품을 제거
                    break

            answer.append(str(result_id))

        # 상품 출발지 변경
        elif cmd == 500:
            s = line[1]
            # 거리 재계산
            cal_distance(s)
            # item_q 리셋
            reset_q()
        # print()
    print('\n'.join(answer))

main()