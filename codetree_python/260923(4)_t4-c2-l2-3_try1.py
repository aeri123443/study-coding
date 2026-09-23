'''
가능한 수열 중 최솟값 구하기
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-find-min-of-possible-series/description

문제 분석: 4m 47s
코드 작성: 12m 32s
최종 디버깅: 0m 0s

총 소요 시간: 17m 19s
'''
def check(arr):
    for n in range(1, len(arr)//2+1):
        a = tuple(arr[-n:])
        b = tuple(arr[-n*2:-n])
        if a == b:
            return False
    return True

N = int(input())
nums = [4,5,6]

def dfs(arr):
    if len(arr)==N:
        print(''.join(map(str, arr)))
        return True

    for num in nums:
        new_arr = [*arr, num]
        if check(new_arr):
            success = dfs(new_arr)
            if success:
                return True


    return False

dfs([])
