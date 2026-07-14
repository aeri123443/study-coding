'''
92344. 파괴되지 않은 건물
https://school.programmers.co.kr/learn/courses/30/lessons/92344

시간 초과
'''

from pprint import pprint

def solution(board, skill):
    N, M = len(board), len(board[0])

    # 1. 내구도 보드 선언
    hp_board = board[:][:]

    # 2. 공격/방어 여부 판정
    # 공격(1): -degree, 방어(2): +degree
    for t, r1, c1, r2, c2, d in skill:
        rev = -1 if t == 1 else 1
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                hp_board[i][j] += (rev*d)
    # pprint(hp_board)

    # 파괴되지 않은 건물 수 탐색
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