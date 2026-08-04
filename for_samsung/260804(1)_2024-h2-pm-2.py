'''
코드트리 등산 게임: 2024 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mountain-climbing-games


시간 초과 후 전략 수정으로 try2에서 이어서 진행
'''

#############################################
##### 전역 선언
#############################################
Q = -1
mountains = []

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

    lis_tmp = [] # 임시 최장증가부분수열
    memo_idx = [-1]*len(mountains) # 각 값이 들어갈 수 있는 인덱스 기록

    for i, v in enumerate(mountains):
        if not lis_tmp or lis_tmp[-1] < v:
            lis_tmp.append(v)
            memo_idx[i] = len(lis_tmp)-1
        else:
            v_idx = bs(lis_tmp, v) # 이분탐색으로 해당 값이 들어갈 위치를 반환
            lis_tmp[v_idx] = v
            memo_idx[i] = v_idx
            # print()
    lis_ans = len(lis_tmp) # 최장증가부분수열 길이

    # 마지막에 오는 인덱스 중, 가장 큰 값
    lis_max = -float('inf')
    for i, v in enumerate(memo_idx):
        if v == lis_ans-1:
            lis_max = max(lis_max, mountains[i])

    # print()

    return lis_ans, lis_max

# m 인덱스부터 역 리스트에 대해, 최장부분감소수열
def lis_m(m):
    max_v = mountains[m]
    lis_tmp = []

    for i in range(m-1, -1, -1):
        v = mountains[i]
        if v >= max_v : continue

        if not lis_tmp or lis_tmp[-1] > v:
            lis_tmp.append(v)
        else:
            v_idx = bs(lis_tmp, v, True)
            lis_tmp[v_idx] = v
    # print(lis_tmp)
    # print()

    return len(lis_tmp)+1
def m_simulation(m):

    # m 도착까지의 LIS - m 기준 역으로
    to_m = lis_m(m-1)
    # 전체 LIS
    from_m, last_h = lis_all()
    # 점수 반환
    # print()

    # 아이템 수가 아니라 이동 수이므로 to_m - 1, from_m -1 한 후, 케이블카 이용 횟수 1 더함
    result = (to_m + from_m - 1) * 1_000_000 + last_h
    return result
#############################################
##### 메인 로직
#############################################
def main():
    global Q

    Q = int(input())
    answer = []
    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]
        # 100 빅뱅 - 초기 산 정보
        if cmd == 100:
            mountains.extend(line[2:])
        # 200 우공이산 - 산 추가
        elif cmd == 200:
            mountains.append(line[1])
        # 300 지진 - 가장 오른쪽 산 제거
        elif cmd == 300:
            mountains.pop()
        # 400 등산 시뮬레이션 - LIS 이분탐색
        elif cmd == 400:
            simul_result = m_simulation(line[1])
            answer.append(simul_result)
            # print(len(answer), simul_result)

    print('\n'.join(map(str, answer)))

main()