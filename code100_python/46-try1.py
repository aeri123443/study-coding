'''
p.471 46. 전력망을 둘로 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/86971
소요시간: 45m 27s
'''

def dfs(a, b, graph, visited, start): 
    for neighbor in graph[start]:
        if not neighbor in visited:
            if (start==a and neighbor==b) or (start==b and neighbor==a):
                continue
            visited.add(neighbor)
            dfs(a, b, graph, visited, neighbor)
    return visited

def solution(n, wires):
    # 그래프 생성
    graph = {i+1:[] for i in range(n)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    # 하나씩 끊어보기
    min_result = n
    for a,b in wires:
        visited_a = set([a])
        visited_a = dfs(a, b, graph, visited_a, a)
        # 한 번 완료했을 때, 모든 노드를 방문했으면 패스 (=끊어도 둘로 나뉘지 않으면 패스)
        if len(visited_a) == n:
            continue
        # 그룹 크기 차 비교 후 누적
        else:
            len_a = len(visited_a)
            len_b = n-len_a
            min_result = min(min_result, abs(len_a-len_b)) 

    return min_result

# 3
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	))
# 0
print(solution(4, [[1,2],[2,3],[3,4]]))
# 1
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
