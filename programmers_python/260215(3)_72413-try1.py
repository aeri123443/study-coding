'''
72413. Lv.3 합승 택시 요금
https://school.programmers.co.kr/learn/courses/30/lessons/72413
30m 07s
'''
from pprint import pprint
def solution(n, s, a, b, fares):
    INF = float('inf')
    graph = [ [INF]*(n+1) for _ in range(n+1)]

    ### 폴로이드-워셜

    # 그래프 초기화
    for i in range(1, n+1):
        graph[i][i]=0
    for c, d, f in fares:
        graph[c][d]=f
        graph[d][c]=f

    for k in range(1, n+1):
        for st in range(1, n+1):
            for en in range(1, n+1):
                graph[st][en] = min(graph[st][en], graph[st][k]+graph[k][en])

    # pprint(graph)

    ### 경유지 K 기준 비용 계산

    min_cost = INF
    for k in range(1, n+1):
        min_cost = min( min_cost, graph[s][k]+graph[k][a]+graph[k][b] )

    return min_cost

print()
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(82)

print()
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(14)

print()
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
print(18)

# print()
# print(solution())
# print()