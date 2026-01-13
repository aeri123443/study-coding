'''
1074. <골드5> Z
https://www.acmicpc.net/problem/1074
16 15 15 SIGTERM
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
answer = -1
add_num = [[0, 1], [2, 3]]

def dfs(sx, sy, snum, width):
    global answer
    # print(width, '...sx, sy, snum:', sx, sy, snum)
    if width == 1:   
        # print('c, r, sx, sy: ', c, r, sx, sy)
        nx, ny = c-sx, r-sy
        # print('snum, nx, ny, sx, sy: ',snum, nx, ny, sx, sy)
        answer = snum+add_num[ny][nx]
        return
    
    ex, ey = sx+width, sy+width
    
    # nx = sx if c <= ex else ex
    # ny = sy if r <= ey else ey
    nx, ny, nxt_num = -1, -1, -1
    # print('standard c, r, ex, ey:', c, r, ex, ey)
    if (c < ex) and (r < ey):
        # print('(c < ex) and (r < ey)')
        nx = sx
        ny = sy
        nxt_num = snum
    elif (c < ex) and (r >= ey) :
        # print('(c < ex) and (r >= ey)')
        nx = sx
        ny = sy+width
        nxt_num = snum+(width**2)*2
    elif (c >= ex) and (r < ey):
        # print('(c >= ex) and (r < ey)')
        nx = sx+width
        ny = sy
        nxt_num = snum+(width**2)
    elif (c >= ex) and (r >= ey):
        # print('(c >= ex) and (r >= ey)')
        nx = sx+width
        ny = sy+width
        nxt_num = snum+(width**2)*3
    dfs(nx, ny, nxt_num, width//2)

dfs(0, 0, 0, 2**(N-1))
print(answer)