'''
1916. <골드 5> 최소비용 구하기
https://www.acmicpc.net/problem/1916

개선 포인트:
다익스트라는 정점이 pop되는 순간 최단거리기 때문에,
c_city에서 e가 뽑히면 바로 탐색 종료해도 됨!!
'''
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V = int(input())
E = int(input())
INF = float('inf')

graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append( (b,c) )

s, e = map(int, input().split())
costs = [INF]*(V+1)
q = []

costs[s] = 0
heapq.heappush(q, (0, s)) # (그 도시까지 걸린 비용, 도시)

while q:
    c_cost, c_city = heapq.heappop(q)

    if c_cost > costs[c_city]: 
        continue

    for n_city, bus in graph[c_city]:
        n_cost = c_cost + bus
        if costs[n_city] > n_cost:
            
            costs[n_city] = n_cost
            heapq.heappush(q, (n_cost, n_city))
        # print(c_city, c_cost, n_city, bus, costs)
print(costs[e])