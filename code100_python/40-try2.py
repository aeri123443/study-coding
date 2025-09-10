'''
p.432 40. 다익스트라 알고리즘
heapq 활용해보기
9/11 memo: 복습 필요 !!
'''

import heapq

def solution(graph, start):
    distance = { g:float('inf') for g in graph}
    distance[start] = 0
    path={start: [start]}

    q = []
    heapq.heappush(q, [start, 0])

    while q:
        pop_node, pop_distance = heapq.heappop(q)

        if pop_distance > distance[pop_node]:
            continue

        for next_node in graph[pop_node]:
            new_distance = pop_distance + graph[pop_node][next_node]
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                path[next_node] = [*path[pop_node], next_node]
                heapq.heappush(q, [next_node, new_distance])

    # print('distance', distance)
    # print('path', path)
    return [distance, path]

# [{'A': 0, 'B': 4, 'C': 3}, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}]
print(solution({ 'A': { 'B': 9, 'C': 3 }, 'B': { 'A': 5 }, 'C': { 'B': 1 } }, 'A'))
# [{'A': 0, 'B': 1, 'C': 6, 'D': 7}, {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']}]
print(solution({ 'A': { 'B': 1 },'B': { 'C': 5 },'C': { 'D': 1 }, 'D': {} }, 'A'))
