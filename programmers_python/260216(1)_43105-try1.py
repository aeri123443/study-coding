'''
43105. Lv.3 정수 삼각형
https://school.programmers.co.kr/learn/courses/30/lessons/43105
9m 47s
'''

def solution(triangle):
    n = len(triangle)
    dp = [*triangle[-1]]
    # print(dp)

    for i in range(n-1, 0, -1):
        for j in range(i):
            dp[j] = max(dp[j], dp[j+1]) + triangle[i-1][j]
        # print(dp)

    return dp[0]

print()
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(30)


print()
print(solution([[0]]))
print(0)

# print()
# print(solution())
# print()
