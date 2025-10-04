'''
9095. <실버3> 1, 2, 3 더하기
https://www.acmicpc.net/problem/9095
'''
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
n_list = [int(input()) for _ in range(T)]
memo = [0]*(max(n_list)+1)
answer = 0
memo[0], memo[1] = 1, 1

def dfs(N):
    global answer, memo

    if memo[N]!=0:
        return memo[N]

    case1 = case2 = case3 = 0
    if N>=3: case3 = dfs(N-3)
    if N>=2: case2 = dfs(N-2)
    case1 = dfs(N-1)
    N_case = case1 + case2 + case3
    memo[N] = N_case
    return N_case

for n in n_list:
    answer = 0
    dfs(n)
    print(memo[n])
