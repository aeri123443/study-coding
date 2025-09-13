'''
10845. 큐
https://www.acmicpc.net/problem/10845
'''

from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q)==0: print(-1)
        else: print(q.popleft())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
            if len(q)==0: print(-1)
            else:
                print(q[0])
    elif cmd[0] == 'back':
            if len(q)==0: print(-1)
            else:
                print(q[-1])            
                