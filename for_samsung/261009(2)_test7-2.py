"""# import sys
# import tracemalloc
# tracemalloc.start()
#
# a = [1,2,3,4,9,4,5,6,5]
# b = [4,5,6,7,8,9,10,11]
# class Node:
#     def __init__(self):
#         self.prev = a
#         self.next = b
#         self.val = -1
#         self.vv = 9448
#
# ab = Node()
# arr = [Node()]*200_000
# cur, peak = tracemalloc.get_traced_memory()
# print(cur, peak)
# print(sys.getsizeof(arr))

import heapq
a = [1,2,9,10,15]
b = [3,4,5,6,11]
tu = []

for i in a:
    for j in b:
        result = i-j if i>j else i+16-j
        heapq.heappush(tu, (result,i,j))

a_used = set()
b_used = set()

while tu:
    d, i,j= heapq.heappop(tu)
    if i not in a_used and j not in b_used:
        print(d, i, j)
        a_used.add(i)
        b_used.add(j)
print(tu)

"""


# 필요한 자료
# - 전체 라인
# - 이벤트 큐 (충돌 이벤트) (T, a1(1원자), a2(2원자))

#
# T초
#     1. 모든 입자 이동: 1초, 입자 종류 규칙에 따라
#         - 동시 이동
#         - 이동 후 충돌 여부 확인, 새 종류 업데이트
#     2. 명령이 있으면 명령 수행

import heapq

# 설계
#     - 아이디어
#         - 합쳐지는 순간은 1+2 만나는 순간. 3 -> 0 이 되어 둘다 사라진다. 세 값이 겹쳐지는 경우는 없음.
#         - 100, 300 명령 -> 1원자, 2원자를 연결리스트로 관리



Q = int(input())
N = -1
items = [] # 전체 라인
event_q = []  # 이벤트 큐 (충돌 이벤트) (T, a1(1원자), a2(2원자))

# 충돌 순서 반환
def get_order_q(line): # 빨리 끝내고싶나... 이거 하나에 실수엄청 했네  44:12
    hq = []
    stack = []

    removed_a = set()
    for i in range(len(line)-1, -1, -1):
        # a를 만날 때마다 스택에 넣고
        if line[i] == 1:
            stack.append(i)

        # b를 만나면 pop해서 차이 구하고 (충돌 시간 최소임) 순서에 넣음
        # 만약 b를 만났는데 a가 없으면 -> a를 늘렷는데도 a가 없단 소리면 그냥 a가 적어서 다 사라진거임 -> 충돌 안 남
        elif line[i] == 2:
            a = -1
            while stack:
                ta = stack.pop()
                if ta%N in removed_a:
                    continue
                else:
                    a = ta
                    removed_a.add(a%N)
                    break
            if a==-1: return hq
            heapq.heappush(hq, ((a-i)%N, a%N, i))

    return hq


def update_conflict_order(): # 2:51
    global event_q

    new_line = items[:]
    for i, v in enumerate(items):
        if v==1: new_line.append(1)
        else: new_line.append(0)

    new_q = get_order_q(new_line)
    event_q = new_q

# T초까지의 상태를 업데이트
def update_status(t): #4: 26
    # t까지 모두 뽑고, 해당하는 인덱스를 제거
    while event_q:
        qe, qa, qb = event_q[0]
        if qe <= t:
            items[qa] = 0
            items[qb] =0
            heapq.heappop(event_q)
        else:
            break

# T초 후의 i1은 cur_x 초에서 어디인가?
def get_initial_idx(t, x): #4:05 -> 인덱스 1 빼야햇는데 아차차~
    return (x-t)%N

# 설계 정리, 전역 입력 3:42
def main():
    global N, items

    for _ in range(Q):
        cmd, *line = map(int, input().split())

        # ===============================================
        # 1. 초기화
        #     - 100 N A1 A2 .. AN
        #     - 트랙길이 N, 각 구역에 순서대로 배치
        # ===============================================
        if cmd == 100:
            N, *items = line
            update_conflict_order()

        # ===============================================
        # 2. 조회
        #     - 200 T x
        #     - T 상태 기준, x구역에 있는 입자는!
        #     - 한 줄에 하나씩
        # ===============================================
        elif cmd == 200:
            t, x = line
            update_status(t)
            idx = get_initial_idx(t, x-1)
            print(items[idx])

        # ===============================================
        # 3. 수정 (20 이하)
        #     - 300 T M i1 v1 i2 v2 ... im vm
        #     - M개 교체: i번 구역의 입자를 v로
        # ===============================================
        elif cmd == 300:
            t, m, *n_line = line
            # def T초까지의 상태를 업데이트
            update_status(t)

            for idx in range(m):
                i, v = n_line[idx*2], n_line[idx*2]+1
                t_idx = get_initial_idx(t, i-1)  # T초 후의 i1은 cur_x 초에서 어디인가?
                items[t_idx] = v # 업데이트
        print()
main()