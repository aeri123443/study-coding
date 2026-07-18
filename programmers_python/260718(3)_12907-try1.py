'''
12907. 거스름돈
https://school.programmers.co.kr/learn/courses/30/lessons/12907
'''

def solution(n, money):
    dp = [1] + [0] * n

    for c in money:
        for i in range(c, n+1):
            dp[i] += dp[i-c]

    return dp[-1]

print(solution(5, [1,2,5])) # 4
