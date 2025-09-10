'''
p.432 40. 다익스트라 알고리즘
'''

from collections import deque

def solution(graph, start):
    not_visited = {g for g in graph}
    chart = {g:[99,99] for g in graph}

    chart[start] = [0,start]
    now = start
    while not_visited:
        # 방문하지 않은 것들 중 제일 작은 값 선택
        temp_cost = min([chart[x][0] for x in not_visited])
        now = [c for c in chart if chart[c][0]==temp_cost][0]
        # 이어지는 다음 노드를 확인한 후
        # 이어지는 노드 자체의 최소비용과, 현재 노드를 거쳤을 때의 비용을 비교
        # 작은 놈 넣기
        for e in graph[now]:
            if chart[e][0] > chart[now][0]+graph[now][e]:
                chart[e] = [chart[now][0]+graph[now][e], now]
        not_visited.remove(now)
        
    # 정답 뽑아내기
    answer1 = {c:chart[c][0] for c in chart}

    answer2 = {}
    for c in chart:
        target = chart[c][1]

        if c == chart[c][1]:
            answer2[c] = [c]
            continue

        temp = deque([c])
        while True:
            temp.appendleft(target)
            if target == chart[target][1]:
                break
            target = chart[target][1]

        answer2[c] = list(temp)
    return [answer1, answer2]

# [{'A': 0, 'B': 4, 'C': 3}, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}]
print(solution({ 'A': { 'B': 9, 'C': 3 }, 'B': { 'A': 5 }, 'C': { 'B': 1 } }, 'A'))
# [{'A': 0, 'B': 1, 'C': 6, 'D': 7}, {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']}]
print(solution({ 'A': { 'B': 1 },'B': { 'C': 5 },'C': { 'D': 1 }, 'D': {} }, 'A'))
