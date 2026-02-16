'''
12905. Lv.2 가장 큰 정사각형 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/12905
45m 10s
'''
from pprint import pprint

def solution(board):
    N, M = len(board), len(board[0])

    if N==1 or M==1: return 1

    dp = [ [0]*M for _ in range(N) ]
    
    # 첫행, 첫열 채우기
    for i in range(N): dp[i][0] = board[i][0]
    for j in range(M): dp[0][j] = board[0][j]

    answer = 0

    for i in range(1,N):
        for j in range(1,M):
            if board[i][j]==1:
                board[i][j] = min(
                    board[i-1][j],
                    board[i][j-1],
                    board[i-1][j-1]
                ) + 1
                answer = max(answer, board[i][j])
    return answer*answer

print()
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(9)

print()
print(solution([[0,0,1,1],[1,1,1,1]]))
print(4)

# print()
# print(solution())
# print()