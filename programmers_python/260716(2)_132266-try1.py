'''
132266. 부대복귀
https://school.programmers.co.kr/learn/courses/30/lessons/132266

문제 분석 & 코드 작성: 22m 08s
디버깅: 0m 0s
total: 22m 08s
'''
from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    # 그래프 만들기
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 최단경로 알고리즘
    visited = [-1]*(n+1)
    visited[destination] = 0
    q = deque([destination]) # [노드, 그 노드까지의 비용]

    while q:
        node = q.popleft()
        cost = visited[node]

        for nxt in graph[node]:
            if visited[nxt] == -1:
                visited[nxt] = cost+1
                q.append(nxt)

    return [ visited[s] for s in sources]

# [1, 2]
print(solution(3,	[[1, 2], [2, 3]],	[2, 3],	1))
# [2, -1, 0]
print(solution(5,	[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],	[1, 3, 5],	5))
