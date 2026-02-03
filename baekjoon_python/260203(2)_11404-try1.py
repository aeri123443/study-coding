'''
11404. <골드 4> 플로이드
https://www.acmicpc.net/problem/11404
'''

import sys
from pprint import pprint
# from collections import deque
import heapq

input = sys.stdin.readline

N, M = int(input()), int(input())
# graph {시작버스: {도착버스: 비용}}
graph = {i:{} for i in range(1, N+1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min( graph[a][b], c )
    else:
        graph[a][b] = c

# pprint(graph)

def costs_by_start_bus(s_city):
    costs = [float('inf')]*(N+1)
    # q = deque()
    q = []
    # q.append([s_city, 0]) # 출발 버스, 누적 비용
    heapq.heappush(q, (0, s_city) )
    costs[s_city] = 0

    while q:
        # cur_bus, cur_cost = q.popleft()
        cur_cost, cur_bus = heapq.heappop(q)
        # print(cur_cost, costs[cur_bus])
        if cur_cost > costs[cur_bus]:
            continue

        # print(graph[cur_bus])
        for nxt_city, bus_cost in graph[cur_bus].items():
            # print(nxt_city, bus_cost)
            nxt_cost = cur_cost + bus_cost
            if nxt_cost < costs[nxt_city]:
                costs[nxt_city] = nxt_cost
                # q.append([nxt_city, nxt_cost])
                heapq.heappush(q, (nxt_cost, nxt_city))

    for i in range(1, N+1):
        if costs[i]==float('inf'):
            costs[i] = 0

    print(' '.join(map(str, costs[1:])))

for i in range(1, N+1):
    costs_by_start_bus(i)
