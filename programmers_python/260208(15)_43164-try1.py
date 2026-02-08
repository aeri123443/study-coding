
'''
43164. lv3 여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
1h 4m 58s
'''

from pprint import pprint

def solution(tickets):
    n = len(tickets)
    graph = {}
    visited = [False]*n

    tickets.sort(key=lambda x:(x[0],x[1]))
    for i, [a, b] in enumerate(tickets):
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append([b, i]) # 출발지: [도착지, 티켓인덱스]

    # pprint(tickets)
    # pprint(graph)

    answer = ['ICN']
    def dfs(s, cnt):
        # print(s, cnt, answer)
        if cnt == n :
            # print(answer)
            return True
        
        for nxt, nxt_idx in graph[s]:
            if not visited[nxt_idx]:
                visited[nxt_idx] = True
                answer.append(nxt)
                if dfs(nxt, cnt+1):
                    return True
                else:
                    visited[nxt_idx] = False
                    answer.pop()

    dfs('ICN', 0)             
    return answer



print()
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])

print()
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(["ICN", "JFK", "HND", "IAD"])
