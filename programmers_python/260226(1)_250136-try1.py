'''
250136. lv.2 [PCCP 기출문제] 2번 / 석유 시추
https://school.programmers.co.kr/learn/courses/30/lessons/250136
27m 57s
'''
from collections import deque

# 0이면 빈 땅, 1이면 석유가 있는 땅
def solution(land):
    N, M = len(land), len(land[0])
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = [[False]*M for _ in range(N)]

    answer = [0]*M

    
    # 석유 그룹 찾기
    def find_group(si, sj):
        j_set = set()

        cnt = 1
        j_set.add( sj )
        q = deque( [ (si, sj) ])
        visited[si][sj] = True

        while q:
            ci, cj = q.popleft()

            for di, dj in move:
                ni, nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and land[ni][nj]==1:
                    cnt += 1
                    visited[ni][nj] = True
                    j_set.add( nj )
                    q.append( (ni, nj) )

        # j좌표에 대해 cnt만큼 더함
        for j in j_set:
            answer[j] += cnt

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and land[i][j]==1:
                find_group(i,j)
    # print(visited)
    # print(j_set)

    # print(answer)
    return max(answer)

print()
print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(9)

print()
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
print(16)

# print()
# print(solution())
# print()