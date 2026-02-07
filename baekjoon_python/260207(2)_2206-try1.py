'''
2206. <골드 3> 벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
'''

import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
move = [(0,1), (0,-1), (1,0), (-1,0)]
board = []
visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # [0:벽 부쉈을 때, 1:안 부쉈을 때]

# 방문 가능 좌표 확인
# return [방문 가능 여부, 벽 부숨 여부]
def is_possible(i, j, is_breaked):
    if not (0<=i<N and 0<=j<M):
        return [False, is_breaked] 
    # print('is_possible...', i, j, is_breaked, '|', visited[i][j][0], visited[i][j][1])

    # 벽을 부순 적이 있으면, 더 부술 수 없음
    if is_breaked:
        if board[i][j]==0 and visited[i][j][0]==0:
            return [True, is_breaked]
    # 벽을 부순 적이 없으면, 한 번은 부술 수 있음
    else:
        if board[i][j]==0 and visited[i][j][1]==0:
            return [True, is_breaked]
        elif board[i][j]==1 and visited[i][j][0]==0:
            return [True, True]
        
    return [False, is_breaked]


# 입력
for _ in range(N):
    board.append( list(map(int, list(input().strip()))) )

# pprint(board)
# pprint(visited)

q = deque() 
q.append([0,0,1,False]) # [i, j, cnt, is_breaked]
visited[0][0][1] = 1

while q:
    ci, cj, cnt, is_breaked = q.popleft()

    for di, dj in move:
        ni, nj = ci+di, cj+dj
        is_pos, is_break = is_possible(ni, nj, is_breaked)
        # print(is_pos, is_break)
        if is_pos:
            if is_break:
                visited[ni][nj][0] = cnt+1
            else:
                visited[ni][nj][1] = cnt+1
            # print(ni,nj,cnt+1,is_break)
            q.append([ni,nj,cnt+1,is_break])

# pprint(min(visited[-1][-1]))

# 결과에 따른 값 출력
answer = visited[-1][-1]
# 둘 다 0이면 -1
if answer[0]==0 and answer[1]==0: print(-1)
# 하나만 0이면 다른 하나 출력
elif answer[0]==0 or answer[1]==0: print(max(answer))
# 둘다 0 초과면 min값
else: print(min(answer))
