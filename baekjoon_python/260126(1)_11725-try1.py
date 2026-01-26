'''
11725. <실버 2> 트리의 부모 찾기
https://www.acmicpc.net/problem/11725
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# 그래프 생성 및 입력
graph = {i+1:set() for i in range(N)}
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
# print(graph)

# 부모 찾기
parents = [-1]*(N+1)

parents[1] = 0
q=deque()
q.append(1)

while q:
    node = q.popleft()
    for child in graph[node]:
        if parents[child] < 0:
            parents[child] = node
            q.append(child)
# print(parents)

# 최종 출력
print('\n'.join(map(str, parents[2:])))