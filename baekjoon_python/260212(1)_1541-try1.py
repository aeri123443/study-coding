'''
1541. <실버 2> 잃어버린 괄호
https://www.acmicpc.net/problem/1541
'''

import sys
import re
input = sys.stdin.readline

arr = re.split(r'([+-])', input().strip())
# print(arr)

answer = 0
# 한 번 -가 나오면 그 이후의 숫자는 그냥 다 뺀다
minus = False
for x in arr:
    if x.isnumeric():
        if minus:
            answer -= int(x)
        else:
            answer += int(x)
    elif x=='-':
        minus = True

print(answer)
