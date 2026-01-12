'''
10773. <실버4> 제로
https://www.acmicpc.net/problem/10773
'''

import sys
input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))