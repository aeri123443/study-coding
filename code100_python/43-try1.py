'''
p.446 43. 네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
소요시간: 28m 38s
'''

from collections import deque

def solution(n, computers):
    non_visited = {i for i in range(n)}
    visited = {}
    cnt = 0

    def bfs(computers, start):
        q = deque([start])
        visited = set([start])
        while q:
            node = q.popleft()
            for name, connected in enumerate(computers[node]):
            #    print(name, connected)
               if connected==1 and not name in visited:
                   q.append(name)
                   visited.add(name) 
        return visited
    
    while non_visited:
        cnt += 1
        start = non_visited.pop()
        visited = bfs(computers, start)
        non_visited = non_visited-visited
    return cnt

# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# 2
print(solution(5, [[1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [0,0,0,1,1], [0,0,0,1,1]]))
# 4
print(solution(5, [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]))
