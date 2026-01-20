'''
2018. <실버5> 수들의 합 5
https://www.acmicpc.net/problem/2018
'''

from pprint import pprint
import sys
import math

input = sys.stdin.readline

N = int(input())
cnt = 1 # 자기자신
s = math.ceil(N/2) # 절반부터 시작
e = s-1
# print(s, e)

sum_num = s
while e > 0:
    sum_num += e
    if sum_num < N:
        e -= 1
    elif sum_num > N:
        s -= 1
        e = s-1
        sum_num = s
    else:
        # print('s, e', s, e)
        cnt += 1 

print(cnt)
