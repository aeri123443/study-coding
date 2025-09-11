'''
p.456 44. 배달
https://school.programmers.co.kr/learn/courses/30/lessons/12978
소요시간: 26m 26s
'''

import heapq

def solution(N, road, K):
    # distance, recent 초기화
    distance = {i+1:float('inf') for i in range(N)}
    recent = {i+1:[] for i in range(N)}
    distance[1] = 0
    recent[1] = 1

    # 그래프 생성
    # 두 값일 경우 작은 값 넣기
    graph = {i+1:{} for i in range(N)}
    for a, b, dis in road:
        if a in graph[b]:
            graph[a][b] = min(dis, graph[a][b])
            graph[b][a] = min(dis, graph[a][b])
        else:
            graph[a][b] = dis
            graph[b][a] = dis
    # print(graph)
    
    # 다익스트라
    q = []
    heapq.heappush(q, [0, 1]) # 거리, 노드

    while q:
        recent_distance, recent_node = heapq.heappop(q)

        if recent_distance > distance[recent_node]:
            continue

        for next_node in graph[recent_node]:
            new_distance = recent_distance + graph[recent_node][next_node]
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                recent[next_node] = recent_node
                heapq.heappush(q, [new_distance, next_node])
    # print(distance)
    # print(recent)

    # K 이하값 추출, 카운트
    answer = [k for k,v in distance.items() if v<=K]
    return len(answer)

# 4
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print()
# 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
