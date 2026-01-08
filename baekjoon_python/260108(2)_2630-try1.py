'''
2630. <실버2> 색종이 만들기
https://www.acmicpc.net/problem/2630
'''
from pprint import pprint

import sys
input = sys.stdin.readline
answer = [0, 0]
arr = []

# 하나의 영역이 모두 같은 색으로 칠해졌는지 확인
def is_same(sx, ex, sy, ey): 
    global arr, answer
    target = arr[sy][sx]
    # print(target)
    for i in range(sx, ex):
        for j in range(sy, ey):
            if arr[j][i] != target:
                return False
    # print('same!', sx, ex, sy, ey)
    answer[target]+=1
    # print(answer)
    return True

# 재귀
def explore(sx, ex, sy, ey, n):
    global answer, arr
    # print(sx, ex, sy, ey, '...')
    same_result = is_same(sx, ex, sy, ey)
    # print(same_result)
    if not same_result:
        if n==2:
            # print('최소 도달', sx, ex, sy, ey)
            for i in range(sx, ex):
                for j in range(sy, ey):
                    # print(j, i, arr[j][i])
                    answer[ arr[j][i] ] += 1
            # print(answer)
            return 
        new_n = n/2
        x1, x2, x3 = sx, (sx+ex)//2, ex
        y1, y2, y3 = sy, (sy+ey)//2, ey
        explore(x1, x2, y1, y2, new_n)
        explore(x2, x3, y1, y2, new_n)
        explore(x1, x2, y2, y3, new_n)
        explore(x2, x3, y2, y3, new_n)


N = int(input())
for _ in range(N):
    tmp_arr = list(map(int, input().split()))
    arr.append(tmp_arr)

# pprint(arr)
explore(0, N, 0, N, N)
print(answer[0])
print(answer[1])