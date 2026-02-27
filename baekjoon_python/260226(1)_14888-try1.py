'''
14888. <실버1> 연산자 끼워넣기
https://www.acmicpc.net/problem/14888
'''

import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
oper_input = map(int, input().split())

opers = []
for i,v in enumerate(oper_input):
    if v>0:
        opers.extend([i]*v)
# print(opers)

operator = {
    0: lambda a,b : a+b,
    1: lambda a,b : a-b,
    2: lambda a,b : a*b,
    3: lambda a,b : int(a/b),
}

max_min = [-float('inf'), float('inf')]

for per_ops in set(permutations(opers)):
    # print()
    # print(per_ops)

    # 연산 수행
    result = nums[0]
    for i in range(N-1):
        o, n = per_ops[i], nums[i+1]
        # print(result, o, n, end=' = ')
        result = operator[o](result, n)
        # print(result)

    max_min[0] = max(max_min[0], result)
    max_min[1] = min(max_min[1], result)

print('\n'.join(map(str, max_min)))