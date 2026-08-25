'''
코디의 향수 공방: 2026 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/

문제 분석: 22m 34s
코드 작성: 43m 02s
최종 디버깅: 0m 0s

총 소요 시간: 1h 5m 36s
'''

# ======================================
# 전역 선언부
# ======================================

INF = float('inf')
N, Q = -1, -1
items = [-1] # 0 인덱싱

# ======================================
# 보조 함수
# ======================================

# 블렌딩
def dp(k):
    # 현재 있는 향수를 오름차순 정렬
    sorted_items = sorted([v for v in items if v != -1])
    memo = [INF] * (k+1)
    memo[0]=0

    # 동전 문제 알고리즘
    for item in sorted_items:
        for i in range(item, k+1):
            memo[i] = min(memo[i], memo[i-item]+1)

    return memo[-1]

def prefix_sum(k):
    memo = [0] * (k+1)
    exist_items = [v for v in items if v != -1]

    # 두 조합의 합을 먼저 카운트(a+b)
    # k를 넘어가면 어차피 이후 조합에서 k 이상으로 넘어가므로, 마지막 인덱스에 넣는다.
    for a in exist_items:
        for b in exist_items:
            sum_ab = a+b
            if sum_ab > k:
                memo[k] += 1
            else:
                memo[sum_ab] += 1

    # a+b 조합에서 각 숫자 이상을 만들 수 있는 경우의 수
    # 큰 수에서 작은 수로, 누적합을 구함
    for i in range(k-1, -1, -1):
        memo[i] += memo[i+1]


    # c를 더했을 때, 요구하는 최소 (a+b)쌍을 업데이트
    result = 0
    for c in exist_items:
        result += memo[max(0, k-c)]

    return result
# ======================================
# 메인 로직
# ======================================
def main():
    global N, Q

    Q = int(input())

    ans = []
    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 향료 준비
        if cmd == 1:
            N = line[1]
            items.extend(line[2:])
        # 향료 추가
        elif cmd  == 2:
            items.append(line[1])
            N += 1
        # 향료 폐기
        elif cmd == 3:
            idx = line[1]

            if idx <= N:
               ans.append(items[idx])
               items[idx] = -1
            else:
                ans.append(-1)
        # 블렌딩
        elif cmd == 4:
            dp_result = dp(line[1])
            ans.append(dp_result if dp_result!=INF else -1)
        # 향수 구성
        elif cmd == 5:
            prefix_sum_result = prefix_sum(line[1])
            ans.append(prefix_sum_result)
        # print(

    print('\n'.join(map(str, ans)))

main()