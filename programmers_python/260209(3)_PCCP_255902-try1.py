
'''
Lv. 2 [PCCP 모의고사 #1] 2번 - 체육대회
https://school.programmers.co.kr/learn/courses/20847/lessons/255901
테케 돌려보니 시간초과 날 것 같아서 노선 틂..
'''

'''
각 완두콩은 자가 수분해서 정확히 4개의 완두콩 후손을 남긴다.
잡종 완두콩(Rr)은 자가 수분해서 첫째는 RR, 둘째와 셋째는 Rr, 넷째는 rr 형질의 후손을 남긴다.
순종 완두콩(RR, rr)은 자가 수분해서 자신과 같은 형질의 후손을 남긴다.

완두콩의 세대와 해당 세대에서 몇 번째 개체인지를 알면 형질을 바로 계산하는 프로그램을 만들려 합니다.
'''

# from pprint import pprint

def solution(queries):
    max_depth = max(queries, key=lambda x:x[0])[0]
    graph = [[] for _ in range(max_depth)]
    graph[0] = ['Rr']

    # 그래프 만들기
    for i in range(1, max_depth):
        for x in graph[i-1]: # 이전 행 기준으로 현재 행 만들기
            if x == 'RR':
                graph[i].extend(['RR', 'RR', 'RR', 'RR'])
            elif x=='rr':
                graph[i].extend(['rr', 'rr', 'rr', 'rr'])
            else: # Rr
                graph[i].extend(['RR', 'Rr', 'Rr', 'rr'])
    # print(graph)

    return [graph[i-1][j-1] for i,j in queries]

print()
print(solution([[3, 5]]))
print(["RR"])

print()
print(solution([[3, 8], [2, 2]]))
print(["rr", "Rr"])

print()
print(solution([[3, 1], [2, 3], [3, 9]]))
print(["RR", "Rr", "RR"])

print()
print(solution([[4, 26]]))
print(["Rr"])

# print(4**15) 1073741824
print()
print(solution([[16, 1073741824]]))
print(["Rr"])