'''
가로등 설치: 2025 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/street-light-installation/

'''

import heapq
import math

# ===============================
# 전역 선언
# ===============================
DEBUG = False

N, M = -1, -1
head, rear = None, None

lights = {}
hq = []

class Light:
    def __init__(self, idx, x):
        self.idx = idx
        self.x = x
        self.left = None
        self.right = None

# ===============================
# 보조 함수
# ===============================
def init_data(line):
    global N, M, head, rear

    N, M = line[1], line[2]

    head = Light(1, line[3])
    rear = Light(M, line[-1])

    lights[1] = head
    lights[M] = rear

    if M == 2:
        heapq.heappush(hq, (head.x-rear.x, head.x, head.idx, rear.idx))
        head.right = rear
        rear.left = head

    for idx in range(2, M): # 양끝은 따로 수행
        i = idx + 2
        x = line[i]
        new_light = Light(idx, x)
        lights[idx] = new_light
        add_right_in_list(idx, x, idx-1, idx+1)

# 연결리스트에 아이템 추가
def add_right_in_list(idx, x, l_num, r_num):
    left = lights[l_num]
    right = lights[r_num] if r_num in lights else lights[rear.idx]

    new_light = Light(idx, x)
    lights[idx] = new_light

    left.right = new_light
    right.left = new_light
    new_light.left = left
    new_light.right = right

    heapq.heappush(hq, (left.x-x, left.x, left.idx, idx ) )
    heapq.heappush(hq, (x-right.x, x, idx, right.idx) )

# 유효한 큐를 반환
def pop_hq():
    while hq:
        rev_dis, from_x, from_idx, to_idx = heapq.heappop(hq)
        if from_idx not in lights:
            continue

        if to_idx not in lights:
            continue

        from_item, to_item = lights[from_idx], lights[to_idx]

        if (from_item.right == to_item) and (to_item.left == from_item):
            return rev_dis, from_x, from_idx, to_idx

    return None, None, None, None

# 가로등 삽입 위치 찾고 add_right_in_list 호출
def add_light():
    global M

    rev_dis, _, from_idx, to_idx = pop_hq()
    from_item, to_item = lights[from_idx], lights[to_idx]

    x = math.ceil((from_item.x + to_item.x) / 2)
    add_right_in_list(M + 1, x, from_idx, to_idx)

    M += 1

def del_light(idx):
    global head, rear
    item = lights[idx]
    left, right = item.left, item.right

    # head일 경우
    if head == item:
        head = right
        right.left = None
    # rear일 경우
    elif rear == item:
        rear = left
        left.right = None
    else:
        left.right = right
        right.left = left
        new_dis = right.x - left.x
        heapq.heappush(hq, (-new_dis, left.x, left.idx, right.idx))

    del lights[idx]

def get_best_r():
    outside_r = max( head.x - 1, N - rear.x)

    pop_info = pop_hq()
    inside_r = (-pop_info[0])/2

    max_r = max(outside_r, inside_r)
    heapq.heappush(hq, pop_info)

    return max_r

# ===============================
# 메인 로직
# ===============================
def main():
    q = int(input())

    ans = []
    for _ in range(q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 마을 상태 확인
        if cmd == 100:
            init_data(line)

        # 가로등 추가
        elif cmd == 200:
            add_light()

        # 가로등 제거
        elif cmd == 300:
            del_light(line[1])

        # 최적 위치 계산
        elif cmd == 400:
            r = get_best_r()
            ans.append(int(2*r))
        if DEBUG: print()

    print('\n'.join(map(str, ans)))

main()