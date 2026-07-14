'''
12913. 땅따먹기

https://school.programmers.co.kr/learn/courses/30/lessons/12913

문제 분석: 3m 13s
코드 작성: 7m 10s
디버깅: 0m 0s
total: 10m 23s
'''

def solution(land):

    memo = land[:][:]
    for i in range(1, len(land)):
        for j in range(4):
            max_prev = 0
            for k in range(4):
                if k==j: continue
                max_prev = max(max_prev, memo[i-1][k])
            memo[i][j] += max_prev
    # print(memo)

    return max(memo[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))