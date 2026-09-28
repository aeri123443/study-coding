'''
정수 사각형 차이의 최소 2
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-minimum-difference-on-the-integer-grid-2/description
'''

INF = float('inf')
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

nums = { x for line in board for x in line }
answer = INF
for low in nums:
    if board[0][0] < low: continue
    dp = [INF]*(N+1)
    dp[1] = board[0][0]

    for r in range(N):
        for c in range(N):
            dp_c = c+1
            if board[r][c] < low:
                dp[dp_c] = INF # 진입 불가 경로로 초기화
            else:
                dp[dp_c] = max(  board[r][c], min(dp[dp_c], dp[dp_c-1]) )
    answer = min(answer, dp[-1]-low)

print(answer)


