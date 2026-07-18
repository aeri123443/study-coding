'''
92344. 파괴되지 않은 건물
https://school.programmers.co.kr/learn/courses/30/lessons/92344

문제 분석: 08m 16s
코드 작성: 12m 48s
디버깅: 1m 49s -> 누적합인데 누적을 안하고 대입함 ㅁㅊ~ 
total: 22m 53s
'''

def solution(board, skill):
    n, m = len(board), len(board[0])
    sum_map = [ [0]*(m+1) for _ in range(n+1) ]

    # 경계값 표시
    for t, r1, c1, r2, c2, d in skill:
        degree = d if t==2 else -d

        sum_map[r1][c1] += degree
        sum_map[r1][c2+1] -= degree
        sum_map[r2+1][c1] -= degree
        sum_map[r2+1][c2+1] += degree

    # 가로 누적합
    for i in range(n):
        for j in range(m):
            sum_map[i][j+1] += sum_map[i][j]

    # 세로 누적합
    for j in range(m):
        for i in range(n):
            sum_map[i+1][j] += sum_map[i][j]

    # 누적합 적용
    answer = 0 # 파괴되지 않은 건물 수

    for i in range(n):
        for j in range(m):
            if board[i][j] + sum_map[i][j] > 0:
                answer += 1

    return answer

# 10
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
# 6
print(solution([[1,2,3],[4,5,6],[7,8,9]],	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
