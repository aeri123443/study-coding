'''
92344. 파괴되지 않은 건물
https://school.programmers.co.kr/learn/courses/30/lessons/92344

문제 분석 & 코드 작성: 20m 14s
디버깅: 47m 25s
total: 1h 7m 39s
'''

from pprint import pprint

def solution(board, skill):
    N, M = len(board), len(board[0])
    d_board = [[0]*(M+1) for _ in range(N+1)] # 변화량 맵

    # 1. 변화량 맵에 경계선 체크
    for type_num, r1, c1, r2, c2, degree in skill:
        d_val = -degree if type_num == 1 else +degree # 공격이면 -degree, 방어면 +degree
        d_board[r1][c1] += d_val
        d_board[r1][c2+1] -= d_val # 중복값 빼기
        d_board[r2+1][c1] -= d_val # 중복값 빼기
        d_board[r2+1][c2+1] += d_val # 두 번 중복된 값 더하기

    # 2. 변화량 맵 계산 (누적합)
    # 2-1. 행 누적합
    for i in range(N+1):
        for j in range(1, M+1):
            d_board[i][j] += d_board[i][j-1]
    # 2-2. 열 누적합
    for j in range(M+1):
        for i in range(1, N+1):
            d_board[i][j] += d_board[i-1][j]

    # 3. 변화량에 따른 최종 hp 업데이트 (가독성상 새 배열 사용)
    hp_board = board[:][:]
    for i in range(N):
        for j in range(M):
            hp_board[i][j] += d_board[i][j]

    # 4. 파괴되지 않은 건물 카운트
    answer = 0
    for i in range(N):
        for j in range(M):
            if hp_board[i][j] > 0:
                answer += 1

    return answer

# 10
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

# 6
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))