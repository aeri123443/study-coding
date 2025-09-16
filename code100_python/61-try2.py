'''
p.579 61. 지형 이동
https://school.programmers.co.kr/learn/courses/30/lessons/62050
다익스트라를 떠올렸을 때 heapq를 활용한 bfs를 떠올렸어야 함
'''
import pprint
import time

import heapq

def is_move(x, y):
    global visited, N
    return x >= 0 and y >= 0 and x < N and y < N and visited[x][y]==False

def solution(land, height):
    global visited, N
    N = len(land)
    answer = 0
    move = [[0,1], [0,-1], [1,0], [-1,0]]
    visited = [[False]*N for _ in range(N)]
    q = []
    heapq.heappush(q, [0, 0, 0])
    while q:
        # time.sleep(0.5)
        cost, x, y = heapq.heappop(q)
        # print(cost, x, y)

        if visited[x][y]==True: continue
        answer += cost

        visited[x][y] = True
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if is_move(nx, ny):
                if abs(land[nx][ny] - land[x][y]) <= height:
                    w = 0
                else:
                    w = abs(land[nx][ny] - land[x][y])
                heapq.heappush(q, [w, nx, ny])
    # pprint.pprint(visited)
    return answer
            

# 15
print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
# 18
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
# 30
print(solution([[1,3,5,7], [15,13,11,9], [17,19,21,23], [31,29,27,25]], 1))
