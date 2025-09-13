'''
1920. 수 찾기
https://www.acmicpc.net/problem/1920
'''

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for b in B:
    if b in A:
        print(1)
    else: print(0)
              