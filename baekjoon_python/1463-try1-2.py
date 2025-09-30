'''
1463. 1로 만들기
https://www.acmicpc.net/problem/1463
1-2 효율성 생각하고 풀기!
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

memo = [-1] * (N+1)

# 2제곱, 3제곱, 6제곱수 미리 기록
memo[0], memo[1] = 0, 0
if N>=2: memo[2] = 1
if N>=3: memo[3] = 1
if N>=6: memo[6] = 2

def dfs(n):
    global memo
    if memo[n] != -1:
        return memo[n]

    result = set()
    if n%3 == 0: result.add(dfs(n//3))
    if n%2 == 0: result.add(dfs(n//2))
    result.update([dfs(n-1), dfs(n-2)+1])

    min_result = min(result) + 1
    memo[n] = min_result
    return min_result

dfs(N)
print(memo[-1])