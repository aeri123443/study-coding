'''
p.663 76. 정수 삼각형
https://school.programmers.co.kr/learn/courses/30/lessons/12913
소요시간: 15m 23s
'''

def solution(land):
    N = len(land)
    arr = [[0]*4 for _ in range(N)]
    arr[0] = [*land[0]]
    
    for i in range(1, N):
        for j in range(4):
            # review: 리스트끼리 더해서 합칠 수 있음
            # land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

            if j==0: arr[i][j] = max(arr[i-1][1], arr[i-1][2], arr[i-1][3]) + land[i][j]
            elif j==1: arr[i][j] = max(arr[i-1][0], arr[i-1][2], arr[i-1][3]) + land[i][j]
            elif j==2: arr[i][j] = max(arr[i-1][0], arr[i-1][1], arr[i-1][3]) + land[i][j]
            elif j==3: arr[i][j] = max(arr[i-1][0], arr[i-1][1], arr[i-1][2]) + land[i][j]
    # print(arr)

    return max(arr[-1])

# 16
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
