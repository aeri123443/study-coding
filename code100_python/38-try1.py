'''
p.426 38. 깊이 우선 탐색 순회
'''

from collections import deque

def solution(graph, start):
    # 그래프 만들기
    tree = {}
    # tree = [tree{s}=e for s, e in graph]
    for s, e in graph:
        if s in tree:
            tree[s].append(e)
        else:
            tree[s] = [e]

    visited = set()
    answer = []
    def dfs(answer, visited, start):
        # print(start)
        visited.add(start)
        answer.append(start)
        if start in tree:
            for next in tree[start]:
                if not next in visited:
                    dfs(answer, visited, next)
        return answer
    
    return dfs(answer, visited, start)


# [ A B C D E ]
print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
# [ A B D E F C ]
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))
