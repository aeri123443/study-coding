'''
p.598 64. 달팽이 수열 만들기
소요시간: 26m 23s
'''
import pprint

def solution(n):
    move = [[0, 1], [1,0], [0,-1], [-1, 0]]
    answer = [[-1]*n for _ in range(n)]
    answer[0][0]=1
    d = 0
    i = 0
    j = 0
    for _ in range(1, n*n):
        ni, nj = i+move[d][0], j+move[d][1]
        
        if not (ni>=0 and nj>=0 and ni<n and nj<n and answer[ni][nj]==-1):
            if d==3: d=0
            else: d+=1
            ni, nj = i+move[d][0], j+move[d][1]
        answer[ni][nj]=answer[i][j]+1        
        i, j = ni, nj
        
    return answer
# [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
pprint.pprint(solution(3))
# [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
pprint.pprint(solution(4))
