'''
N개의 점 중 M개 고르기
https://www.codetree.ai/ko/trails/complete/curated-cards/test-choose-m-out-of-n-points/description

총 소요 시간: 18m 02s
'''
from itertools import combinations, permutations
INF = float('inf')
N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]
for a in range(N):
    ar, ac = points[a]
    for b in range(N):
        br, bc = points[b]
        memo[a][b] = (ar-br)**2 + (ac-bc)**2

answer = INF
for com in combinations([i for i in range(N)], M):
    max_num = -INF
    for (x, y) in permutations(com, 2):
        max_num = max(max_num, memo[x][y])
    answer = min(max_num, answer)
print(answer)