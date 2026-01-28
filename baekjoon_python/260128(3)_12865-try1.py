'''
12865. <골드 5> 평범한 배낭
https://www.acmicpc.net/problem/12865
시간초과
'''

import sys
input = sys.stdin.readline

N, W = map(int, input().split())
arr = [] #[w, v]
for _ in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)

max_v = 0

def find_vest_v(si, total_w, total_v):
    global max_v

    for i in range(si, N):
        new_total_w = total_w + arr[i][0]

        if new_total_w <= W:
            new_total_v = total_v + arr[i][1]
            max_v = max(new_total_v, max_v)
            find_vest_v(i+1, new_total_w, new_total_v)

find_vest_v(0,0,0)
print(max_v)
