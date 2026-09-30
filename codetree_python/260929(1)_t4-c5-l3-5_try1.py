'''
증가했다가 감소하는 부분 수열
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-increasing-and-descreasing-subsequence/description
'''
N = int(input())
arr = list(map(int, input().split()))


def get_lis_up():
    dp = [0] * N
    for i in range(N):
        max_lis_prev = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_lis_prev = max(max_lis_prev, dp[j])
        dp[i] = max_lis_prev + 1
    return dp


def get_lis_down():
    dp = [0] * N
    for i in range(N - 1, -1, -1):
        max_lis_prev = 0
        for j in range(i + 1, N):
            if arr[j] < arr[i]:
                max_lis_prev = max(max_lis_prev, dp[j])
        dp[i] = max_lis_prev + 1
    return dp


def main():
    up_dp = get_lis_up()  # arr[i]를 끝으로 하는 LIS
    down_dp = get_lis_down()  # arr[i]를 시작으로 하는 LDS

    answer = 0
    for i in range(N):
        # up_dp[i]와 down_dp[i] 모두 arr[i]를 포함하므로 1을 빼줍니다.
        answer = max(answer, up_dp[i] + down_dp[i] - 1)

    print(answer)

main()
