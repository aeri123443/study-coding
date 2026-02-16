'''
2109. <골드 3> 순회강연
https://www.acmicpc.net/problem/2109
'''

import sys

input = sys.stdin.readline

N = int(input())

if N==0:
    print(0)
    sys.exit()

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(-x[0]))
# print(arr)
memo = [0]*(max(arr, key=lambda x:x[1])[1]+1)

for i in range(len(arr)):
    [np, nd] = arr[i]
    for j in range(nd, 0, -1):
        if memo[j] == 0:
            memo[j]=np
            break

# print(memo)
print(sum(memo))