'''
코드트리 등산 게임: 2024 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mountain-climbing-games

문제 분석: 28m 38s
  - [고민 포인트 1] 기존 Lis dp는 시간 초과 -> 이분탐색 lis 사용
  - [고민 포인트 2] 이분탐색 lis도 시간 초과의 여지가 있음 -> lis 관련 list, dict를 전역으로 관리
  - [고민 포인트 3] 산 제거 시 bi_lis_arr 복구 방법 -> 제거된 산의 idx 기준으로, 그 직전 업데이트 되었던 idx로 바꿔야 함
                  -> history를 stack으로 관리 -> 메모리가 여유로워 보여서 해당 방식 선택
코드 작성: 45m 39s
최종 디버깅: 0m 0s

총 소요 시간: 1h 14m 18s
'''

from collections import defaultdict
from bisect import bisect_left

############################################################
##### 전역 선언부
############################################################

Q = -1
h_list = [] # 높이 정보를 stack으로 관리

# LIS 이분탐색
bi_lis_arr = [] # tmp lis를 채워가며,
bi_lis_idx = [] # 각 산이 bi_lis_arr의 몇 번째 인덱스에 해당하는지를 저장하는데,
bi_lis_history = defaultdict(list) # 300에서 산 제거 시 bi_lis_arr를 복원하기 위해 idx 업데이트 내역을 스택으로 관리(idx:[h])

############################################################
##### 보조 함수
############################################################

### 산 추가
def add_mountain(h):
    if not bi_lis_arr or bi_lis_arr[-1] < h:
        new_idx = len(bi_lis_arr)
        bi_lis_arr.append(h)
    else:
        new_idx = bisect_left(bi_lis_arr, h)
        bi_lis_arr[new_idx] = h

    bi_lis_idx.append(new_idx)
    bi_lis_history[new_idx].append(h)

    h_list.append(h)

### 산 제거
def remove_mountain():

    # bi_lis_arr 되돌리기
    lis_idx = bi_lis_idx[-1]
    bi_lis_history[lis_idx].pop()
    if bi_lis_history[lis_idx]:
        bi_lis_arr[lis_idx] = bi_lis_history[lis_idx][-1]
    else:
        # bi_lis_arr는 단조 증가 스택이었기 때문에, 그 인덱스가 더 남지 않았다는 것은 lis 유일한 최댓값이었다는 의미가 됨.
        # 따라서 bi_lis_arr에서도 제거
        del bi_lis_history[lis_idx]
        bi_lis_arr.pop()

    # 각 전역에서 삭제
    h_list.pop()
    bi_lis_idx.pop()

### 등산 시뮬레이션
def simulation(m):
    cnt = 1 # 케이블카 이용 횟수 미리 추가

    # 시작 -> 케이블카 이동 수
    cable_idx = m-1
    cnt += bi_lis_idx[cable_idx]

    # 전체 LIS
    max_lis_idx = len(bi_lis_arr) - 1
    cnt += max_lis_idx

    # max_lis_idx 도착 높이가 가장 큰 곳
    # 디버깅 포인트: 시간 초과시 이 부분 확인
    arrive_h = max(bi_lis_history[max_lis_idx])

    return cnt * 1_000_000 + arrive_h


############################################################
##### 메인 로직
############################################################
def main():
    global Q

    Q = int(input())
    answer = []

    for q in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 100 초기 산 정보
        if cmd == 100:
            n = line[1]
            for i in range(n):
                idx = i + 2
                add_mountain(line[idx])
        # 200 오른쪽에 산 추가
        if cmd == 200:
            add_mountain(line[1])
        # 300 오른쪽 산 제거
        if cmd == 300:
            remove_mountain()
        # 400 등산 시뮬레이션
        if cmd == 400:
            ans = simulation(line[1])
            answer.append(ans)
        # print()
    print('\n'.join(map(str, answer)))

main()