
'''
49191. lv3 순위
https://school.programmers.co.kr/learn/courses/30/lessons/49191
'''

from pprint import pprint
from collections import defaultdict, deque

def solution(n, results):
    win_lose = defaultdict(list)
    lose_win = defaultdict(list)
    rank = [[0, 0] for _ in range(n+1)] # [0 승, 1 패]

    for w, l in results:
        win_lose[w].append(l) 
        lose_win[l].append(w)
    # pprint(win_lose)
    # pprint(lose_win)
    # print(rank)
    
    def bfs_win(s):
        q = deque()
        q.append(s)
        visited[s] = True
        cnt = 0

        while q:
            cur = q.popleft()
            cnt += 1

            for nxt in win_lose[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    # cnt += 1
        return cnt

    def bfs_lose(s):
        q = deque()
        q.append(s)
        visited[s] = True
        cnt = 0

        while q:
            cur = q.popleft()
            cnt += 1

            for nxt in lose_win[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    # cnt += 1
        return cnt
        
    for i in range(1, n+1):
        # print(i, '...')

        # 이겼는지
        visited = [False]*(n+1)
        for nxt in win_lose[i]:
            if not visited[nxt]:
                win_cnt = bfs_win(nxt)
                # print(win_cnt)
                # print(visited)
                rank[i][0] += win_cnt

        # 졌는지
        visited = [False]*(n+1)
        for nxt in lose_win[i]:
            if not visited[nxt]:
                lose_cnt = bfs_lose(nxt)
                # print(lose_cnt)
                # print(visited)
                rank[i][1] += lose_cnt
    # pprint(rank)
    
    answer = 0
    for i in range(1, len(rank)):
        w, l = rank[i]
        if w+l == n-1:
            answer+=1

    return answer

print()
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(2)
