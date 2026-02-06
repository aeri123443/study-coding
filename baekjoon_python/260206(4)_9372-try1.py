'''
9372. <실버 4> 상근이의 여행
https://www.acmicpc.net/problem/9372
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(N-1)
    for _ in range(M): input() # 버리는 코드