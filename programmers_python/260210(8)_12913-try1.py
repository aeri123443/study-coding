'''
12913. Lv.2 땅따먹기
https://school.programmers.co.kr/learn/courses/30/lessons/12913
11m 46s
'''

def solution(land):
    n = len(land)

    dp = [[0]*4 for _ in range(n)]
    dp[0] = land[0]

    for i in range(1,n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
        dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]


    # print(dp) 
    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))