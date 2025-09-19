'''
p.672 78. 가장 큰 정사각형 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/12905
소요시간: 51m 19s (힌트 참고)
2*2 -> 3*3으로 넘어갈 때 양 사이드만 확인하면 된다는 것까진 파악했었음
더 나아가서, 숫자를 대입해보면서 -> 그렇다면 대각선 범위로 확장하고, 위/왼쪽/대각선만 확인하면 된다는 걸 파악했어야 함
+ 테스트케이스는 최솟값 조건일때와 적당히 큰 조건일 때를 모두 확인해봐야 함
'''

def solution(board):
    N = len(board)
    M = len(board[0])
    if N==1 or M==1:
        for i in range(N):
            for j in range(M):
                if board[i][j]==1:
                    return 1
        return 0
    
    max_num = 0
    for i in range(1,N):
        for j in range(1,M):
            if board[i][j]==1:
                # 위, 왼쪽, 대각선 확인 후 최솟값+1
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_num = max(max_num, board[i][j])
    return max_num*max_num

# 0~1
print(solution([[0]]))
print(solution([[1]]))
print(solution([[1, 0]]))
print(solution([[0],[1]]))

# 9
print(solution([[0,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [0,0,1,0]]))

# 4
print(solution([[0,0,1,1],
                [1,1,1,1]]))

# 25
print(solution([[0,1,1,1,1,0,0,0], 
                [0,1,1,1,1,0,0,0], 
                [0,1,1,1,1,1,1,0], 
                [0,1,1,1,1,1,1,0], 
                [0,0,1,1,1,1,1,0], 
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,0],
                [1,1,1,0,0,0,0,0]]))
