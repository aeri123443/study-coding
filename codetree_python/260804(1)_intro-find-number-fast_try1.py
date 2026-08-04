'''
숫자 빠르게 찾기
https://www.codetree.ai/ko/trails/complete/curated-cards/intro-find-number-fast/description

문제 분석: 2m 23s
코드 작성: 4m 42s
최종 디버깅: 0m 0s

총 소요 시간: 7m 5s
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cmds = [int(input()) for _ in range(M)]
answer = []

def bs(x):
    i, j = 0, N-1

    while i <= j:
        mid = (i+j)//2
        if arr[mid] > x:
            j = mid - 1
        elif arr[mid] < x:
            i = mid + 1
        else:
            return mid + 1

    return -1

for v in cmds:
    answer.append(bs(v))

print('\n'.join(map(str,answer)))