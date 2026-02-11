'''
1026. <실버 4> 보물
https://www.acmicpc.net/problem/1026
'''

import sys

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

print( sum( a*b for (a, b) in zip(A, B) ) )