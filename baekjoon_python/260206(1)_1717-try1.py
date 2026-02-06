'''
1717. <골드 5> 집합의 표현
https://www.acmicpc.net/problem/1717
'''

import sys
from pprint import pprint

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [i for i in range(n+1)]

# 루트 노드 찾기
def find(a):
    # 찾는 과정에서 거친 노드들 업데이트
    arr = []
    x = a

    while graph[x]!=x:
        arr.append(x)
        x = graph[x]
    
    for i in range(len(arr)):
        tmp = arr[i]
        graph[tmp] = x
    # print(x)

    return x

# 집합 합치기
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        graph[root_b] = root_a

for _ in range(m):
    c, a, b = map(int, input().split())

    if c==0: # 합치기
        union(a, b)
    else: # 같은 집합 확인
        print( 'YES' if find(a) == find(b) else 'NO')
