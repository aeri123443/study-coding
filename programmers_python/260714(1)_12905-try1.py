'''
12905. 가장 큰 정사각형 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/12905

문제 분석: 4m 22s
코드 작성: 17m 25s
디버깅: 0m 0s
total: 21m 48s
'''
import pprint

def solution(board):
    n = len(board)
    m = len(board[0])

    max_num = 0

    memo = [[0]*m for _ in range(n)]

    # 첫 행/열 메모제이션
    for i in range(n):
        max_num = max(max_num, board[i][0])
        memo[i][0] = board[i][0]
    for j in range(m):
        max_num = max(max_num, board[0][j])
        memo[0][j] = board[0][j]

    # 두 번째 행/열부터 메모제이션
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 0: continue
            tmp_min = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
            memo[i][j] = tmp_min + 1
            max_num = max(max_num, memo[i][j])

    # pprint.pprint(memo)
    return max_num*max_num

# 9
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# 4
print(solution([[0,0,1,1],[1,1,1,1]]))
