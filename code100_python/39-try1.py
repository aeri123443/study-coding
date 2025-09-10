'''
p.429 39. 너비 우선 탐색 순회
'''

from collections import deque

def solution(graph, start):
    # 그래프 만들기
    tree = {}
    for s, e in graph:
        if s in tree:
            tree[s].append(e)
        else:
            tree[s] = [e]
    # print(tree)

    q = deque([start])
    answer = []
    visited = set()
    while q:
        node = q.popleft()
        if not node in visited:
            answer.append(node)
            visited.add(node)
            if node in tree:
                for child in tree[node]:
                    q.append(child)
    return answer

# [ 1 2 3 4 5 6 7 8 9 ]
print(solution([(1,2), (1,3), (2,4), (2,5), (3,6), (3,7), (4,8), (5,8), (6,9), (7,9)], 1))
# [ 1 2 3 4 5 0 ]
print(solution([(0,1), (1,2), (2,3), (3,4), (4,5), (5,0)], 1))
