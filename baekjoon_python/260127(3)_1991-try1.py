'''
1991. <실버 1> 트리 순회
https://www.acmicpc.net/problem/1991
'''

import sys
from pprint import pprint
input = sys.stdin.readline

N = int(input())
graph = {}
answer = []

# 전위 순회
def pre_explore(node):
    global answer
    child1, child2 = graph[node]
    answer.append(node)
    if child1 != '.': pre_explore(child1)
    if child2 != '.': pre_explore(child2)

# 중위 순회
def mid_explore(node):
    global answer
    child1, child2 = graph[node]
    if child1 != '.': mid_explore(child1)
    answer.append(node)
    if child2 != '.': mid_explore(child2)

# 후위 순회
def last_explore(node):
    global answer
    child1, child2 = graph[node]
    if child1 != '.': last_explore(child1)
    if child2 != '.': last_explore(child2)
    answer.append(node)

for _ in range(N):
    a, b, c = input().split()
    graph[a] = [b,c]

# pprint(graph)

# 전위 순회
answer = []
pre_explore('A')
print(''.join(answer))

# 중위 순회
answer = []
mid_explore('A')
print(''.join(answer))

# 후위 순회
answer = []
last_explore('A')
print(''.join(answer))
