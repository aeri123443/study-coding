'''
42892. 길 찾기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/42892

분할정복으로 풀어보기
'''
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None

def print_graph(node):
    if node is None: return
    print(f"num:{node.num}, left:{node.left.num if node.left else None } right:{node.right.num if node.right else None}")
    print_graph(node.left)
    print_graph(node.right)

def order(node, pre_list, post_list):
    if node is None: return
    pre_list.append(node.num)
    order(node.left, pre_list, post_list)
    order(node.right, pre_list, post_list)
    post_list.append(node.num)

def solution(nodeinfo):
    # 1. 리스트 정렬
    sorted_list = []
    for i, [x,y] in enumerate(nodeinfo):
        sorted_list.append( (-y, x, i+1) )
    sorted_list.sort()

    # 2. 그래프 구현
    def build_tree(nodes):
        if not nodes: return None

        y_rv, x, num = nodes[0]
        root = Node(x, -y_rv, num)
        left_group = []
        right_group = []

        for nxt_node in nodes[1:]:
            if nxt_node[1] < root.x:
                left_group.append(nxt_node)
            else:
                right_group.append(nxt_node)

        root.left = build_tree(left_group)
        root.right = build_tree(right_group)

        return root

    rt_node = build_tree(sorted_list)
    # 그래프 구현 확인(디버깅)
    # print_graph(rt_node)

    pre_list = []
    post_list = []
    order(rt_node, pre_list, post_list)
    return [pre_list, post_list]


# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))