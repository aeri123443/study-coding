'''
여왕 개미: 2025 상반기 오후 2번

https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description

문제 분석: 22m 49s
1차 코드 작성: 52m 26s
    - [시간 소요] 이분탐색 헷갈려. . .
    - [TC15 fail] need_r == target_r 에서만 min_t를 업데이트 햇더니 결과값에서 특정 값만 너무 튐
                  -> 2차 작성에서 need_r < target_r 에서도 min_t 업데이트
2차 코드 작성: 5m 8s

총 소요 시간: 1h 20m 25s
'''

from bisect import bisect_right

# =================================================
# 전역 및 클래스
# =================================================
DEBUG = False

N, Q = -1, -1

ant_house = [-1]
x_to_idx = {}

# =================================================
# 보조 함수
# =================================================

# mt만큼의 제한시간이 주어졌을 때, 개미가 최소 몇 마리 필요한가?
def get_r(t, x_arr):
    r = 0
    ant_x = x_arr[0]

    while ant_x <= x_arr[-1]:
        r += 1

        nxt_x = ant_x + t # t초 후에 이 개미가 몇 x까지 갈 수 있는지
        nxt_idx = bisect_right(x_arr, nxt_x)-1 # 그럼 몇번째 집까지 본 건지

        if nxt_idx+1 == len(x_arr) : break # 다음 집이 존재하지 않으면 종료
        ant_x = x_arr[nxt_idx+1]

    return r

# 개미집 정찰
def explore_house(target_r):
    # 유효한 개미만 필터링
    x_arr = [x for x in ant_house if x != -1]

    # target_r  1일 때
    if target_r == 1:
        return x_arr[-1] - x_arr[0]

    # 탐색 시간을 기준으로 이분탐색
    lt = 0
    rt = x_arr[-1]

    min_t = rt
    while lt <= rt:
        mt = (lt+rt)//2
        # mt만큼의 제한시간이 주어졌을 때, 개미가 최소 몇 마리 필요한가?
        need_r = get_r(mt, x_arr)

        if need_r > target_r:
            lt = mt + 1
        elif need_r < target_r:
            min_t = min(min_t, mt)
            rt = mt - 1
        else:
            min_t = min(min_t, mt)
            rt = mt - 1

    return min_t
# =================================================
# 메인 로직
# =================================================
def main():
    global Q, N, ant_house, x_to_idx

    answer = []
    Q = int(input())

    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 마을 건설
        if cmd == 100:
            N = line[1]
            for idx in range(1, N + 1):
                x = line[idx + 1]
                ant_house.append(x)
                x_to_idx[x] = idx

        # 개미집 건설
        elif cmd == 200:
            p = line[1]
            N += 1
            ant_house.append(p)
            x_to_idx[p] = N

        # 개미집 철거
        elif cmd == 300:
            q = line[1]
            x = ant_house[q]
            ant_house[q] = -1
            del x_to_idx[x]

        # 개미집 정찰
        elif cmd == 400:
            r = line[1]
            min_t = explore_house(r)
            answer.append(min_t)

        if DEBUG: print()

    print('\n'.join(map(str, answer)))

main()