'''
p.446 43. 네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
dfs로 풀어보기
'''

def dfs(visited, name, computers):
    visited[name] = True
    for i in range(len(computers)):
        if computers[name][i]==1 and not visited[i]:
            dfs(visited, i, computers)

def solution(n, computers):

    cnt = 0
    visited = [False]*n

    for i in range(n):
        # print(i)
        if not visited[i]:
            cnt += 1
            dfs(visited, i, computers)

    return cnt

# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# 2
print(solution(5, [[1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [0,0,0,1,1], [0,0,0,1,1]]))
# 4
print(solution(5, [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]))
