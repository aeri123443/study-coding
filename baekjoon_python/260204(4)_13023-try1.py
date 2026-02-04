'''
13023. <골드 5> ABCDE
https://www.acmicpc.net/problem/13023
'''

import sys
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# pprint(graph)

visited = [False] * N
def dfs(s_node, depth):
    # print(visited, depth)
    if depth==4:
        return True
    
    for nxt in graph[s_node]:
        if not visited[nxt]:
            visited[nxt] = True
            result = dfs(nxt, depth+1)
            if not result:
                visited[nxt] = False
            else:
                return True

flag = False
for i in range(N):
    visited[i] = True
    result = dfs(i, 0)
    if result:
        flag = True
        break
    visited[i] = False

print(1) if flag else print(0)