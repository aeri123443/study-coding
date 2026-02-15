'''
49189. Lv.3 가장 먼 노드
https://school.programmers.co.kr/learn/courses/30/lessons/49189
11m
'''
from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    dist = [-1] * (n+1)

    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    
    q = deque( [1] )
    dist[1] = 0

    # bfs
    while q:
        v = q.popleft()

        for neighbor in graph[v]:
            if dist[neighbor] < 0:
                dist[neighbor] = dist[v]+1
                q.append(neighbor)

    # 최대 거리 확인
    max_dist = max(dist)

    return len([x for x in dist if x==max_dist])

print()
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(3)