'''
11724. <실버2> 연결 요소의 개수
https://www.acmicpc.net/problem/11724
bfs로 풀어보기!
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = {(i+1):set() for i in range(N)}
visited = [False]*(N+1)
answer = 0

# 쭉쭉 탐색
def bfs(start_node):
    q = deque()
    q.append(start_node)
    visited[start_node] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


# u, v에 대하여 양방향 간선 딕셔너리
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
# print(graph)
# print(len(graph[6]))

# 방문 안한 애들 탐색
for i in range(1, N+1):
    if not visited[i]:
        answer+=1
        visited[i]=True
        bfs(i)

print(answer)
