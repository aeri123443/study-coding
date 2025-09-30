'''
1463. 1로 만들기
https://www.acmicpc.net/problem/1463
메모리 초과 -> 바텀업 방식 시도
'''
import sys
input = sys.stdin.readline

N = int(input())
max_N = N+2
memo = [-1] * (N+1)

memo[0], memo[1] = 0, 0

for i in range(2, N+1):
    case1 = case2 = case3 = max_N
    if i%2==0: case1 = memo[i//2]
    if i%3==0: case2 = memo[i//3]
    case3 = memo[i-1]
    memo[i] = min(case1, case2, case3) + 1

print(memo[-1])