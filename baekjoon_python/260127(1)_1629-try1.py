'''
1629. <실버 1> 곱셈
https://www.acmicpc.net/problem/1629
모듈러 연산 숙지
dp -> 메모리 초과
'''

import sys
input = sys.stdin.readline

# a^b mod c
a, b, c = map(int, input().split())
dp = {1:a}

def mod(b):
    
    if b in dp:
        return dp[b]

    if b%2 == 0:
        div2 = div1 = mod(b//2)
    else:
        div1 = mod(b//2)
        div2 = mod(b//2+1)
    
    dp[b] = (div1*div2)%c
    # print('b, div1, div2, dp[b]', b, div1, div2, dp[b])

    return dp[b]

print(mod(b))
