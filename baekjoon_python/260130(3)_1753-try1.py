'''
1753. <골드 4> 최단경로
https://www.acmicpc.net/problem/1753
'''

import sys
from pprint import pprint
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
si = int(input())
graph = {i+1:[] for i in range(V)}
memo = [[float('inf'), -1] for _ in range(V+1)] # cost, parents

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v,w])

# q = deque()
q = []
heapq.heappush(q, [0, si])
memo[si] = [0,0]

while q:
    cost, node = heapq.heappop(q)
    # print(node, cost)
    # print(cost , memo[node][0])
    if cost > memo[node][0]:
        continue 

    for n, w in graph[node]:
        new_cost = cost+w
        if new_cost < memo[n][0]:
            memo[n] = [new_cost, node]
            heapq.heappush(q, [new_cost, n])

for i in range(1,V+1):
    if memo[i][0]==float('inf'):
        print('INF')
    else:
        print(memo[i][0])

