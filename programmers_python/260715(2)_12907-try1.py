'''
12907. 거스름돈
https://school.programmers.co.kr/learn/courses/30/lessons/12907

문제 분석: 36m 9s -> gpt 참고
코드 작성: 4m 31s
디버깅: 0m 0s
total: 40m 40s
'''

def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1

    for coin in money:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]

    return dp[-1]

print(solution(5, [1,2,5])) # 4
print(solution(10, [1,2,5])) # 10
