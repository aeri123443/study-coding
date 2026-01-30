'''
1967. <골드 4> 트리의 지름
https://www.acmicpc.net/problem/1967
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 시작노드 : [[끝 노드, 가중치]]
graph = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])

def bfs(s_node):
    max_node, max_cost = -1, -1
    visited = [False]*(n+1)
    # cnt = 0 # 디버깅: 탐색 횟수
    q = deque()
    # 출발 노드, 축적 비용
    q.append([s_node, 0])
    # print(s_node)
    visited[s_node] = True

    while q:
        cur_node, cur_cost = q.popleft()
        # cnt += 1
        # print(cnt, cur_node, cur_cost)

        if max_cost < cur_cost:
            max_cost = cur_cost
            max_node = cur_node

        for nxt_node, w in graph[cur_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                q.append([nxt_node, w+cur_cost])

    # print(cnt, visited)
    return max_node, max_cost

# 아무거나 잡고 가장 멀리 가봄
max_node, max_cost = bfs(1)

# 거기서부터 다시 멀리 가봄
max_node, max_cost = bfs(max_node)

print(max_cost)