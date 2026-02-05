'''
5430. <골드 5> AC
https://www.acmicpc.net/problem/5430
'''

import sys
from collections import deque
from pprint import pprint

# 배열이 비었는데 D하면 에러
input = sys.stdin.readline

T = int(input())
# T = 1

for _ in range(T):
    p = list(input().strip())
    _ = input()
    arr = input().strip()
    arr = deque(map(int, arr.strip('[').strip(']').split(','))) if len(arr)>2 else deque()
    # print(arr)
    # print(p)
    rev = False # 리버스 여부
    err = False # 에러 여부
    for x in p:
        # R: 배열에 있는 수의 순서를 뒤집음
        if x == 'R':
            rev = not rev
        # D: 첫번째 수를 버림
        elif not arr:
            err = True
            break
        elif rev:
            arr.pop()
        else:
            arr.popleft()
        # print(arr)

    # 값 출력
    if err:
        print('error')
    elif rev:
        arr.reverse()
        print(f"[{','.join(map(str, arr))}]")
    else:
        print(f"[{','.join(map(str, arr))}]")

