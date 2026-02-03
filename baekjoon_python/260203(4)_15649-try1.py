'''
15649. <실버 3> N과 M (1)
https://www.acmicpc.net/problem/15649
통과는 했지만 비효울적
백트래킹으로 풀어보기...
'''

import sys
from pprint import pprint

input = sys.stdin.readline

N, M = map(int, input().split())

def permutation(arr, num):
    # print(arr, num)
    if num == 1:
        return [[x] for x in arr]
    
    result = []
    for i in range(len(arr)):
        select_num = arr[i] # 값 선택
        attach = permutation([*arr[:i], *arr[i+1:]], num-1)
        # print([select_num, *attach])
        result.extend([ [select_num, *att] for att in attach])
        # print(result)
    # print(num, 'result', result)
    return result

arr = [i for i in range(1, N+1)]  
result = permutation(arr, M)
# pprint(result)
print('\n'.join([' '.join(map(str, per)) for per in result]))