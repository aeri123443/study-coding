'''
# 2024 상반기 오후 2번 · 색깔 트리
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/color-tree

케이스
    - 루트 노드 모아둬야하는지 -> 시간초과시 확인

nodes = [Node...]
class 노드
    - 고유 번호 m_id
    - 부모 노드 p_id(-1이면 이 노드가 루트임)
    - 최대 깊이 max_depth(100) (해당 노드를 루트로 하는 서브트리의 최대 깊이, 자기 자신의 깊이:1 )
    - changed: (turn, color) # 최근 변경된 턴 수와 컬러. 초깃값은 노드 생성 턴 수

def 재귀로 색 종류 반환
    f(n): 현재 보고 있는 노드 번호, node 색 그룹 결과값[]
        - 최신 색상 변경 사항 넘김
        f(n+1):
            - 최신 색상 변경 사항 업데이트
            - 컬러 그룹(defalutdict) 반환
        - 컬러 그룹(defalutdict) 누적
        - 각 노드에 컬러 그룹 추가
        - 최종 결과(각 노드에 컬러 그룹 추가) 반환
    f(n) -> f(n+1) :
        - 최신 색상 변경 사항 넘김
    f(n+1):
        - 최신 색상 변경 사항 업데이트4
    f(n+1) -> f(n):
        -
명령 Q(100_000)
1. 노드 추가 (20_000) -> O(200_000)
    - 100, m_id, p_id, color, max_depth
    - 루트 노드일 경우
        - 바로 추가
    - 아닐 경우
        - 기존 노드 모순 확인
            - 루트까지 타고 올라가며 모든 상위 노드 확인 O(100)
        - 추가 가능하면 추가, 안되면 넘어감
2. 색깔 변경 (50_000) -> O(50_000)
    - 200, m_id, color
    - m_id를 루트로 하는 서브트리의 모든 노드 색을 color로 변경
    - last_changed: (turn, color) # 최근 변경된 턴 수와 컬러, 업데이트

3. 색깔 조회 (20_000) -> O(200_000)
    - 300, m_id
    - m_id 색
    - 위로 올라가면서 현재 턴 수 기준 색상 확인 O(100)
        - 현재 턴 이전에 변경된 색 중, 가장 최근에 변경된 정보 반환
4. 점수 조회 (100) -> O(100*(20_000+40_000+100_000)) -> O(16_000_000)
    - 400
    - 모든 노드의 가치의 합
        - 가치: 해당 노드를 루트로 하는  서브트리의 서로 다른 색상 수
        [!] 각 노드별 서브트리 색상 종류 모두 구한 후 sum해야함
    - 루트 노드 찾기 O(20_000)
    - 재귀 - 탑->다운으로 색상 정보 업데이트 후 다운 -> 탑으로 컬러그룹 정보 반환 O(20_000*2)
    - 각 노드 결과의 합 구하기 O(20_000*5)

# 문제 1회독 4m 29s
# 문제 2회독 8m 2s
# 설계 35m 36s
# 표 작성 및 시간복잡도 재점검 6m 21s
# non-fail pass.
# 총 소요시간 2h 47m 45s
'''

# 케이스
#     - 루트 노드 모아둬야하는지 -> 시간초과시 확인

from collections import defaultdict, deque

DEBUG = False
Q = int(input())
nodes = {} # nodes = [Node...]

class Node:
    def __init__(self, turn, m_id, p_id, color, max_depth):
        self.n_id = m_id # 고유 번호 m_id
        self.p_id = p_id # 부모 노드 p_id(-1이면 이 노드가 루트임)
        self.max_depth = max_depth # 해당 노드를 루트로 하는 서브트리의 최대 깊이, 자기 자신의 깊이:1
        self.changed = (turn, color) # 최근 변경된 턴 수와 컬러. 초깃값은 노드 생성 턴 수
        self.child = [] # [child_node_num, ...]
# 전역 입력 5m 24s


# 노드 추가 가능 여부 판단
# 상위 노드의 모순 확인
def can_add(p_id):
    cur_depth = 2

    while p_id != -1:
        # nodes[p_id].max_depth >= cur_depth -> 통과
        if nodes[p_id].max_depth < cur_depth:
            return False

        cur_depth += 1
        p_id = nodes[p_id].p_id

    return True

# 1. 노드 추가
def add_node(t, line): # 17m 59s
    m_id, p_id, color, max_depth = line
    # 루트 노드이거나, 루트가 아닌데 모순 발생x 경우에만 추가
    if p_id == -1 or can_add(p_id):
        nodes[m_id] = Node(t, m_id, p_id, color, max_depth)
        if p_id != -1: nodes[p_id].child.append(m_id)

# 2. 색깔 변경
def update_color(t, line): # 4m 7s
    m_id, color = line
    nodes[m_id].changed = (t, color)

# 모든 노드 색 변경
# 탑다운으로 최신 변경사항 누적
def update_tree_color(r_id, recent_changed):
    node = nodes[r_id]


    # 색상 변경 조건
    # 상위 색 변경 명령이 지금보다 최신이어야 함
    recent = max(recent_changed, node.changed)
    node.color = recent[1]

    for ch in node.child:
        update_tree_color(ch, recent)

# 색 종류 반환 -> 재귀 헷갈려서 bfs로 변경
def get_color_info(color_info, r_id):

    # 탐색 루트
    stack = [r_id]
    q = deque([r_id])
    while q:
        cur_id = q.popleft()

        for child in nodes[cur_id].child:
            q.append(child)
            stack.append(child)

    # 컬러 인포 업데이트
    while stack:
        node_id = stack.pop()
        node = nodes[node_id]

        color_group = defaultdict(int)
        color_group[node.color] += 1

        # 자식의 컬러그룹 정보를 업데이트
        for c_id in node.child:
            for k,v in color_info[c_id].items():
                color_group[k]+=v

        color_info[node_id] = color_group

# 4. 점수 조회
# - 모든 노드의 가치의 합
# - 가치: 해당 노드를 루트로 하는  서브트리의 서로 다른 색상 수
# [!] 각 노드별 서브트리 색상 종류 모두 구한 후 sum해야함
def get_score(): # 재귀 시도 50m 23s + bfs 26m 47s
    # 루트 노드 찾기
    root_ids = [node_id for node_id, node in nodes.items() if node.p_id == -1]

    # 모든 노드 색 변경
    for r_id in root_ids:
        update_tree_color(r_id, nodes[r_id].changed)

    color_info = defaultdict()
    for r_id in root_ids:
        get_color_info(color_info, r_id)

    score = 0
    for dic in color_info.values(): # 아그냥 set으로 관리할걸
        score += len(dic)*len(dic)

    return score

# 3. 색깔 조회
def get_node_color(node_id): # 7m 28s
    node = nodes[node_id]
    recent = node.changed

    p_id = node.p_id
    while p_id != -1:
        p_node = nodes[p_id]
        recent = max(recent, p_node.changed)
        p_id = p_node.p_id
    return recent[1]

def main():
    answer = []
    for t in range(1, Q+1):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 1. 노드 추가
        if cmd == 100:
            add_node(t, line[1:])
        # 2. 색깔 변경
        elif cmd == 200:
            update_color(t, line[1:])
        # 3. 색깔 조회
        elif cmd == 300:
            color = get_node_color(line[1])
            answer.append(color)
        # 4. 점수 조회
        elif cmd == 400:
            score = get_score()
            answer.append(score)

        if DEBUG: print()
    print('\n'.join(map(str, answer)))

main()
