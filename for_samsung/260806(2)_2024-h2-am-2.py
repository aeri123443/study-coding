'''
코드트리 DB: 2024 하반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-db/description

gemini와 대화하며 세그먼트 트리 공부 후 코드 갈아엎고 다시 씀
이후 코드 작성 시간: 1h 39m 11s, 1트 통과
'''
from bisect import bisect_right

####################################################
##### 전역 선언부
####################################################

# Q: 쿼리 수
# N: 쿼리에 등장하는 모든 v가 몇 가지인지
# B: 세그먼트 트리의 리프노드 시작 인덱스
Q, N, B = -1, -1, -1

# 처음에 모든 v를 훑고 정렬
v_list = []
n_list = [] # 없을 경우 None

# 세그먼트 트리 idx를 기준으로 name-value를 관리
v_idx_map = {}
n_idx_map = {}

# 세그먼트 트리
sum_tree = [] # 누적합 (k 이하의 합)
count_tree = [] # 랭크 (k번째 수, 카운트로 해결)

####################################################
##### 보조 함수
####################################################

# 데이터 스캔 후 기초 환경 세팅
def data_scan():
    global Q, N, B, v_list, v_idx_map

    Q = int(input())
    cmd_line = [list(input().split()) for _ in range(Q)]

    v_set = set()
    for line in cmd_line:
        if line[0] == 'insert':
            v = int(line[2])
            v_set.add(v)

    N = len(v_set)
    B = 1
    while B < N:
        B *= 2

    v_list = sorted(v_set)
    for idx, v in enumerate(v_list):
        v_idx_map[v] = idx

    return cmd_line

# 데이터 초기화
def reset_data():
    global n_list, n_idx_map, sum_tree, count_tree

    n_idx_map = {}
    n_list = [None]*N
    sum_tree = [0]*(N*4)
    count_tree = [0] * (N * 4)

# 기존 데이터 존재 여부 확인
def can_insert(n, v):
    if n in n_idx_map:
        return False

    tid = B + v_idx_map[v]
    if sum_tree[tid] > 0:
        return False

    return True


# 데이터 추가
def insert_data(n, v):
    idx = v_idx_map[v]

    n_idx_map[n] = idx
    n_list[idx] = n

    tid = B + idx
    while tid > 0:
        sum_tree[tid] += v
        count_tree[tid] += 1

        tid //= 2

# 데이터 삭제
def remove_data(idx):
    n, v = n_list[idx], v_list[idx]

    n_list[idx] = None
    del n_idx_map[n]

    tid = B + idx
    while tid > 0:
        sum_tree[tid] -= v
        count_tree[tid] -= 1
        tid //= 2

    return v

# k번째 값
def rank_k(k):
    cnt = k
    tid = 1

    while tid < B:
        left_child = count_tree[tid*2]
        if left_child >= cnt: # 왼쪽 서브트리에 값 존재
            tid *= 2
        else: # 오른쪽 서브트리에 값 존재
            cnt -= left_child
            tid = tid*2 + 1

    idx = tid - B
    return n_list[idx]

## k 이하의 합 (구간합 응용)
def sum_under_k(k):
    s = B

    e_idx = bisect_right(v_list, k) - 1
    e = B + e_idx

    total = 0
    while s <= e:
        # s는 홀수일 때 선택
        if s % 2 == 1: total += sum_tree[s]
        # e는 짝수일 때 선택
        if e % 2 == 0: total += sum_tree[e]
        # s, e 업데이트
        s = (s+1) // 2
        e = (e-1) // 2

    return total
####################################################
##### 메인 로직
####################################################
def main():
    ## 전체 데이터 스캔
    cmd_line = data_scan()

    ## 쿼리 실행
    answer = []
    for line in cmd_line:
        cmd = line[0]
        # answer.append(line)
        ## 1. 테이블 초기화
        if cmd == 'init':
            reset_data()
        ## 2. 데이터 추가
        elif cmd == 'insert':
            n, v = line[1], int(line[2])
            # 기존 데이터 존재 여부 확인
            if can_insert(n, v):
                # 데이터 추가
                insert_data(n, v)
                answer.append(1)
            else:
                answer.append(0)
        ## 데이터 삭제
        elif cmd == 'delete':
            n = line[1]
            if n in n_idx_map:
                idx = n_idx_map[n]
                v = remove_data(idx)
                answer.append(v)
            else:
                answer.append(0)
        ## k번째 값
        elif cmd == 'rank':
            k = int(line[1])
            if k <= len(n_idx_map):
                n = rank_k(k)
                answer.append(n)
            else:
                answer.append(None)

        ## k 이하의 합
        elif cmd == 'sum':
            k = int(line[1])
            # v_list의 최솟값보다 작은 값이 들어오면 바로 0 반환
            if v_list[0] > k:
                answer.append(0)
            else:
                total = sum_under_k(k)
                answer.append(total)
        # print()
    print("\n".join(map(str, answer)))

main()