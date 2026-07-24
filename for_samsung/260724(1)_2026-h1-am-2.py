'''
코디의 향수 공방: 2026 상반기 오전 2번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/perfume-workshop/description
문제 분석: 15m 07s
코드 1차 작성: 1h 24m 39s
  - [시간 초과] 백트래킹으로 조합 및 순열을 구현하여 시간 초과 발생
문제 2차 분석: 21m 4s
  - gemini 활용으로 dp&누적합 갈피 잡기
코드 2차 작성: 52m 45s
  - [작성 시간 오래 걸림] 향수 구성을 투포인터에서 누적합으로 변경
최종 디버깅: 5m 11s
  - [오류 원인] 문제를 잘못 파악해서, 향수 구성 시 경우의 수가 없으면 그대로 0을 반환하면 되는데, -1을 반환하게 함

총 소요 시간: 2h 58m 48s
'''
####################################################
#### 전역 선언
####################################################

Q = -1
INF = float('inf')
items = []
# pressed_items = [] # 백트래킹용 압축 데이터
####################################################
#### 보조 함수
####################################################

# 아이템 압축
def press_item():
    arr = []
    for i, v in enumerate(items):
        if v > 0:
            arr.append((i,v))
    return arr

# 블랜딩(dp)
def dp(k):
    sorted_items = set(items)
    if 0 in sorted_items: sorted_items.remove(0)
    sorted_items = sorted(sorted_items)

    memo = [INF]*(k+1)
    memo[0] = 0

    for x in sorted_items:
        for i in range(x, k+1):
            remain = i-x
            if remain >= 0 and memo[remain]!=INF:
                memo[i] = min( memo[i], memo[remain]+1 )

    return memo[-1]

# 향수 구성 (product 백트래킹)
def product_item(k):
    sorted_items = sorted([x for x in items if x>0])
    memo = [0]*(k+1)

    # N+N 빈도수 계산
    for a in sorted_items:
        for b in sorted_items:
            if a+b >= k: # 이 부분 연산 줄일 수 있음
                memo[k] += 1
            else:
                memo[a+b] += 1

    # 누적합: 합이 i가 넘는 빈도수 계산
    for i in range(k-1, -1, -1):
        memo[i] += memo[i+1]

    # c를 골랐을 때, 다른 두 수의 합이 k-c를 넘는 경우의 수를 반환
    cnt = 0
    for c in sorted_items:
        target_ab_sum = k-min(c, k) # c가 k를 이미 넘으면 사실상 모든 경우의 수를 더해도 무관
        cnt += memo[target_ab_sum]

    return cnt

####################################################
#### 메인 함수
####################################################
def main():
    global Q, items

    Q = int(input())
    answer = []

    for q in range(Q):
        cmd_line = list(map(int, input().split()))
        if cmd_line[0] == 1: # 향료 준비
            items = [0] + cmd_line[2:]
        elif cmd_line[0] == 2: # 향료 추가
            items.append(cmd_line[1])
        elif cmd_line[0] == 3: # 향료 폐기
            idx = cmd_line[1]

            if idx >= len(items):
                answer.append('-1')
                continue

            v = items[idx]
            if v > 0:
                items[idx] = 0
                answer.append(str(v))
            else:
                answer.append('-1')
        elif cmd_line[0] == 4:  # 블렌딩
            blending_cnt = dp(cmd_line[1])
            answer.append(str(blending_cnt) if blending_cnt!=INF else '-1')
        elif cmd_line[0] == 5: # 향수 구성
            product_cnt = product_item(cmd_line[1])
            answer.append(str(product_cnt))
        # print()
    print('\n'.join(answer))

main()