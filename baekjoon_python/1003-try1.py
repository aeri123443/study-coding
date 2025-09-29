'''
1003. 피보나치 함수
https://www.acmicpc.net/problem/1003
'''
import sys

input = sys.stdin.readline
# print = sys.stdout.write
# sys.stdin = open("input.txt", "r")

T = int(input())

def dp(n):
    global memo
    if memo[n]:
        return memo[n]
    result = dp(n-1) + dp(n-2)
    memo[n] = result
    return result

N_list = []
for _ in range(T):
    N_list.append(int(input()))

memo = [None]*(max(N_list)+1)

for N in N_list:

    if N == 0: print(1, 0)
    elif N == 1: print(0, 1)
    else:
        memo[0] = 1
        memo[1] = 1

        dp(N)
        print(memo[N-2], memo[N-1])
