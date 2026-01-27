'''
1932. <실버 1> 정수 삼각형
https://www.acmicpc.net/problem/1932

'''

import sys
from pprint import pprint
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
board = [[0]*(i+1) for i in range(N)]

board[-1] = arr[-1][:]
# print(board)
for i in range(N-1, 0, -1):
    # print(i, arr[i])
    for j in range(i):  
        # print(i-1)
        board[i-1][j] = max(board[i][j], board[i][j+1]) + arr[i-1][j]
    # pprint(board)

print(board[0][0])