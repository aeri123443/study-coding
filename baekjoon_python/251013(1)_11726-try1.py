'''
11726. <실버3> 2×n 타일링
https://www.acmicpc.net/problem/11726
'''
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
if N==1: print(1)
elif N==2: print(2)
else:
    memo = [0] * (N+1)
    memo[0], memo[1] = 1, 1
    for i in range(2, N+1):
        memo[i] = (memo[i-1] + memo[i-2])%10007
    print((memo[N-1]+memo[N-2])%10007)
