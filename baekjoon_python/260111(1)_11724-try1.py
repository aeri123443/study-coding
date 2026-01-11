'''
11724. <실버2> 연결 요소의 개수
https://www.acmicpc.net/problem/11724
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {(i+1):set() for i in range(N)}
visited = [False]*(N+1)
answer = 0

# 쭉쭉 탐색
# i: 노드명(1~N)
def grouping(i):
    global visited, graph
    # 다음 노드 찾기
    for next_node in graph[i]:
        # 방문하지 않은 노드면
        if not visited[next_node]:
            # 이 노드 탐색한다
            visited[next_node] = True
            grouping(next_node)
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
        grouping(i)

print(answer)
