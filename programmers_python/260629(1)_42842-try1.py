'''
42842. 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842

문제 분석: 3m 2s
코드 작성: 11m 26s
디버깅: 0m 0s
total: 14m 30s
'''
import math
def solution(brown, yellow):
    for w in range(yellow, math.floor(math.sqrt(yellow))-1, -1):
        # yello의 w, h 후보
        if yellow % w != 0: continue
        h = int(yellow / w)
        if w < h: continue

        # brown과 일치하는지 수식 대입
        if 2*(w+h) + 4 == brown:
            return [w+2, h+2]
    return []

print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]
