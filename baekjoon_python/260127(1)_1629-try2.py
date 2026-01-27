'''
1629. <실버 1> 곱셈
https://www.acmicpc.net/problem/1629
분할정복으로 풀어보기
'''

import sys
input = sys.stdin.readline

# a^b mod c
a, b, c = map(int, input().split())
dp = {1:a}

def mod(b):
    
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    half_mod = mod(b//2)

    if b%2 == 0:
        return (half_mod*half_mod)%c
    else:
        return (half_mod*half_mod*a)%c

    # return dp[b]

print(mod(b))
