'''
10844. <실버 1> 쉬운 계단 수
https://www.acmicpc.net/problem/10844
dp 전 슬로우코드
'''

import sys
sys.setrecursionlimit(int(1e6))

N = int(sys.stdin.readline())

answer = []
answer_cnt = 0

def backtraking(n, cnt): #최근 push한 숫자, 현재 자리수
    global answer, answer_cnt

    if cnt==N:
        print(''.join(map(str, answer)))
        answer_cnt+=1
        return

    for i in range(10):
        if n==i-1 or n==i+1:
            answer.append(i)
            backtraking(i, cnt+1)
            answer.pop()

for first in range(1,10):
    answer.append(first)
    backtraking(first, 1)
    answer.pop()

print(answer_cnt % 1000000000)


