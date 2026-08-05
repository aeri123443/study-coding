'''
색깔 트리: 2024 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/color-tree

문제 분석: 54m 56s
  - [시간 소요] depth 조건을 못 보고 시간 복잡도가 넘을 것이라고 판단하고 300 cmd 전략에 시간 소요, 200 cmd에서는 gpt와 상의하며 bit mask 공부.
코드 1차 작성: 2h 06m 00s
코드 2차 작성: 14m 40s
  - [TC28 시간초과] 루트 노드(p==-1)을 리스트에 넣으면 마지막 인덱스를 반환하는데, 해당 케이스를 놓쳐서 무한루프에 빠짐

총 소요 시간: 3h 15m 38s
'''
from collections import deque

##################################################
##### 전역 선언부
##################################################
MAX = 100_000
Q = -1

graph = [None]*(MAX+1)
roots = set() # 루트 노드 목록
nodes = set() # 현재 있는 노드만 접근하는 용도!

class Node:
    def __init__(self, q, idx, p, c, md):
        self.idx = idx
        self.p = p
        self.c = 1 << (c-1) # 비트마스크로 기록
        self.md = md
        self.change = (q, self.c) # 변경 명령 시점, 변경 색
        self.child = [] # 자식 목록
        self.remain = md # 후처리: 부모까지 봤을 때 총 얼마가 남았는지

##################################################
##### 보조 함수
##################################################
### 최신 변경 업데이트
def update_color(dp, r_num):
    p_to_child = [] # 부모 -> 자식 rank 순서로 stack에 담음, 향후 pop하며 자식 순으로 접근. 쓰다보니 후위 순회를 하면 되었나?

    r_node = graph[r_num]
    q = deque([(r_num, r_node.change)])
    dp[r_num] = r_node.change
    p_to_child.append(r_num)

    while q:
        num, change = q.popleft()
        node = graph[num]

        if change[0] < node.change[0]:
            change = node.change

        # 색 변경
        dp[num] = change[1]

        for nxt in node.child:
            q.append((nxt, change))
            p_to_child.append(nxt)

    return p_to_child


# 색상 종류 누적
def count_color(dp, p_to_child):
    while p_to_child:
        cur_num = p_to_child.pop()
        cur_node = graph[cur_num]

        # 자식의 색상 수에서 업데이트
        tmp_result = 0
        for c in cur_node.child:
            tmp_result = tmp_result | dp[c]
            # print()
        dp[cur_num] = tmp_result | dp[cur_num]
        # print()


### 점수 조회
def get_score():
    dp = [0]*(MAX+1)
    # 전체 탐색으로 최신 색 업데이트
    for rt in roots:
        p_to_child = update_color(dp, rt)
        # print()
        # 색상 종류 누적
        count_color(dp, p_to_child)
        # print()
    # print()

    # 점수 계산
    score = 0
    for node in nodes:
        score += (bin(dp[node]).count('1'))**2

    return score

### 색상 조회
def get_color(idx):
    node = graph[idx]
    change = node.change

    if node.p == -1:
        return change[1]

    parent = graph[node.p]

    # 부모 타고가면서, 업데이트 명령이 새로 있었는지 확인
    while parent:
        # print(parent.idx, parent.p)

        if change[0] < parent.change[0]:
            change = parent.change

        if parent.p == -1:
            break
        parent = graph[parent.p]

    # print()
    return change[1]



##################################################
##### 메인 로직
##################################################
def main():
    global Q

    Q = int(input())
    answer = []

    for q in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]
        # print(cmd, line, roots)
        ## 100: 노드 추가
        if cmd == 100:
            idx, p, c, md = line[1:]
            new_node = Node(q, idx, p, c, md)
            # p == -1이면 새 그래프로 처리
            if p == -1:
                graph[idx] = new_node
                roots.add(idx)
                nodes.add(idx)
            # p > 0이면 부모 노드 확인
            else:
                p_node = graph[p]
                if p_node.remain > 1:
                    new_node.remain = min(p_node.remain-1, md)
                    graph[idx] = new_node
                    p_node.child.append(idx)
                    nodes.add(idx)

        ### 200: 색 변경
        elif cmd == 200:
            idx, color = line[1:]
            graph[idx].change = (q, 1 << (color-1) )
        ### 300: 색 조회
        elif cmd == 300:
            color = get_color(line[1])
            answer.append(len(bin(color))-2)
            # print(q, cmd, len(bin(color))-2)
            # print()
        ### 400: 점수 조회
        elif cmd == 400:
            score = get_score()
            answer.append(score)
            # print(q, cmd, score, len(nodes))
        # print()
    print('\n'.join(map(str, answer)))

main()