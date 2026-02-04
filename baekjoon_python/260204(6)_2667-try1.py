'''
2667. <실버 1> 단지번호붙이기
https://www.acmicpc.net/problem/2667
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [[0]*N for _ in range(N)] #0:False, 1:True
move = [ (0,1), (0,-1), (1,0), (-1,0) ]
board = []
for _ in range(N):
    board.append( list(map(int, list(input().strip()))))

# pprint(board)

groups = []
def grouping(i, j):

    q = deque()
    q.append([i, j])

    cnt = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in move:
            ni, nj = di+ci, dj+cj
            if 0<=ni<N and 0<=nj<N and board[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                q.append([ni, nj])
    return cnt

for i in range(N):
    for j in range(N):
        if board[i][j]==1 and not visited[i][j]:
            visited[i][j] = 1
            cnt = grouping(i,j)
            # print(i, j, cnt)
            groups.append(cnt)

print(len(groups))
print('\n'.join(map(str, sorted(groups))))