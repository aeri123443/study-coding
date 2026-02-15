'''
67259. Lv.3 [카카오 인턴] 경주로 건설
https://school.programmers.co.kr/learn/courses/30/lessons/67259
39m 15s
'''
from pprint import pprint
import heapq

def solution(board):
    # board... 0: 비어 있음 1:벽 
    N = len(board)
    INF = float('inf')
    visited = [[[INF, INF] for _ in range(N)] for _ in range(N)] # [직진, 코너]
    move = [(1,0,1), (-1,0,1), (0,1,0), (0,-1,0)] # 가로r:0, 세로c:1

    q = [] # 비용, 온 방향, i, j
    heapq.heappush( q, (0,0,0,0) ) # 가로 방향
    heapq.heappush( q, (0,1,0,0) ) # 세로 방향
    visited[0][0]=[0, 0]

    while q:
        cost, direct, ci, cj = heapq.heappop(q)

        if cost > visited[ci][cj][direct]:
            continue

        for di, dj, dd in move:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and board[ni][nj]==0:
                # 직선 도로 100원, 코너 100+500=600원
                new_cost = cost + (100 if direct==dd else 600)
                if new_cost < visited[ni][nj][dd]:
                    visited[ni][nj][dd] = new_cost
                    heapq.heappush(q,  (new_cost, dd, ni, nj))

    # pprint(visited)
    return min(visited[-1][-1])

print()
print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(900)

print()
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(3800)

print()
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(2100)

print()
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
print(3200)

# print()
# print(solution())
# print()
