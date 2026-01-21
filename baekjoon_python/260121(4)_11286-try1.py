'''
11286. <실버 1> 절댓값 힙
https://www.acmicpc.net/problem/11286
'''

from pprint import pprint
import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        print(heapq.heappop(heap)[1]) if heap else print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
        