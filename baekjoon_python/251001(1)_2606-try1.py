'''
2606. <실버3> 바이러스
https://www.acmicpc.net/problem/2606
'''
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

N = int(input())
M = int(input())
graph = {i+1:[] for i in range(N)}

# 그래프 만들기 /리스트 포함
for i in range(M):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

# pprint(graph)

# 1부터 bfs 시작, cnt 누적
q = deque()
q.append(1)
visited = [False] * (N+1)
visited[1] = True
cnt = 0

while q:
    num = q.popleft()

    for child in graph[num]:
        if visited[child]:
            continue
        visited[child] = True
        q.append(child)
        cnt += 1

print(cnt)


