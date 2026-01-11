'''
1697. <실버1> 숨바꼭질
https://www.acmicpc.net/problem/1697
'''

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
max_len = 2*K-N+1
visited = [-1]*max_len
# print(memo)

def is_possible(x, cnt):
    # visited 인덱스 범위 안인지
    # 방문하지 않은 곳인지
    if (0<=x<max_len) and (visited[x]<0):
        return True
    else:
        return False
        
def bfs(start_node):
    visited[start_node]=0

    q = deque()
    # q.append([cur, nxt, cnt])
    next_nodes = [start_node-1, start_node+1, start_node*2]
    for next_node in next_nodes:
        if is_possible(next_node, 1):
            visited[next_node]=1
            q.append([start_node, next_node, 1])
    # print(visited)

    while q:
        cur, nxt, cnt = q.popleft()
        new_cnt = cnt+1
        next_nodes = [nxt-1, nxt+1, nxt*2]
        for next_node in next_nodes:
            if is_possible(next_node, new_cnt):
                visited[next_node]=new_cnt
                q.append([start_node, next_node, new_cnt])
        

if N==K: print(0)
elif N>K: print(N-K)
else:
    bfs(N)
    print(visited[K])