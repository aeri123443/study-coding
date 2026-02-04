'''
2839. <실버 4> 설탕 배달 
https://www.acmicpc.net/problem/2839
'''

import sys
from pprint import pprint

input = sys.stdin.readline

num = int(input())
answer = float('inf')

# 5씩 빼면서 3의 배수가 되는지 탐색
five = 0

while num >= 0:

    if num%3 == 0:
        answer = min(answer, five + num//3)
        # print(five, num//3)
    
    num -= 5
    five += 1

print(answer) if answer < float('inf') else print(-1)
