'''
42898. Lv.3 등굣길
https://school.programmers.co.kr/learn/courses/30/lessons/42898
28m 57s
'''

from collections import deque

def solution(m, n, puddles):
    MOD = 1_000_000_007
    board = [[0]*(m+1) for _ in range(n+1)] # 패딩
    move = [(0,1), (1,0)]

    # 방문 불가 좌표 표시
    for j, i in puddles:
        board[i][j] = -1

    q = deque([(1, 1)]) # (i,j)
    board[1][1] = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in move:
            ni, nj = ci+di, cj+dj

            if ni <= n and nj <= m and board[ni][nj] != -1:
                
                # 첫방문이면 계산 후 큐에 넣음
                if board[ni][nj] == 0:
                    board[ni][nj] = board[ci][cj]
                    q.append( (ni, nj) )
                # 첫방문이 아니면 값만 누적
                else:
                    board[ni][nj] = (board[ni][nj]%MOD + board[ci][cj]%MOD)
                    

    return board[-1][-1] % MOD


print(solution(4, 3, [[2, 2]]))
print(solution(4, 3, []))