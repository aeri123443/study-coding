'''
12900. Lv.2 2 x n 타일링
https://school.programmers.co.kr/learn/courses/30/lessons/12900
17m 25s
'''

def solution(n):
    MOD = 1000000007

    if n == 1: return 1
    if n == 2: return 2
    dp = [0]+[0]*n
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-2]%MOD + dp[i-1]%MOD
    # print(dp)
    return dp[-1]%MOD

# print(solution(4))
# print(solution(1))
# print(solution(2))
# print(solution(3))
print(solution(60000))
