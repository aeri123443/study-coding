'''
43162. lv3 네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
20m 56s

- 이미 인접 행렬이 있으니 굳이 인접리스트를 만들 필요가 없음
- visited 자체가 수정되는 것이 아니므로 nonlocal 필요 없음
'''

from pprint import pprint
from collections import deque

def solution(n, computers):
    
    graph = [ [] for _ in range(n)] 
    visited = [False]*n

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]==1:
                graph[i].append(j)

    # pprint(graph)

    def bfs(s):
        nonlocal visited

        q = deque()
        q.append(s)
        visited[s] = True

        while q:
            cur = q.popleft()

            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)

    return answer

print()
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(2)

print()
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(1)

print()
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(3)

print()
print(solution(5, [[1,0,1,0,0], [0,1,0,1,0], [1,0,1,0,1], [0,1,0,1,0], [0,0,1,0,1]]))
print(2)

print()
print(solution(5, [[1,0,1,0,1], [0,1,0,1,0], [1,0,1,0,1], [0,1,0,1,0], [1,0,1,0,1]]))
print(2)

print()
print(solution(5, [[1,0,1,0,1], [0,1,0,1,0], [1,0,1,0,1], [0,1,0,1,1], [1,0,1,1,1]]))
print(1)

# print(solution())
# print()
