'''
1463. 1로 만들기
https://www.acmicpc.net/problem/1463
1-1 효율성 생각 안 하고 풀기 (TC 확인용)
'''
import sys
input = sys.stdin.readline

N = int(input())

def dfs(n, cnt):
    if n == 1:
        return cnt

    result = []

    if n % 3 == 0: result.append( dfs(n//3, cnt+1) )
    if n % 2 == 0: result.append( dfs(n//2, cnt+1) )
    result.append(dfs(n - 1, cnt + 1))

    return min(result)

print(dfs(N, 0))