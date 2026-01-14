'''
1931. <골드5> 회의실 배정
https://www.acmicpc.net/problem/1931
시간초과
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())
arr = [[0,0]]
max_num = 0
answer = 0

def dfs(idx, cnt):
    global answer
    answer = max(answer, cnt)
    # print('dfs... idx, cnt:', idx, cnt)

    # answer가 이미 회의 최댓값에 도달하면 끝
    if answer==N:
        return

    cx, cy = arr[idx]
    for ndx in range(idx+1, N+1):

        nx, ny = arr[ndx]
        if nx >= cy:
            # print('  cx, cy -> nx, ny', cx, cy, nx, ny)
            dfs(ndx, cnt+1)
    #  

# 입력 및 오름차순 정렬
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x:x[0])

# pprint(arr)
dfs(0,0)
print(answer)