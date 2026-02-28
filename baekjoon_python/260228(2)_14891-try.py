'''
14891. <골드 5> 톱니바퀴
https://www.acmicpc.net/problem/14891

복사하고 값 안 바꾸는 실수 줄이기
'''

import sys
from collections import deque

input = sys.stdin.readline

items = [None]+[deque(map(int, list(input().strip()))) for _ in range(4)]
K = (int(input()))
# print(items)

def rotation(n, d):
    global items
    # print(' ', n, d)

    # 시계방향 1
    if d == 1:
        tmp = items[n].pop()
        # print('pop ', tmp, d)
        items[n].appendleft(tmp)
    # 반시계방향 -1
    elif d == -1:
        tmp = items[n].popleft()
        # print('pop ',tmp, d)
        items[n].append(tmp)

# 로테이션 확인

# items = [ deque([0, 1,2,3,4,5,6,7]) ]
# rotation(0, -1)
# print(items)

for _ in range(K):
    n, d = map(int, input().split())
    # print()
    # print(n, d)

    # 이번 회전에서 로테이션해야하는 배열
    rots = [None]*5

    # n번째 톱니바퀴 회전 
    rots[n] = d

    # 오른쪽 톱니바퀴 회전 확인
    cur_d = d
    for cur in range(n, 4):
        # 다음으로 넘어갈 수 있는지?
        if items[cur][2] != items[cur+1][6]:
            cur_d = -cur_d
            rots[cur+1] = cur_d
        else:
            break

    # 왼쪽 톱니바퀴 회전 확인
    cur_d = d
    for cur in range(n, 1, -1):
        # 다음으로 넘어갈 수 있는지?
        if items[cur][6] != items[cur-1][2]:
            cur_d = -cur_d
            rots[cur-1] = cur_d
        else:
            break

    # print(rots)
    # 톱니바퀴 회전하기
    for i in range(1, 5):
        if rots[i] != None:
            rotation(i,rots[i])

    # print(items)

# 점수 계산
print(
    items[1][0] * 1
    + items[2][0] * 2
    + items[3][0] * 4
    + items[4][0] * 8
)