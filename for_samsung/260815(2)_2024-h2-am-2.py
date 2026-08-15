'''
코드트리 DB: 2024 하반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-db/description

문제 분석: 16m 08s
코드 작성: 1h 01m 28s
최종 디버깅: 0m 0s

총 소요 시간: 1h 17m 36s
'''
from bisect import bisect_right
# ====================================================
# 전역 선언부
# ====================================================

# Q: 쿼리 수, N: v_list의 길이, B: 루트 노드의 시작 인덱스
Q, N, B = -1, -1, -1

# 값 정보, 초깃값 고정
v_list = []
v_idx_map = {}

# 이름 정보, 유동적 변화
n_list = []
n_idx_map = {}

# 세그먼트 트리
c_tree = [] # count
s_tree = [] # sum

# ====================================================
# 보조 함수
# ====================================================

# 전체 값을 읽고 초기 데이터 구성, 명령줄 반환
# n_list, c_tree, s_tree는 init에서 관리
def input_data():
    global Q, N, B, v_list, v_idx_map

    Q = int(input())
    lines = [list(input().split()) for _ in range(Q)]

    # insert value 값만 모음!
    for line in lines:
        if line[0] == 'insert':
            v_list.append(int(line[2]))

    v_list.sort()
    for i, v in enumerate(v_list):
        v_idx_map[v] = i

    N = len(v_list)
    B = 1
    while B < N:
        B *= 2


    return lines

# 테이블 초기화
def init_data():
    global n_list, n_idx_map, c_tree, s_tree

    n_list = [None]*N
    n_idx_map = {}

    c_tree = [0]*(2*B)
    s_tree = [0] * (2*B)

def add_data(idx, n, v):
    cur = B + idx

    n_list[idx] = n
    n_idx_map[n] = idx

    while cur > 0:
        c_tree[cur] += 1
        s_tree[cur] += v

        cur //= 2

# 데이터 제거 후 제거된 값 반환
def delete_data(n):
    idx = n_idx_map[n]
    v = v_list[idx]

    cur = B + idx
    while cur > 0:
        c_tree[cur] -= 1
        s_tree[cur] -= v

        cur //= 2

    n_list[idx] = -1
    del n_idx_map[n]

    return v

def get_rank(k):
    r = k
    cur = 1

    while cur < B:
        left = cur*2
        if r <= c_tree[left]:
            cur = left
        else:
            r -= c_tree[left]
            cur = left + 1

    idx = cur - B
    return n_list[idx]

def sum_data(k):
    total = 0

    left = B
    right = bisect_right(v_list, k) - 1 + B

    while left <= right:

        # left는 홀수일 경우 선택
        # right는 짝수일 경우 선택
        if left%2 == 1: total += s_tree[left]
        if right%2 == 0: total += s_tree[right]

        left = (left+1)//2
        right = (right-1)//2

    return total


# ====================================================
# 메인 로직
# ====================================================
def main():
    # 전체 값을 읽고 초기 데이터 구성, 명령줄 반환
    lines = input_data()
    # print()

    ans = []
    for line in lines:
        cmd = line[0]

        # 테이블 초기화
        if cmd == 'init':
            init_data()
        # 데이터 추가
        elif cmd == 'insert':
            n, v = line[1], int(line[2])

            if n in n_idx_map:
                ans.append(0)
                continue

            idx = v_idx_map[v]
            if c_tree[B+idx] == 1:
                ans.append(0)
                continue

            add_data(idx, n, v)
            ans.append(1)

        # 데이터 삭제
        elif cmd == 'delete':
            n = line[1]

            if n not in n_idx_map:
                ans.append(0)
                continue

            v = delete_data(n)
            ans.append(v)

        # k번째 작은 값의 이름 출력
        elif cmd == 'rank':
            k = int(line[1])

            if len(n_idx_map) < k:
                ans.append(None)
                continue

            n = get_rank(k)
            ans.append(n)

        # k 이하인 값의 합
        elif cmd == 'sum':
            k = int(line[1])

            if k < v_list[0]:
                ans.append(0)
                continue

            sum_val = sum_data(k)
            ans.append(sum_val)

        # print()
    print('\n'.join(map(str, ans)))

main()