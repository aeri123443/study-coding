'''
나 잡아 봐라 | 모의고사 2회 - 2번
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4802/curated-cards/mock-complex-pinball-game/description

문제 분석: 1h 13m 29s
코드 1차 작성: 1h 28m 43s
TC fail, 클로드 도움으로 해결
총 소요 시간: 2h 42m 12s
'''


from bisect import bisect_left, bisect_right

# idx = [0, 3, 7]
# power = [2, 1, 3]
#
# idx_end = [2, 6, 13]
# idx_start = [0, 5, 10]
# dp = [0, 2, 3, 6]

# 시계
# for i in range(-1, 9):
#     bl = bisect_left(idx, i)
#     print(i, bl, i+dp[bl])
# 반시계
# for i in range(-1, 9):
#     bl = bisect_right(idx, i)
#     print(i, bl, i+dp[bl])

# 설계 1h 13m 29s


# 역추적
#
# for num in range(0, 15):
#     s = bisect_right(idx_start, num)
#     e = bisect_right(idx_end, num)
#     if s == e:
#         print(num, num-dp[s])
#     else:
#         print(num, idx[e])
    # print(num, s, e, dp[s], dp[e])


from bisect import bisect_left, bisect_right

# =============================================
# 전역 및 클래스
# =============================================
DEBUG = False
L, N, Q = map(int, input().split())

bench_idx = []
bench_power = []

bench_dp = []
idx_end = []
idx_start = []
# =============================================
# 보조 함수
# =============================================
def init_data(line): # 9m 32s
    global bench_idx, bench_power

    bench_idx = line[1:N+1]
    bench_power = line[N+1:]

def init_dp():
    global bench_dp, idx_start, idx_end

    dp = [0]*(N+1)
    s = []
    e = []
    for i in range(N):
        dp[i+1] = dp[i]+bench_power[i]
        e.append(bench_idx[i]+dp[i+1])
        s.append(e[i]-bench_power[i])
    bench_dp = dp
    idx_end = e
    idx_start = s

def call_meet_idx(a_idx, b_idx): # 15m 14s
    if a_idx < b_idx:
        return (a_idx+b_idx)/2
    else:
        l = L + bench_dp[-1]
        b_idx += l
        meet_idx = (a_idx+b_idx)/2
        return meet_idx % l

def get_point(meet_idx): # 48m 04s
    s = bisect_right(idx_start, meet_idx)
    e = bisect_right(idx_end, meet_idx)
    if s == e:
        return meet_idx-bench_dp[s]
    else:
        return bench_idx[e]
# =============================================
# 메인 로직
# =============================================
def main():
    answer = []
    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        if cmd == 100:
            init_data(line)
            # dp 초기화
            init_dp()
        elif cmd == 200: # 8m 4s
            x, p = line[1:]
            idx = bench_idx.index(x) # TODO: 더 가볍게
            bench_power[idx] = p
            init_dp()
        elif cmd == 300:
            a, b = line[1:]
            a_idx = a + bench_dp[bisect_left(bench_idx, a)]
            b_idx = b + bench_dp[bisect_right(bench_idx, b)]
            l = L + bench_dp[-1]

            meet_idx = call_meet_idx(a_idx, b_idx)
            meet_time = ((b_idx - a_idx) % l) / 2 # open tc2 오류로 수정: 7m 49s
            meet_point = get_point(meet_idx)

            s = bisect_right(idx_start, meet_idx)
            e = bisect_right(idx_end, meet_idx)
            if s != e: # 벤치 위에서 만남 → 둘 다 벤치 구간에 들어온 순간
                meet_time = max((idx_start[e] - a_idx) % l, (b_idx - idx_end[e]) % l)

            answer.append(f'{float(meet_time)} {float(meet_point)}')
            # #     bl = bisect_left(idx, i)
            # #     print(i, bl, i+dp[bl])
        if DEBUG: print()
    print('\n'.join(answer))
main()