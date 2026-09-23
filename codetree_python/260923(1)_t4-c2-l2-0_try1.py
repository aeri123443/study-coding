'''
특정 조건에 맞게 K개 중에 1개를 N번 뽑기
https://www.codetree.ai/ko/trails/complete/curated-cards/intro-n-permutations-of-k-with-repetition-under-constraint/description
'''

K, N = map(int, input().split())
nums = [i for i in range(1, 1+K)]

def bt(arr):
    if len(arr) == N:
        print(' '.join(map(str, arr)))
        return

    for n in nums:
        if len(arr) >= 2 and arr[-1]==arr[-2]==n:
            continue
        new_arr = [*arr, n]
        bt(new_arr)

bt([])
