'''
12971. Lv.3 스티커 모으기(2)
https://school.programmers.co.kr/learn/courses/30/lessons/12971
36m 53s
'''

def solution(sticker):
    N = len(sticker)
    answer = 0

    # sticker[0] 골랐을 때
    dp = [0]*N 
    dp[0] = sticker[0]
    for i in range(1, N-1):
        if i==1: 
            dp[1] = max(dp[0], sticker[1])
        else:
            dp[i] = max(dp[i-1], dp[i-2]+sticker[i])
    answer = max(dp[-3:])

    # dp[0] 안 골랐을 때    
    dp = [0]*N 
    dp[0] = 0
    for i in range(1, N):
        if i==1: 
            dp[1] = max(dp[0], sticker[1])
        else:
            dp[i] = max(dp[i-1], dp[i-2]+sticker[i])
    answer = max(answer, max(dp[-2:]))

    return answer

print()
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(36)

print()
print(solution([1, 3, 2, 5, 4]))
print(8)

# print()
# print(solution())
# print()