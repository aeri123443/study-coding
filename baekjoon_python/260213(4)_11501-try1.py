'''
11501. <실버 2> 주식
https://www.acmicpc.net/problem/11501
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    m = arr[-1]
    answer = 0
    for i in range(N-1, -1, -1):
        if arr[i] < m:
            answer += m-arr[i]
        elif arr[i] > m:
            m = arr[i]

    # 최대 이익이 음수가 될 바에 아무것도 안 사는 것이 나음
    print(max(0, answer)) 
