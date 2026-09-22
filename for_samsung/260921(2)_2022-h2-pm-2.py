'''
산타의 선물 공장 2:  2022 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory-2/description

문제 분석: 40m 29s
코드 작성: 1h 14m 04s -> 너무 복잡하게 풀고있는 것 같아서 중단, 기본함수부터 다시 짜기
'''

# =====================================
# 전역 및 클래스
# =====================================
DEBUG = True
N, M, Q = -1, -1, -1

belts = []
items = []

class Node:
    def __init__(self, p_num):
        self.p_num = p_num
        self.prev = None
        self.next = None

class Belt: # 연결리스트
    def __init__(self, b_num):
        self.b_num = b_num
        self.head = None
        self.rear = None
        self.len = 0

# =====================================
# 보조 함수
# =====================================

# 공장 설립 (초기 데이터 입력)
def init_data(line):
    global N, M, belts, items

    N, M = line[1], line[2]
    belts = [Belt(i) for i in range(N+1)]
    items = [None] * (M+1)

    for p_num in range(1, M+1):
        idx = p_num+2
        b_num = line[idx]

        belt = belts[b_num]
        new_node = Node(p_num)

        # 길이가 0일 경우, head & rear 업데이트
        if belt.len == 0:
            belt.head = new_node
            belt.rear = new_node
        else:
            belt.rear.next = new_node
            new_node.prev = belt.rear
            belt.rear = new_node

        belt.len += 1 # 길이 업데이트

        items[p_num] = new_node

# 물건 모두 옮기기
def move_all_node(m_src, m_dst):
    b_src = belts[m_src]
    b_dst = belts[m_dst]

    if b_src.len == 0:
        # b_src에 아무것도 없으므로, 변화가 일어나지 않음
        return b_dst.len

    elif b_dst.len == 0:
        # src의 모든 것을 옮김
        b_dst.head = b_src.head
        b_dst.rear = b_src.rear
        b_dst.len = b_src.len

        b_src.head = None
        b_src.rear = None
        b_src.len = 0

        return b_dst.len

    else:
        # 두 리스트 연결
        b_src.rear.next = b_dst.head
        b_dst.head.prev = b_src.rear

        # dst 업데이트
        b_dst.head = b_src.head
        b_dst.len += b_src.len

        # src 업데이트
        b_src.head = None
        b_src.rear = None
        b_src.len = 0

        return b_dst.len

def replace_head_node(m_src, m_dst):
    b_src = belts[m_src]
    b_dst = belts[m_dst]

    if b_src.len == 0 and b_dst.len==0:
        return 0

    # belt 앞에 새로운 head를 추가
    def link_head(new_head, belt):

        # belt에 아무것도 없을 때는 그냥 바로 추가
        if belt.len == 0:
            belt.head = new_head
            belt.rear = new_head
        else:
            new_head.next = belt.head
            belt.head.prev = new_head
            belt.head = new_head

        belt.len += 1

    # dst의 헤드만 이동
    if b_src.len == 0:
        head_dst = b_dst.head
        b_dst.head = b_dst.head.next
        b_dst.len -= 1
        link_head(head_dst, b_src)
        return b_dst.len

    # src의 헤드만 이동
    if b_dst.len == 0:
        head_src = b_src.head
        b_src.head = b_src.head.next
        b_src.len -= 1
        link_head(head_src, b_dst)
        return b_dst.len

    head_src = b_src.head
    head_dst = b_dst.head

    b_src.head = b_src.head.next
    b_dst.head = b_dst.head.next
    b_src.len -= 1
    b_dst.len -= 1

    # dst의 원래 헤드를 b_src 앞에 연결
    link_head(head_dst, b_src)

    # src의 원래 헤드를 dst 앞에 연결
    link_head(head_src, b_dst)

    return b_dst.len

# =====================================
# 메인 로직
# =====================================
def main():
    global Q

    Q = int(input())
    answer = []

    for q in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 1. 공장 설립
        if cmd == 100:
            init_data(line)

        # 2. 물건 모두 옮기기
        elif cmd == 200:
            m_src, m_dst = line[1], line[2]
            dst_len = move_all_node(m_src, m_dst)
            answer.append(dst_len)

        # 3. 앞 물건만 교체
        elif cmd == 300:
            m_src, m_dst = line[1], line[2]
            dst_len = replace_head_node(m_src, m_dst)
            answer.append(dst_len)

        # 4. 물건 나누기

        # 5. 선물 정보 얻기
        # 6. 벨트 정보 얻기
        if DEBUG: print()
main()