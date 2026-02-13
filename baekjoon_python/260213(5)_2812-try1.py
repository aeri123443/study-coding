'''
2812. <2812> 크게 만들기
https://www.acmicpc.net/problem/2812
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(input().strip())
# print(arr)

stack = []
remain = K
for n in arr:
    if stack and stack[-1] < n:
        while stack and stack[-1] < n:
            stack.pop()
            remain -= 1
            if remain == 0: break
        if remain == 0: break
    stack.append(n)

# remain값이 남음 == stack이 내림차순 배열이다
if remain: print(''.join(stack[:-remain]))
# remain값이 안 남음 = stack이 내림차순 배열이다
else: print(''.join([*stack, *arr[K+len(stack):]]))
