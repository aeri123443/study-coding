'''
1874. <실버 2> 스택 수열
https://www.acmicpc.net/problem/1874
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())
target_arr = [int(input()) for _ in range(N) ]
answer_arr = []
# pprint(target_arr)
stack = []
n = 1
flag = True

for target in target_arr:
    # print('target: ', target)
    # print('before stack:', stack)
    # 스택이 비어있거나, top값이 target보다 작으면   
    if not stack or stack[-1] < target:
        # target이 나올 때까지 스택에 push 
        while n <= target:
            # print('n: ', n)
            stack.append(n)
            answer_arr.append('+')
            n += 1
        stack.pop()
        answer_arr.append('-')
    # top=stack 바로 팝
    elif stack[-1] == target:
        stack.pop()
        answer_arr.append('-')
    else: 
        flag = False
        break
    
    # print(stack)
    # print(' '.join(answer_arr))
    
if flag:
    print('\n'.join(answer_arr))
else:
    print('NO')
