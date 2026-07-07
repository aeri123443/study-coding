'''
42892. 길 찾기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/42892

문제 분석: 17m 49s
코드 작성: 48m 20s
디버깅: 2m 50s
total: 1h 09m 0s

- 런타임 에러: 재귀 횟수 초과
- 함수 기본 인자에 리스트 선언: Python에서 함수의 기본 인자(default argument)는 함수가 정의되는 시점에 딱 한 번만 생성되고, 그 이후로는 함수를 호출할 때마다 동일한 리스트 객체를 공유합니다.
'''
import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, x, y, num):
       self.x = x
       self.y = y
       self.num = num
       self.left = None
       self.right = None

# 트리 확인 (디버깅용)
def print_tree(node, level=0, label="Root"):
    if node is not None:
        print("  "*level, f"[{label}] lv{level} num{node.num}", node.left.num if node.left else None , node.right.num if node.right else None)

        # 오른쪽 먼저
        print_tree(node.right, level+1, label="R")
        # 현재 노드의 정보

        # 왼쪽 다음
        print_tree(node.left, level+1, label="L")

# 전위 순회(p - left - right)
def pre_order(node, visited=None):
    if visited is None: visited = []

    if node is None: return []
    visited.append(node.num)
    pre_order(node.left, visited)
    pre_order(node.right, visited)
    return visited

# 후위 순회(left - right - p)
def last_order(node, visited=None):
    if visited is None: visited = []
    if node is None: return []
    last_order(node.left, visited)
    last_order(node.right, visited)
    visited.append(node.num)
    return visited

def solution(nodeinfo):
    # 1. 인풋값 정렬 (-y, x, num) -> 힙큐로 구현하면 더 빨라질듯
    sorted_nodes = []
    for i, [x, y] in enumerate(nodeinfo):
        sorted_nodes.append( (-y, x, i+1) )
    sorted_nodes.sort()
    # print(sorted_nodes)

    # 2. 그래프 구현
    rt_params = sorted_nodes[0]
    rt_node = Node(rt_params[1], -rt_params[0], rt_params[2])
    for y_rv, x, num in sorted_nodes:
        y = -y_rv
        if rt_node.y == y: continue

        # x좌표 기준으로 그래프 구현
        pt_node = rt_node
        while True:
            # 포인터 노드보다 작으면 왼쪽으로
            if x < pt_node.x:
                # 왼쪽에 노드가 있으면 포인터를 왼쪽으로
                if pt_node.left:
                    pt_node = pt_node.left
                # 없으면 배치 후 탈출
                else:
                    pt_node.left = Node(x, y, num)
                    break
            # 포인터 노드보다 크면 오른쪽으로 (x값이 같은 경우는 없음)
            else:
                # 오른쪽에 노드가 있으면 포인터를 오른쪽으로
                if pt_node.right:
                    pt_node = pt_node.right
                # 없으면 배치 후 탈출
                else:
                    pt_node.right = Node(x, y, num)
                    break

    # print_tree(rt_node)
    # 3. 그래프 순회
    return [pre_order(rt_node), last_order(rt_node)]

# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

# 최소케이스
print(solution([[1,0]]))
