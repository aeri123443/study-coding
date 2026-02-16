'''
12907. Lv.3 거스름돈
https://school.programmers.co.kr/learn/courses/30/lessons/12907
'''

def solution(n, money):
    MOD = 1_000_000_007
    dp = [0]*(n+1)
    money = sorted(set(money))

    for m in money:
        dp[m] += 1 # 자기 코인만 쓰는 경우를 추가
        for i in range(m+1, n+1):
            if i-m>0: dp[i] = (dp[i] + dp[i-m])%MOD

    return dp[-1]

print()
print(solution(5, [1,2,5]))
print(4)

print()
print(solution(5, [2,5]))
print(1)

# print()
# print(solution())
# print()