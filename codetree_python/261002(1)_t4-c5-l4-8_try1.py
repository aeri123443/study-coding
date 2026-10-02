'''
최대 합 분할
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-maximum-sum-partition/description
'''

N = int(input())
arr = list(map(int, input().split()))
INF = float('inf')

total = sum(arr)
dp_len = total*2+1
dp = [[-1]*dp_len for _ in range(N+1)]
dp[0][total] = 0

for i in range(1, N+1):
    n = arr[i-1]
    sum_prev = {(d,s) for d, s in enumerate(dp[i-1]) if s>-1}

    for diff, sp in sum_prev:
        # A 그룹에 넣으면: diff 증가, A합 증가
        dp[i][diff+n] = max(dp[i-1][diff+n], dp[i-1][diff]+n, dp[i][diff+n])
        # B 그룹에 넣으면: diff 감소, A합 불변
        dp[i][diff-n] = max(dp[i-1][diff-n], dp[i-1][diff], dp[i][diff-n])
        # C 그룹에 넣으면: 변화 없음, 값 그대로
        dp[i][diff] = max(dp[i-1][diff], dp[i-1][diff], dp[i][diff])

answer = (INF, -INF) # 차이 최소, 그때의 합 최대
for diff, s in enumerate(dp[-1]):
    answer = min(answer, (abs(diff-total), dp[-1][diff]))

print(answer[1])


