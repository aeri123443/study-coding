'''
10814. 나이순 정렬
https://www.acmicpc.net/problem/10814
'''

N = int(input())
arr = [input().split() for _ in range(N)]
arr.sort(key=lambda x:int(x[0]))

[print(*a, sep=' ') for a in arr]