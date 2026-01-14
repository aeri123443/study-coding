'''
1931. <골드5> 회의실 배정
https://www.acmicpc.net/problem/1931
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())

# 입력: 시작 시간이 같은데 끝나는 시간이 더 나중이면 넘어감
# s_e_map = {}
# for _ in range(N):
#     s, e = map(int, input().split())
#     if (s in s_e_map) and (s_e_map[s] <= e):
#         continue
#     s_e_map[s]=e

arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s,e])
# pprint(s_e_map)

# end time 기준 정렬
# arr = sorted(s_e_map.items(), key=lambda x:x[1])
arr.sort(key=lambda x:(x[1], x[0]))
# print(arr)

cnt = 0
prev_end = 0
for s, e in arr:
    if prev_end <= s:
        cnt += 1
        prev_end = e

print(cnt)