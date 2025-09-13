'''
2164. 카드2
https://www.acmicpc.net/problem/2164
'''

from collections import deque
N = int(input())
q = deque([i+1 for i in range(N)])

while True:
    if len(q)==1:
        print(q.popleft())
        break
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)
