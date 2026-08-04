'''
수의 개수
https://www.codetree.ai/ko/trails/complete/curated-cards/intro-number-of-integers/description

문제 분석: 9m 43s
코드 작성: 21m 37s
최종 디버깅: 0m 0s

총 소요 시간: 31m 21s
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cmds = [int(input()) for _ in range(M)]
answer = []

def down_b(x):
    i, j = 0, N-1
    ans = -1

    while i <= j:
        mid = (i+j) // 2

        if arr[mid] < x:
            ans = mid
            i = mid + 1
        else:
            j = mid - 1

        # print()

    return ans

def upper_b(x):
    i, j = 0, N-1
    ans = N

    while i <= j:
        mid = (i+j)//2
        if arr[mid] > x:
            ans = mid
            j = mid -1
        else:
            i = mid + 1
        # print()

    return ans

for v in cmds:
    db = down_b(v)

    ub = upper_b(v)
    # print(v, ub, db, ub - db - 1)
    # print()
    answer.append(ub - db - 1)

print('\n'.join(map(str, answer)))