'''
경험치를 빠르게 얻기
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-gain-exp-quickly/description
'''

N, M = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(N)]

total = 0
for e, t in quests: total += t
dp = [-1]*(total+1) # dp[t] = 그 시간에 얻을 수 잇는 최대 경험치
dp[0] = 0

for e, t in quests:
    for i in range(total, -1, -1):
        v = dp[i]
        if v == -1: continue
        dp[i+t] = max(dp[i+t], dp[i]+e)

answer = -1
for i, v in enumerate(dp):
    if v >= M:
        answer = i
        break
print(answer)
