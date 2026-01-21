'''
17298. <골드 4> 오큰수
https://www.acmicpc.net/problem/17298
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
ans_arr = [0]*N

for i in range(N-1, -1, -1):
    # print('i', i)
    # 스택 단순화
    while stack:
        if arr[i] >= stack[-1]: stack.pop()
        else: break

    # 스택이 비었으면 -1 반환, 아니면 top 반환
    ans_arr[i] = str(stack[-1]) if stack else '-1'
    stack.append(arr[i])

print(' '.join(ans_arr))