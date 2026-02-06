'''
18352. <실버 2> 특정 거리의 도시 찾기
https://www.acmicpc.net/problem/18352
'''

import sys
from pprint import pprint
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
costs = [float('inf')]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# pprint(graph)

q = []
costs[X] = 0
heapq.heappush(q, [0, X]) # cost, node

while q:
    cost, node = heapq.heappop(q)

    if cost > costs[node]:
        continue

    for neighbor in graph[node]:
        if cost + 1 < costs[neighbor]:
            costs[neighbor] = cost + 1
            heapq.heappush(q, [cost+1, neighbor])

answer = []
for i in range(1,N+1):
    if costs[i] == K:
        answer.append(i)

# print(costs, answer)
print( '\n'.join(map(str, answer)) if answer else -1 )
