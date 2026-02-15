'''
12978. Lv.2 배달
https://school.programmers.co.kr/learn/courses/30/lessons/12978
24m 29s
'''
import heapq

def solution(N, road, K):
    INF = float('inf')
    graph = [[] for _ in range(N+1)]
    cost = [INF]*(N+1)

    # 그래프 담기
    for a, b, c in road:
        # print(a,b,c)
        graph[a].append([b, c]) # 다음노드, 노드 간 거리
        graph[b].append([a, c]) 
    # print(graph)

    # 시작노드
    q = [(0, 1)] # 비용, 정점
    cost[1] = 0

    while q:
        c, node = heapq.heappop(q) # 비용, 정점

        if c > cost[node]:
            continue
        

        for neighbor, e in graph[node]:
            # print(node, neighbor, e)
            if cost[node]+e < cost[neighbor]:
                cost[neighbor] = cost[node]+e
                heapq.heappush(q, (cost[node]+e, neighbor))

    return len([c for c in cost if c <= K])

print()
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(4)

print()
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
print(4)

# print()
# print(solution())
# print()