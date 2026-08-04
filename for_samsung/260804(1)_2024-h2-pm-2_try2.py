'''
코드트리 등산 게임: 2024 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mountain-climbing-games

문제 분석: 57m 54s
  - [시간 소요] LIS 문제인 건 알았는데, 기준 DP로 하면 시간초과가 날 것 같아서 이분탐색 LIS를 알아보고 문제 풀이 돌입
코드 1차 작성: 50m 01s
코드 1차 디버깅 및 분석: 29m 22s
  - [TC31 Fail] 시간초과, LIS memo 배열을 최상단에서 관리하는 방식으로 전략 수정
코드 2차 작성: 1h 09m 57s
  - [시간 소요] fail tc를 돌려보는데 계속 느리게 출력됨, 이에 전역에 max_len, max_h를 추가하고 이를 관리하는 함수를 추가

총 소요 시간: 3h 27m 16s
'''

#############################################
##### 전역 선언
#############################################
Q = -1
mountains = []
lis_arr = [] # 최장증가부분수열
lis_memo = [] # 인덱스 기록
max_len = -1
max_h = -1
#############################################
##### 보조 함수
#############################################

# 이분탐색
# 배열 안에서 특정 값이 위치하는 인덱스를 반환
def bs(arr, x, rev=False):
    i, j = 0, len(arr)
    ans = arr[-1]

    while i <= j:
        mid = (i+j)//2
        if (not rev and arr[mid] >= x) or (rev and arr[mid] <= x):
            ans = mid
            j = mid -1
        else:
            i = mid + 1

    return ans

# 전체 LIS - 이분탐색
def lis_all():
    global lis_arr, lis_memo

    lis_tmp = [] # 임시 최장증가부분수열
    memo_idx = [-1]*len(mountains) # 각 값이 들어갈 수 있는 인덱스 기록

    for i, v in enumerate(mountains):
        if not lis_tmp or lis_tmp[-1] < v:
            lis_tmp.append(v)
            memo_idx[i] = len(lis_tmp) -1
        else:
            v_idx = bs(lis_tmp, v) # 이분탐색으로 해당 값이 들어갈 위치를 반환
            lis_tmp[v_idx] = v
            memo_idx[i] = v_idx
            # print()
    # lis_ans = len(lis_tmp) # 최장증가부분수열 길이
    #
    # # 마지막에 오는 인덱스 중, 가장 큰 값
    # lis_max = -float('inf')
    # for i, v in enumerate(memo_idx):
    #     if v == lis_ans-1:
    #         lis_max = max(lis_max, mountains[i])

    # print()

    lis_arr, lis_memo = lis_tmp, memo_idx

    # return lis_ans, lis_max

# lis 배열에 인덱스(산) 추가
def add_m(h):
    global max_len, max_h

    if not lis_arr or lis_arr[-1] < h:
        lis_arr.append(h)
        lis_memo.append(len(lis_arr) - 1)
        max_len += 1
        max_h = h

    else:
        v_idx = bs(lis_arr, h)  # 이분탐색으로 해당 값이 들어갈 위치를 반환
        lis_arr[v_idx] = h
        lis_memo.append(v_idx)

def update_max_val():
    global max_len, max_h
    max_len = len(lis_arr)  # 케이블 이동 후, 최장 길이
    max_h = -float('inf')

    for i, v in enumerate(lis_memo):
        if v == max_len - 1:
            max_h = max(max_h, mountains[i])
#############################################
##### 메인 로직
#############################################
def main():
    global Q, max_len, max_h

    Q = int(input())
    answer = []
    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]
        # 100 빅뱅 - 초기 산 정보
        if cmd == 100:
            mountains.extend(line[2:])
            lis_all()

            update_max_val()

        # 200 우공이산 - 산 추가
        elif cmd == 200:
            h = line[1]
            mountains.append(h)
            add_m(h)

            # if
            # 마지막 값 기준
            # max_h 다시 계산
            # max_len = len(lis_arr) # 케이블 이동 후, 최장 길이
            # max_h = -float('inf')
            # for i, v in enumerate(lis_memo):
            #     if v == max_len-1:
            #         max_h = max(max_h, mountains[i])

        # 300 지진 - 가장 오른쪽 산 제거
        elif cmd == 300:
            poped_m = mountains.pop()
            # 거꾸로 스캔
            prev_lis_len = lis_memo[-1]
            replaced = False
            for i in range(len(mountains)-1, -1, -1):
                # lis_memo에 pop했던 인덱스가 또 있음 -> 덮어씀
                if lis_memo[i] == prev_lis_len:
                    replaced = True
                    lis_arr[prev_lis_len] = mountains[i]
                    break
            # 없음 -> pop
            if not replaced:
                lis_arr.pop()
            lis_memo.pop()

            if max_h == poped_m  or max_len != len(lis_arr):
                update_max_val()

        # 400 등산 시뮬레이션 - LIS 이분탐색
        elif cmd == 400:
            m = line[1] - 1
            to_m = lis_memo[m] # m까지의 lis


            simul_result = (to_m + max_len) * 1_000_000 + max_h
            answer.append(simul_result)
            # print(len(answer), simul_result)
        # print()
    print('\n'.join(map(str, answer)))

main()