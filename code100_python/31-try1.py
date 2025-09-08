'''
p.334 31. 양과 늑대
https://school.programmers.co.kr/learn/courses/30/lessons/92343
소요시간: 86m 22s
'''

from collections import deque

def solution(info, edges):
    # 그래프 만들기
    graph = {}
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

    # bfs
    q = deque()
    q.append([0, 1, 0, [0]])
    all_sheeps = [i for i in info if i==0]
    all_sheeps = len(all_sheeps)

    max_sheeps = 1
    while q:
        num, sheep, wolf, visited = q.popleft()
        max_sheeps = max(max_sheeps, sheep)
        if max_sheeps == all_sheeps: return all_sheeps
        # print(num, sheep, wolf, visited)
        new_visited = [*visited]
        new_visited.remove(num)
        if num in graph: 
            new_visited.update(graph[num])
        
        for v in new_visited:
            # 양일 경우
            if info[v]==0:
                q.append([v, sheep+1, wolf, new_visited])
            # 늑대일 경우
            else:
                if sheep > wolf+1:
                    q.append([v, sheep, wolf+1, new_visited])
        
    return max_sheeps

# print(solution([0,0,1,1,1,0,0], [[0,1], [0,4], [1,2], [1,3], [4,5], [4,6]]))

# 5
print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
