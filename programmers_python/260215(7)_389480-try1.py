'''
389480. Lv.2 완전범죄
https://school.programmers.co.kr/learn/courses/30/lessons/389480
'''
#  두 도둑 모두 경찰에 붙잡히지 않도록 모든 물건을 훔쳤을 때, || -1
#  A도둑이 남긴 흔적의 누적 개수의 최솟값

def solution(info, n, m):
    info_cnt = len(info)
    INF = float('inf')
    dp = [[INF]*m for _ in range(info_cnt)]
    # 첫행 초기화
    if info[0][0]<n: dp[0][0] = info[0][0] # a가 훔침
    if info[0][1]<m: dp[0][info[0][1]] = 0 # b가 훔침
    # dp[0] = [info[0][0]]*info[0][1] + [0]*(m-info[0][1])

    for i in range(1, info_cnt):
        for b in range(m):

            if dp[i-1][b]+info[i][0] < n:   
                dp[i][b] = min(dp[i][b], dp[i-1][b]+info[i][0])
            if b >= info[i][1]:
                dp[i][b] = min(dp[i][b], dp[i-1][b-info[i][1]])

    answer = min(dp[-1])
    return answer if answer < INF else -1

print()
print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print(2)

print()
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
print(0)

print()
print(solution([[3, 3], [3, 3]], 7, 1))
print(6)

print()
print(solution([[3, 3], [3, 3]], 6, 1))
print(-1)

print()
print(solution([[2, 2], [2, 2], [1, 1], [3, 1], [2, 3], [3, 2], [3, 3], [3, 1], [2, 1], [3, 1], [1, 2], [1, 3], [3, 2], [2, 1], [1, 3], [2, 1], [1, 3], [1, 3], [2, 1], [3, 2], [1, 3], [2, 1], [1, 2], [3, 3], [3, 3], [2, 3], [1, 2], [3, 2], [2, 3], [2, 2], [2, 2], [3, 1], [2, 2], [2, 3], [1, 1], [3, 1], [3, 3], [3, 2], [2, 1], [2, 2]], 40, 40))
print()

# print()
# print(solution())
# print()