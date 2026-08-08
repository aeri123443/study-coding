'''
여왕 개미: 2025 상반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description

문제 분석: 17m 27s
코드 1차 작성: 1h 08m 52s
  - [시간 소요] 다음 개미의 출발 좌표를 정할 때, 집 하나씩 직접 카운트하는 것(O(n))으로 작성하다가,
              이것도 이분탐색으로 다음 좌표를 구할지(logn), 이 방식으로 계획을 바꾸면 작성에 오래 걸릴지를 고민함
              -> tmp_house = [x for x in house if x]로 한 번 리스트를 줄여준 후 이진탐색 작성
  - [시간 소요] 이분탐색에서 cnt가 목표 r보다 작아도 ans 업데이트 되는지 계속 고민
              -> 개미가 남으면 몇마리는 움직이지 않게 배치하면 된다고 생각, 업뎃 결정!
코드 1차 디버깅: 21m 35s
  - [TC2 Fail] 1. 개미집 철거할 때 idx를 바로 뺌 -> idx-1번 집을 빼도록 변경 -> 답은 달라졌지만 여전히 틀림
               2. 초=거리 개념으로 생각해서 i, j = tmp_house[0], tmp_house[-1]으로 했었는데,
                  이렇게 되면 tmp_house[0]보다 적은 초가 소요되었을때는 탐색할 수 없어서 틀림.
                  -> 이에 i, j = 0, tmp_house[-1]으로 최댓값만 지정

총 소요 시간: 1h 47m 54s
'''
from bisect import bisect_right

########################################################################
##### 전역 선언부
########################################################################
MAX_X = 10**9+1
Q, N = -1, -1 # N: 집 번호 기준

x_idx_map = {} # x좌표 - 개미집 번호
idx_x_map = {}
house = [] # 개미집 x 좌표. 주기적으로 none 정리
########################################################################
##### 보조 함수
########################################################################

### t초 제한이 있으면 몇 마리가 필요한지?
def cal_ant_cnt(arr, start_idx, t):
    si = start_idx
    si_list = [start_idx] # 디버깅용 시작 개미집 번호
    cnt = 0

    while si < len(arr):
        cnt += 1
        # 지금 출발하는 개미가 t초 후 어디까지 갈 수 있는지?
        ant_x = arr[si]
        after_t_x = ant_x + t

        # 다음 개미는, 이전 개미가 최대로 갈 수 있는 좌표에서 다음 좌표임
        si = bisect_right(arr, after_t_x)
        si_list.append(si)

    return cnt, si_list

### 개미집 정찰 - 이분 탐색 후 최적의 시간 반환
def explore(r):
    # 이진 탐색을 위해, 임시로 none을 제거한 리스트를 반환
    tmp_house = [x for x in house if x]

    i, j = 0, tmp_house[-1] # 0초, 끝 좌표

    # 개미 수가 1이면 (가장 먼 곳 - 가장 가까운 곳) 반환
    if r == 1:
        return j - tmp_house[0]

    # 집 수와 r이 같으면 0초 소모)
    if r == len(tmp_house):
        return 0

    ans = -1
    # print()
    # 이분탐색: mid초 제한이 있으면 몇 마리가 필요한지?
    while i <= j:
        mid = (i+j)//2
        cnt, si_list = cal_ant_cnt(tmp_house, 0, mid)
        # print()
        # cnt가 목표 r보다 같거나 작으면 탐색 범위를 좁힘
        if cnt <= r:
            ans = mid
            j = mid - 1
        else:
            i = mid + 1
        # print()
    return ans

    # 개미 출발 좌표, 끝 좌표
#     #
########################################################################
##### 메인 로직
########################################################################
def main():
    global Q, N

    Q = int(input())
    answer = []

    for q in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        ### 100 마을 건설
        if cmd == 100:
            N = line[1]
            for i in range(2, N+2):
                x = line[i]
                house.append(x)
                x_idx_map[x] = i-1

        ### 200 개미집 건설
        elif cmd == 200:
            x = line[1]
            house.append(x)
            x_idx_map[x] = N
            N += 1

        ### 300 개미집 철거
        elif cmd == 300:
            idx = line[1]
            house[idx-1] = None

        ### 400 개미집 정찰
        elif cmd == 400:
            t = explore(line[1])
            answer.append(t)
        # print()
    print('\n'.join(map(str, answer)))

main()