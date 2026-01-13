'''
1074. <골드5> Z
https://www.acmicpc.net/problem/1074
16 15 15 SIGTERM
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
board = [[0]*(2**N) for _ in range(2**N)]
idx_num, value_num = 1, 1

board[0][1] = 1
board[1][0] = 2
board[1][1] = 3

def explore():
    global idx_num, value_num

    for _ in range(2, N+1):
        idx_num *= 2
        value_num *= 4
        idx_move = [(idx_num, 0, value_num), (0, idx_num, value_num*2), (idx_num, idx_num, value_num*3)]
        
        # 4번 반복
        for dx, dy, dvalue in idx_move:
            # 이전 사각형만큼 반복
            for i in range(idx_num):
                for j in range(idx_num):
                    nx, ny = j+dx, i+dy
                    # print(nx, ny)
                    board[ny][nx] = board[i][j] + dvalue
                    if (ny==r) and (nx==c):
                        return board[ny][nx]

        




if N==1:
    # pprint(board)
    print(board[r][c])
else:
    print(explore())
    # pprint(board)
    # print(board[r][c])