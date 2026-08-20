'''
코드트리 메신저: 2023 하반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-messenger/description

집중해서 다시 풀기 !!
'''
from collections import deque, defaultdict

# =============================================
# 전역 및 클래스
# =============================================

class Node:
    def __init__(self, idx, p, a):
        self.idx = idx # 채팅방 고유 번호
        self.p = p # 부모
        self.a = a # 권한 세기
        self.toggle = True # 알림 설정 토글
        self.depth = 0 # 깊이
        self.cnt = 0 # 해당 채팅방까지 도달하는 알림의 수
        self.children = set() # 자식 정보
        self.remains = defaultdict(int) # {remain: int}, remain만큼 위로 올라갈 수 있는 것이 int개 남음!

N, Q = -1, -1

graph = [Node(0, -1, 0)]
# =============================================
# 보조 함수
# =============================================

# 최초 1회 - 노드 생성 및 트리 구성
def make_tree(line):
    tmp_child = [set() for _ in range(N+1)]

    # 노드 생성 및 p, a 업데이트
    for idx in range(1, N+1):
        p, a = line[idx], line[N+idx]
        new_node = Node(idx, p, a)
        graph.append(new_node)
        tmp_child[p].add(idx)

    # 탑다운으로 depth & children 업데이트
    q = deque([0])
    while q:
        cur = q.popleft()
        node = graph[cur]

        for ch in tmp_child[cur]:
            ch_node = graph[ch]
            ch_node.depth = node.depth + 1
            ch_node.children = tmp_child[ch]
            q.append(ch)

    # 하나씩 바텀업으로 cnt & remains 업데이트
    for idx in range(1, N+1):
        node = graph[idx]
        remain = min(node.a, node.depth)

        while remain >= 0:
            if remain > 0: node.remains[remain] += 1
            node.cnt += 1
            remain -= 1
            node = graph[node.p]

def update_remain_info(start_c, d):
    c_node = graph[start_c]

    # 켜졋으면 더하고, 꺼졌으면 뺀다

    remain_info = c_node.remains

    cur_node = c_node
    while remain_info:
        if not cur_node.toggle and cur_node != c_node:
            break

        p_node = graph[cur_node.p]
        p_info = p_node.remains

        new_remain = {}

        for k, v in remain_info.items():
            p_node.cnt += v*d
            if k > 1:
                p_info[k-1] += v*d
                if p_info[k-1] <= 0:
                    del p_info[k-1]
                new_remain[k-1] = v

        remain_info = new_remain
        cur_node = p_node

def update_a(c, new_power):
    c_node = graph[c]

    # 기존의 a만큼 올라가면서 cnt--
    remain = min(c_node.a, c_node.depth)
    diff = new_power - c_node.a

    cur_node = graph[c]

    while remain>=0:
        cur_node.cnt -= 1
        if remain > 0:
            cur_node.remains[remain] -= 1
            if cur_node.remains[remain] <= 0 : del cur_node.remains[remain]

        if not cur_node.toggle: break
        cur_node = graph[cur_node.p]
        remain -= 1

    # 새로운 a만큼 올라가면서 cnt++
    c_node.a = new_power
    remain = min(c_node.a, c_node.depth)

    cur_node = graph[c]

    while remain>=0:
        cur_node.cnt += 1
        if remain > 0:
            cur_node.remains[remain] += 1

        if not cur_node.toggle: break

        cur_node = graph[cur_node.p]
        remain -= 1


def toggle_item(c):
    c_node = graph[c]
    c_node.toggle = not c_node.toggle

    d = 1 if c_node.toggle else -1
    update_remain_info(c, d)

# =============================================
# 메인 로직
# =============================================
def main():
    global Q, N

    N, Q = map(int, input().split())
    ans = []

    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 사내 메신저 준비
        if cmd == 100:
            make_tree(line)

        # 알림망 토글
        elif cmd == 200:
            toggle_item(line[1])

        # 권한 세기 변경
        elif cmd == 300:
            c, power = line[1:]
            update_a(c, power)

        # 부모 교환
        elif cmd == 400:
            c1, c2 = line[1:]
            c1_node, c2_node = graph[c1], graph[c2]

            # 기존 노드만큼을 뺀다
            if c1_node.toggle: update_remain_info(c1, -1)
            if c2_node.toggle: update_remain_info(c2, -1)

            # 부모 교환
            c1_node.p, c2_node.p = c2_node.p, c1_node.p

            # 다시 업데이트
            if c1_node.toggle: update_remain_info(c1, 1)
            if c2_node.toggle: update_remain_info(c2, 1)

        # 알림 수
        elif cmd == 500:
            c = line[1]
            c_node = graph[c]
            ans.append(c_node.cnt-1)

        # print()

    print('\n'.join(map(str, ans)))

main()