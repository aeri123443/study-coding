'''
산타의 선물 공장 2:  2022 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory-2/description

문제 재설계: 16m 09s
코드 1차 작성: 1h 05m 24s
    - [TC4 error]  get_node에서 n==0일 때를 처리했으니 괜찮다고 생각해서 pop_list에서 n==0일때를 처리하지 않음 -> new_list.rear.next에서 NoneType 에러
            코드 2차 작성애서 해당사항 반영
코드 2차 작성: 3m 24s
'''

# ====================================
# 전역 및 클래스
# ====================================
DEBUG = False
N, M, Q = -1, -1, -1

belts = []
presents = []

class Present: # Node
    def __init__(self, p_num):
        self.p_num = p_num
        self.prev = None
        self.next = None

class Belt: # Linked List
    def __init__(self, b_num):
        self.b_num = b_num
        self.head = None
        self.rear = None
        self.len = 0

    # 리스트 초기화
    def clear(self):
        self.head = None
        self.rear = None
        self.len = 0

    # 앞에 노드 추가
    def add_front_node(self, node):
        if not node:
            return

        if self.len == 0:
            self.head = node
            self.rear = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.len += 1

    # 앞에 연결리스트를 추가(새로 연결)
    def add_front_list(self, new_list):
        if not new_list or new_list.len == 0:
            return

        if self.len == 0:
            self.head = new_list.head
            self.rear = new_list.rear
        else:
            new_list.rear.next = self.head
            self.head.prev = new_list.rear
            self.head = new_list.head
        self.len += new_list.len

    # 뒤에 노드 추가
    def add_tail_node(self, node):
        if self.len == 0:
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        self.len += 1

    # 헤드를 pop
    def pop_head(self):
        if self.len == 0:
            return None

        prev_head = self.head
        self.head = self.head.next

        if self.len == 1:
            self.clear()
        else:
            prev_head.next = None
            self.head.prev = None
            self.len -= 1

        return prev_head

    # n번째 노드를 반환
    def get_node(self, n):
        if n == 0: return None
        if n == 1: return self.head

        cur = self.head
        for _ in range(n-1):
            cur = cur.next

        return cur
    # n번까지의 리스트를 끊고, 새로운 연결리스트로 반환
    def pop_list(self, n):
        new_list = Belt(-1)

        if n==0: return new_list

        new_list.head = self.head
        new_list.rear = self.get_node(n)
        new_list.len = n

        self.head = new_list.rear.next
        self.head.prev = None
        new_list.rear.next = None
        self.len -= n

        return new_list

# n번까지의 리스트를 끊고, 새로운 연결리스트로 반환

# ====================================
# 보조 함수
# ====================================
def init_data(line):
    global N, M, belts, presents

    N, M = line[1], line[2]
    belts = [Belt(i) for i in range(N+1)]
    presents = [Present(i) for i in range(M+1)]

    for p_num in range(1, M+1):
        b_num = line[p_num+2]
        belts[b_num].add_tail_node(presents[p_num])

# ====================================
# 메인 로직
# ====================================
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
            src_list, dst_list = belts[m_src], belts[m_dst]
            dst_list.add_front_list(src_list)
            src_list.clear()
            answer.append(dst_list.len)

        # 3. 앞 물건만 교채
        elif cmd == 300:
            m_src, m_dst = line[1], line[2]
            src_list, dst_list = belts[m_src], belts[m_dst]
            head_src = src_list.pop_head()
            head_dst = dst_list.pop_head()
            src_list.add_front_node(head_dst)
            dst_list.add_front_node(head_src)
            answer.append(dst_list.len)

        # 4. 물건 나누기
        elif cmd == 400:
            m_src, m_dst = line[1], line[2]
            src_list, dst_list = belts[m_src], belts[m_dst]
            # n번까지의 리스트를 끊고, 새로운 연결리스트로 반환
            tmp_list = src_list.pop_list( src_list.len//2 )
            dst_list.add_front_list(tmp_list)
            answer.append(dst_list.len)

        # 5. 선물 정보
        elif cmd == 500:
            p_num = line[1]
            p = presents[p_num]
            a = p.prev.p_num if p.prev else -1
            b = p.next.p_num if p.next else -1
            answer.append( a + 2*b )

        # 6. 벨트 정보
        elif cmd == 600:
            b_num = line[1]
            belt = belts[b_num]
            a = belt.head.p_num if belt.head else -1
            b = belt.rear.p_num if belt.rear else -1
            c = belt.len
            answer.append( a + 2*b + 3*c )

        # if DEBUG: print()

    print('\n'.join(map(str, answer)))

main()