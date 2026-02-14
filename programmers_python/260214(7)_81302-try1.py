'''
81302. Lv. 2 거리두기 확인하기
https://school.programmers.co.kr/learn/courses/30/lessons/81302
33m 20s
'''
from pprint import pprint
from collections import deque

def solution(places):
    N = 5
    move = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = []
    answer = []

    for place in places:
        s_list = []
        for i in range(N):
            for j in range(N):
                if place[i][j] == 'P':
                    s_list.append((i,j))

        # print(s_list)
        
        # BFS
        is_breaked = False
        for si, sj in s_list:

            visited = [[0]*5 for _ in range(N)]
            visited[si][sj]=1
            q = deque( [(si,sj)] )

            while q:
                ci, cj = q.popleft()

                for di, dj in move:
                    ni, nj = ci+di, cj+dj

                    # 이동가능 좌표, 방문여부, 벽여부
                    if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and place[ni][nj]!='X':
                        # 다른 참가자가 있으면...
                        if place[ni][nj] == 'P':
                            # print(ci,cj, ni, nj)
                            # pprint(visited)
                            if visited[ci][cj] <= 2:
                                is_breaked = True
                                break
                        else:
                            q.append( (ni,nj) )
                            visited[ni][nj] = visited[ci][cj] + 1
                if is_breaked: break

            if is_breaked: break

        answer.append(0 if is_breaked else 1)
    
    return answer

print()
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]))
print([1])

print()
print(solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]))
print([0])

print()
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print([1, 0, 1, 1, 1])
# print()
# print(solution())
# print()