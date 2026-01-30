'''
13549. <골드 5> 숨바꼭질 3
https://www.acmicpc.net/problem/13549
'''

import sys
# from collections import deque
import heapq
input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
dp = [-1]*(MAX+1)
q = []
# q = deque()

# 이동 가능한지 묻고 큐에 넣기
def append_q(nx, ns):
    global dp, q

    if 0 <= nx <= MAX and dp[nx] < 0:
        dp[nx] = ns
        # print(nx, dp[nx])
        heapq.heappush(q, [ns, nx])
        # q.append([ns, nx])    

# 시작 위치
dp[N] = 0
q.append([0, N]) # cnt, x
heapq.heappush(q, [0, N])
while q:
    # cur_s, cur_x = q.popleft()
    cur_s, cur_x = heapq.heappop(q)

    append_q(cur_x*2, cur_s)
    append_q(cur_x+1, cur_s+1)
    append_q(cur_x-1, cur_s+1)
    
print(dp[K])