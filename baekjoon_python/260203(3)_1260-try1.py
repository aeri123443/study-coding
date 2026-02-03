'''
1260. <실버 2> DFS와 BFS
https://www.acmicpc.net/problem/1260
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 그래프 입력 및 내부 정렬
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
# print(graph)

def bfs(s_node):
    visited = [False]*(N+1)
    visit_step = []
    
    q = deque()
    q.append(s_node)
    visited[s_node] = True
    visit_step.append(s_node)

    while q:
        cur_node = q.popleft()

        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                q.append(nxt_node)
                visit_step.append(nxt_node)

    print(' '.join(map(str, visit_step)))

def dfs(s_node):
    visited = [False]*(N+1)
    visit_step = []
    
    stack = []
    stack.append(s_node)

    while stack:
        cur_node = stack.pop()

        if visited[cur_node]:
            continue

        visited[cur_node] = True
        visit_step.append(cur_node)

        # 그래프 역순으로
        for i in range(len(graph[cur_node])-1, -1, -1):
            nxt_node = graph[cur_node][i]
            if not visited[nxt_node]:
                stack.append(nxt_node)

    print(' '.join(map(str, visit_step)))
    
dfs(V)
bfs(V)