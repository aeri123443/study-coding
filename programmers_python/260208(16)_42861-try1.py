
'''
42861. lv3 섬 연결하기
https://school.programmers.co.kr/learn/courses/30/lessons/42861
19m 27s
'''

def solution(n, costs):
    graph = sorted(costs, key=lambda x: x[2])
    parents = [i for i in range(n)]
    cnt = 0
    answer = 0

    # print(graph)

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
        
    def union(a, b):
        p_a = find(a)
        p_b = find(b)

        if p_a != p_b:
            parents[p_a] = p_b
            return True
        else:
            return False
        
    for a, b, c in graph:
        if union(a, b):
            cnt += 1
            answer += c
            # print(cnt, answer)

            if cnt == n-1:
                return answer

print()
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(4)