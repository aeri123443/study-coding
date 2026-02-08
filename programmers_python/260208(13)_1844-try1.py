'''
1844. lv2 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
11m 46s
'''

from pprint import pprint
from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[0]*M for _ in range(N)]
    move = [(0,1), (0,-1), (1,0),  (-1,0)]

    q = deque()
    q.append( (0,0) )
    visited[0][0] = 1

    while q:
        ci, cj = q.popleft()

        if ci==N-1 and cj==M-1:
            return visited[ci][cj]
        
        for di, dj in move:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and maps[ni][nj]==1:
                visited[ni][nj] = visited[ci][cj]+1
                q.append( (ni,nj) )

    # pprint(visited)
    return -1

print()
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(11)

print()
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(-1)
