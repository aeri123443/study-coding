# 삼성 기출 복습 - 코드트리 등산 게임
# 문제 분석 36m 46s
# 총 소요시간 1h 36m 32s
# non-fail pass

'''

일차원 지도

등산가 이동 조건
- 등산을 통한 산 사이 이동: 오른쪽으로만, 더 높은 산으로만

케이블카
- 특정 산에서만
- 임의의 산으로 이동: 높낮이 ㄱㅊ [?] 오른쪽으로는 필수?? -> 아님!

등산 시뮬레이션
-> 케이블 lis
케이블 이용
-> 전체 lis
1) 시작 산 선택
2) 오른쪽 오르막 이동 -> 1_000_000
3) 케이블 카 이용 -> 1_000_000
4) 등산 시작 -> 1_000_000
5) + 최종 위치 산

dp_idx_list = [dp_idx]
dp_history = {dp_idx: [h_idx]}
lis_stack = [h_val]

케이스 확인
- 같은 높이가 있을 경우

산 추가
- lis_stack[-1]과 비교
    - 클 경우: lis_stack 추가, dp_history 추가, dp_idx_list 업데이트
    - 작거나 같음:
      1) b-left로 lis_stack에 들어갈 인덱스 찾기
      2) lis_stack 해당 인덱스 교체, dp_history 추가, dp_idx_list 업데이트

산 제거
1) dp_idx_list에서 dp_idx 반환 후 pop
2) dp_history에서 팝하고, 마지막 값을 업데이트
    - 마지막 값이었음: 그냥 del dp_history, stack pop



명령 Q (500_000)
1. 빅뱅 (최초 1회)
    - 100 n, h...
2. 우공이산
    - 200 h
    - 오른쪽 끝에 h 높이 산 추가
3. 지진
    - 300
    - 가장 오른쪽 산 제거
4. 등산 시뮬레이션
    - 400 m
    - m_idx번째 산에 케이블(1-idx)
    - 얻을 수 있는 최대 점수
'''
from collections import defaultdict
from bisect import bisect_left

Q = int(input())

h_list = []
dp_idx_list = [] # [dp_idx]
dp_history = defaultdict(list) # {dp_idx: [h_idx]}
lis_stack = [] # [h_val]
max_info = (-1,-1) # 이동 횟수 최대, 산 높이 최대

def debug_print():
    print(f'max_info: {max_info}')
    print(f'h_list: {h_list}')
    print(f'lis_stack: {lis_stack}')
    print(f'dp_idx_list: {dp_idx_list}')
    print('dp_history: ')
    for i, v in dp_history.items():
        print(f' | {i} : {v}')
    print()

# 산 추가
def add_mountain(h): # 16m 18s
    global max_info

    # 클 경우: lis_stack 추가, dp_history 추가, dp_idx_list 업데이트
    if not lis_stack or lis_stack[-1] < h:
        lis_stack.append(h)
        dp_idx = len(lis_stack) - 1
    # 작거나 같음
    else:
        # 1) b-left로 lis_stack에 들어갈 인덱스 찾기
        dp_idx = bisect_left(lis_stack, h)
        # 2) lis_stack 해당 인덱스 교체, dp_history 추가, dp_idx_list 업데이트
        lis_stack[dp_idx] = h

    h_list.append(h)
    h_idx = len(h_list)-1
    dp_history[dp_idx].append(h_idx)
    dp_idx_list.append(dp_idx)

    max_info = max(max_info, (dp_idx_list[-1], h))

# 산 제거
def remove_mountain(): # 16m 14s
    global max_info

    pop_cnt = dp_idx_list[-1]
    pop_h = h_list.pop()
    dp_idx = dp_idx_list.pop()
    # p_history에서 팝하고, 마지막 값을 업데이트
    dp_history[dp_idx].pop()
    if dp_history[dp_idx]:
        last_h_idx = dp_history[dp_idx][-1]
        lis_stack[dp_idx] = h_list[last_h_idx]
        max_candidate = dp_history[dp_idx]
    else:
        del dp_history[dp_idx]
        lis_stack.pop()
        max_candidate = dp_history[dp_idx-1]

    if max_info == (pop_cnt, pop_h):
        can_max_info = (-1, -1)
        for can_h_idx in max_candidate:
            can_max_info = max(can_max_info, (dp_idx_list[can_h_idx], h_list[can_h_idx]))
        max_info = can_max_info

# 등산 시뮬레이션

# 1) 시작 산 선택
# 2) 오른쪽 오르막 이동 -> 1_000_000
# 3) 케이블 카 이용 -> 1_000_000
# 4) 등산 시작 -> 1_000_000
# 5) + 최종 위치 산

def simulation(m):
    m -= 1
    # -> 케이블 lis
    s_to_cable = dp_idx_list[m]
    # 케이블 이용
    # -> 전체 lis
    s_to_e, last_h = max_info

    return (s_to_cable+1+s_to_e)*1_000_000 + last_h

    # - 얻을 수 있는 최대 점수
def main(): # 28m 14s
    answer = []
    for _ in range(Q):
        cmd, *line = list(map( int, input().split()))
        # 1. 빅뱅 (최초 1회)
        if cmd == 100:
            for h in line[1:]:
                add_mountain(h)
        # 2. 우공이산
        elif cmd == 200:
            h = line[0]
            add_mountain(h)
        # 3. 지진
        elif cmd == 300:
            remove_mountain()
        # 4. 등산 시뮬레이션
        elif cmd == 400:
            m = line[0]
            score = simulation(m)
            answer.append(score)
        # debug_print()
    print('\n'.join(map(str, answer)))

main()