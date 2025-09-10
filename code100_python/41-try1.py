'''
p.442 41. 벨만-포드 알고리즘
'''

def solution(graph, source):
    n = len(graph)
    distance = [float('inf')]*n
    recent = [None]*n
    distance[source]=0

    for _ in range(n-1):
        for i in range(n):
            for (next_node, next_weight) in graph[i]:
                new_distance = distance[i] + next_weight
                if new_distance < distance[next_node]:
                    distance[next_node] = new_distance
                    recent[next_node] = i
        # print('distance', distance)
        # print('recent', recent)
        # print()

    # 음의 가중치 순회 체크
    for i in range(n):
        for (next_node, next_weight) in graph[i]:
            new_distance = distance[i] + next_weight
            # 여기서 또 작아지면 순회하고 있다는 뜻
            if new_distance < distance[next_node]:
                return [-1]

    return [distance, recent]

# [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
print(solution([[[1, 4], [2, 3], [4, -6 ]], [[3, 5]], [[1, 2]], [[0, 7], [2, 4]], [[2, 2]]], 0))
# [-1]
print(solution([[[1, 5], [2, -1]], [[2, 2]], [[3, -2]], [[0, 2], [1, 6]]], 0))
