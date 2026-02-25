'''
121690. [PCCP 모의고사 #2] 4번 - 보물 지도
https://school.programmers.co.kr/learn/courses/15009/lessons/121690
'''

'''
이 신발을 신고 뛰면 한 번에 두 칸을 이동할 수 있으며, 함정이 있는 칸도 넘을 수 있습니다. 
하지만, 이 신발은 한 번밖에 사용할 수 없습니다. 신비로운 신발을 사용하여 뛰어서 두 칸을 이동하는 시간도 1입니다.

대각선으로 뛸 수도 있는지?
'''
from collections import deque
from pprint import pprint

def solution(n, m, hole):
    board = [[0]*n for _ in range(m)]
    visited = [[[-1,-1] for _ in range(n)] for _ in range(m)] # [사용함, 사용안함]
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # 함정 표시
    for x, y in hole:
        board[y-1][x-1] = 1
    # pprint(board)
    # pprint(visited)
    q = deque() # (x,y), 사용여부(사용0,미사용1)
    q.append([(0,0), 1])
    visited[0][0][1] = 0
    
    while q:
        (cx, cy), c_used = q.popleft()
        
        for dx, dy in move:
            nx, ny = cx+dx, cy+dy
            
            # 이동 가능한 범위
            if 0<=nx<n and 0<=ny<m:
                # 함정이 없으면 그대로 직진
                if board[ny][nx]==0:
                    if visited[ny][nx][c_used] == -1:
                        visited[ny][nx][c_used] = visited[cy][cx][c_used] + 1
                        q.append([(nx,ny), c_used])
                # 함정 있음 + 뛰어넘은 적 없음 + 존재하는 좌표
                elif c_used==1: 
                    nnx, nny = nx+dx, ny+dy
                    if 0<=nnx<n and 0<=nny<m and visited[nny][nnx][0] == -1 and board[nny][nnx]==0:
                        visited[nny][nnx][0] = visited[cy][cx][c_used] + 1
                        q.append([(nnx,nny), 0])
                    
    # pprint(visited)
    
    # print(visited[-1][-1])
    a, b = visited[-1][-1]

    if a<0 and b<0: 
        return -1
    elif a>0 and b<0: 
        return a
    elif a<0 and b>0:
        return b-1
    else:
        return min(a, b-1)
