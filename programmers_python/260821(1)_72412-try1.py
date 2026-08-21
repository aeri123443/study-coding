'''
72412. 순위 검색
https://school.programmers.co.kr/learn/courses/30/lessons/72412

문제 분석: 6m 37s
코드 작성: 30m 19s
최종 디버깅: 0m 0s

총 소요 시간: 36m 56s
'''

from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    info_set = defaultdict(list)

    for line in info:
        a, b, c, d, score = line.split()
        score = int(score)

        for ca, cb, cc, cd in product([a,'-'], [b,'-'], [c,'-'], [d,'-']):
            info_set[ (ca, cb, cc, cd) ].append(score)

    for k in info_set:
        info_set[k].sort()

    # print(info_set)

    ans = []
    for line in query:
        a, _, b, _, c, _, d, score = line.split()
        score = int(score)

        q = (a, b, c, d)

        # print(q, score)
        if q not in info_set:
            ans.append(0)
            continue

        ans.append( len(info_set[q]) - bisect_left(info_set[q], score) )

    return ans


# [1,1,1,1,2,4]
print(solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))
