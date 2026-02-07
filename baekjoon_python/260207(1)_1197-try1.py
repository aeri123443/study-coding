'''
1197. <골드 4> 최소 스패닝 트리
https://www.acmicpc.net/problem/1197
'''

import sys
from pprint import pprint
input = sys.stdin.readline

V, E = map(int, input().split())
edge_list = [] # [node, node, w]
root_list = [i for i in range(V+1)]

# 유니온-파인드 연산

def find(a):
    root = a
    tmp_stack = []
    while root_list[root] != root:
        tmp_stack.append(root)    
        root = root_list[root]
    
    if len(tmp_stack) > 1:
        for x in tmp_stack:
            root_list[x] = root

    return root
        
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        root_list[root_a] = root_b
        return True
    else: 
        return False

# 값 입력
for _ in range(E):
    edge_list.append(list(map(int, input().split())))

# pprint(edge_list)

anwser = 0
num = 0
edge_list.sort(key=lambda x:x[2])

for a, b, c in edge_list:
    if num==V-1: break
    
    if union(a, b):
        anwser += c
        num += 1

# print(root_list)
print(anwser) 
