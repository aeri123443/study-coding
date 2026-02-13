'''
5639. <골드 4> 이진 검색 트리
https://www.acmicpc.net/problem/5639
왼쪽/오른쪽 재귀적으로 분할 후 붙이는 방향이 더 좋음
'''

import sys
# from pprint import pprint
sys.setrecursionlimit(int(1e5))

preorder_list = list(map(int, sys.stdin.readlines()))
graph = {v:[0,0] for v in preorder_list}
n = len(preorder_list)
# print(preorder_list)
# pprint(graph)

# 트리 생성: target num, parent node
def make_tree(t, p):
    # 작으면 왼쪽으로
    if t < p:
        if graph[p][0]: 
            make_tree(t, graph[p][0])
        else: 
            graph[p][0] = t
    # 크면 오른쪽으로
    else:
        if graph[p][1]:
            make_tree(t, graph[p][1])
        else:
            graph[p][1] = t

root_node = preorder_list[0]
for i in range(1, n):
    make_tree(preorder_list[i], root_node)

# pprint(graph)

# 후위 순회
postorder_list = []
def postorder(node):
    global preorder_list

    l, r = graph[node]
    if l: postorder(l)
    if r: postorder(r)
    postorder_list.append(node)

# postorder(root_node)
# print('\n'.join(map(str, postorder_list)))
