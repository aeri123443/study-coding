'''
최소 차 분할
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-minimum-diff-partition/description
'''

N = int(input())
arr = list(map(int, input().split()))

all_sum = sum(arr)
dp = [False]*(all_sum + 1)
dp[0] = True

for n in arr:
    for i in range(all_sum, -1, -1):
        if dp[i] and dp[i]+n <= all_sum:
            dp[i+n] = True

answer = float('inf')
for i in range(all_sum//2+2):
    v = dp[i]
    if v:
        answer = min(answer, abs(all_sum-2*i))

print(answer)


