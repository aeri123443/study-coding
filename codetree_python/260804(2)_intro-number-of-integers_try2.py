'''
수의 개수
https://www.codetree.ai/ko/trails/complete/curated-cards/intro-number-of-integers/description

내장함수 사용해보기
문제 분석: 9m 43s
코드 작성: 21m 37s
최종 디버깅: 0m 0s

총 소요 시간: 31m 21s
'''
from bisect import bisect_right, bisect_left
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cmds = [int(input()) for _ in range(M)]
answer = []

for v in cmds:
    db = bisect_left(arr, v)
    ub = bisect_right(arr, v)
    # print(v, ub, db, ub - db - 1)
    # print()
    answer.append(ub - db)

print('\n'.join(map(str, answer)))