'''
1463. <실버 3> 1로 만들기
https://www.acmicpc.net/problem/1463
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([ (n,0) ]) # number, cnt
visited = set()

while q:
    num, cnt = q.popleft()
    if num == 1:
        print(cnt)
        break
    if num == 2 or num == 3:
        print(cnt+1)
        break

    if not num in visited:
        visited.add(num)
        if num%3==0: 
            q.append((num//3, cnt+1))
        if num%2==0: 
            q.append((num//2, cnt+1))
        q.append((num-1, cnt+1))

