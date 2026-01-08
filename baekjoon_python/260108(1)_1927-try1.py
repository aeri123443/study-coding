'''
1927. <실버2> 최소 힙
https://www.acmicpc.net/problem/1927
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    elif x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))

