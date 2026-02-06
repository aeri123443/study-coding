'''
11657. <골드 4> 타임머신
https://www.acmicpc.net/problem/11657

개선 포인트
answer[node] == inf 인 경우 간선 계산을 하지 않고 바로 업데이트
매 반복마다 변경 확인할 수 있는 플래그를 만들고, 변경이 없으면 바로 조기 종료
인접 리스트는 의미 없음 -> 어차피 모든 엣지를 순회하니 엣지 리스트로
float('inf')는 상수로 빼두기 INF = float('inf')
'''

import sys
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = [float('inf')]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
# pprint(graph)

# 벨만-포드
answer[1] = 0
for _ in range(N-1):
    for node in range(1, N+1):
        for neighbor, weight in graph[node]:
            if answer[neighbor] > answer[node]+weight:
                answer[neighbor] = answer[node]+weight
# pprint(answer)

# 음의 순환 확인 (-1 반환)
for node in range(1, N+1):
    for neighbor, weight in graph[node]:
        if answer[neighbor] > answer[node]+weight:
            print(-1)
            sys.exit()

# 결과 출력
    # 1번 도시 -> 2번 3번 N번도시 가장 빠른 시간 출력
    # 이때 해당 경로로 가는 버스가 없으면 -1
for i in range(2, N+1):
    if answer[i]==float('inf'):
        answer[i] = -1

print('\n'.join(map(str, answer[2:])))
