'''
132265. 롤케이크 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/132265

문제 분석: 3m 00s
코드 작성: 7m 43s
디버깅: 0m 0s
total: 10m 43s
'''

from collections import Counter, defaultdict

def solution(topping):
    a = dict(Counter(topping))
    b = defaultdict(int)

    answer = 0
    for v in topping:
        # a에게 있는 v를 b에게 옮김
        a[v] -= 1
        b[v] += 1
        if a[v]==0: del a[v]

        # 종류 비교
        if len(a) == len(b): answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0
