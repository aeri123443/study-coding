'''
1744. <골드 4> 수 묶기
https://www.acmicpc.net/problem/1744
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
answer = 0
# print(arr)

# 양수 ~ 1 초과까지 반복
tmp = None
while arr and arr[-1] > 1:
    num = arr.pop()

    if tmp == None:
        tmp = num
    else:
        answer += tmp*num
        tmp = None
if tmp: answer += tmp

# 정렬 순서 뒤집기
arr = arr[::-1]

# 음수 ~ 0 이하까지 반복
tmp = None
while arr and arr[-1] <= 0:
    num = arr.pop()

    if tmp == None:
        tmp = num
    else:
        answer += tmp*num
        tmp = None
if tmp: answer += tmp

# 남아있는 아이들은 그냥 다 더함
if arr: answer += sum(arr)

print(answer)
