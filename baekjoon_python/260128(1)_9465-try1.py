'''
9465. <실버 1> 스티커
https://www.acmicpc.net/problem/9465
'''

import sys
from pprint import pprint
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [[0]*(N+2) for _ in range(4)]

    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    arr[1][2:] = a1
    arr[2][2:] = a2
    # pprint(arr)

    for j in range(2, N+2):
        for i in range(1, 3):

            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j-2], arr[i][j-2], arr[i+1][j-2], arr[i+1][j-1])

    # pprint(arr)
    # pprint([arr[1][-2:], arr[2][-2:]])
    print(max(arr[1][-1], arr[1][-2], arr[2][-2], arr[2][-1]))
    
   