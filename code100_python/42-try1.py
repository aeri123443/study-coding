'''
p.446 42. 게임 맵 최단 거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
소요시간: 26m +a
'''

from collections import deque

def solution(maps):
    x_max, y_max = len(maps), len(maps[0])
    print(x_max, y_max)
    visited = [[-1]*y_max for _ in range(x_max)]
    visited[0][0]=1
    q = deque()
    q.append([0, 0])
    x, y = 0, 0

    while q:
        x, y = q.popleft()
        # print(x, y)
        if x==x_max-1 and y==y_max-1: 
            return visited[x][y]

        if x+1<x_max and visited[x+1][y]<0 and maps[x+1][y]==1:
            visited[x+1][y] = visited[x][y]+1
            q.append([x+1, y])
        if y+1<y_max and visited[x][y+1]<0 and maps[x][y+1]==1:
            visited[x][y+1] = visited[x][y]+1
            q.append([x, y+1])
        if x-1>=0 and visited[x-1][y]<0 and maps[x-1][y]==1:
            visited[x-1][y] = visited[x][y]+1
            q.append([x-1, y])
        if y-1>=0 and visited[x][y-1]<0 and maps[x][y-1]==1:
            visited[x][y-1] = visited[x][y]+1
            q.append([x, y-1])

    return -1

# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
# 21
print(solution([[1,0,1,1,1,1,0],[1,0,1,0,0,1,0],[1,0,1,1,0,1,0],[1,0,0,1,0,1,0],[1,1,1,1,0,1,1]]))
