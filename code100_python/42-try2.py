'''
p.446 42. 게임 맵 최단 거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
소요시간: 이동시 반복문 사용해보기
'''

from collections import deque

def solution(maps):
    x_max, y_max = len(maps), len(maps[0])
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    visited = [[-1]*y_max for _ in range(x_max)]
    visited[0][0]=1
    q = deque()
    q.append([0, 0])

    while q:
        x, y = q.popleft()
        # print(x, y)
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
            if nx>=0 and nx<x_max and ny>=0 and ny<y_max:
                if visited[nx][ny]<0 and maps[nx][ny]==1:
                    visited[nx][ny] = visited[x][y]+1
                    q.append([nx, ny])

    return visited[x_max-1][y_max-1]

# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
# 21
print(solution([[1,0,1,1,1,1,0],[1,0,1,0,0,1,0],[1,0,1,1,0,1,0],[1,0,0,1,0,1,0],[1,1,1,1,0,1,1]]))
