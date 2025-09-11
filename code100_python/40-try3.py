'''
p.432 40. 다익스트라 알고리즘
heapq 활용해보기
9/11 오후 복습
'''

import heapq

def solution(graph, start):
    # distance, path 초기화 
    distance = {g:float('inf') for g in graph}
    paths = {g:[] for g in graph}
    distance[start] = 0
    paths[start] = [start]

    q = []
    heapq.heappush(q, [0, start])
    while q:
        recent_distance, recent_node = heapq.heappop(q)

        if recent_distance > distance[recent_node]:
            continue

        # 다음 노드에 대하여
        for next_node in graph[recent_node]:
            new_distance = recent_distance + graph[recent_node][next_node]
            # 최소 거리 비교 후 업데이트
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                paths[next_node] = [*paths[recent_node], next_node]
                heapq.heappush(q, [new_distance, next_node])

    return [distance, paths]

# [{'A': 0, 'B': 4, 'C': 3}, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}]
print(solution({ 'A': { 'B': 9, 'C': 3 }, 'B': { 'A': 5 }, 'C': { 'B': 1 } }, 'A'))
# [{'A': 0, 'B': 1, 'C': 6, 'D': 7}, {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']}]
print(solution({ 'A': { 'B': 1 },'B': { 'C': 5 },'C': { 'D': 1 }, 'D': {} }, 'A'))
