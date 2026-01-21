'''
17298. <골드 4> 오큰수
https://www.acmicpc.net/problem/17298
느린 코드로 tc 정답 만들기
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans_arr = ['-1' for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            ans_arr[i] = str(arr[j])
            break

print(' '.join(ans_arr))