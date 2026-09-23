'''
최소 점프 횟수
https://www.codetree.ai/ko/trails/complete/curated-cards/test-min-num-of-jumps/description

문제 분석: 4m 4s
코드 작성: 6m 21s
최종 디버깅: 0m 0s

총 소요 시간: 10m 25s
'''
INF = float('inf')
N = int(input())
arr = list(map(int, input().split()))
dp = [INF]*N
dp[0] = 0

def dfs(cur):
    c_cnt = dp[cur]
    for d in range(1, arr[cur]+1):
        nxt = cur+d # 다음 인덱스
        if nxt < N and c_cnt+1 < dp[nxt]:
            dp[nxt] = c_cnt+1
            dfs(nxt)

dfs(0)
if dp[-1] != INF: print(dp[-1])
else: print(-1)
