'''
42892. 길 찾기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/42892

문제 분석: 11m 59s
코드 작성: 17m 51s
디버깅: 2m 23s
total: 32m 15s
sys.setrecursionlimit(10^6)가 아니라 10**6 !!
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
    rt_params = sorted_list[0]
    rt_node = Node(rt_params[1], -rt_params[0], rt_params[2])

    for rv_y, x, num in sorted_list:
        if rt_node.x == x: continue
        y = -rv_y

        pt_node = rt_node
        while True:
            # x값이 pt_node보다 작으면 왼쪽
            if x < pt_node.x:
                # 왼쪽에 값이 있으면 이동, 없으면 삽입 후 탈출
                if pt_node.left:
                    pt_node = pt_node.left
                else:
                    pt_node.left = Node(x, y, num)
                    break
            # x값이 pt_node보다 크면 오른쪽 (x가 같은 경우는 없음.)
            else:
                # 오른쪽에 값이 있으면 이동, 없으면 삽입 후 탈출
                if pt_node.right:
                    pt_node = pt_node.right
                else:
                    pt_node.right = Node(x, y, num)
                    break
    # 그래프 구현 확인(디버깅)
    # print_graph(rt_node)

    pre_list = []
    post_list = []
    order(rt_node, pre_list, post_list)
    return [pre_list, post_list]


# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))