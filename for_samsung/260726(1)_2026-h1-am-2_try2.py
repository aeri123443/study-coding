'''
코디의 향수 공방: 2026 상반기 오전 2번 문제 복습
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/perfume-workshop/description

문제 분석: 13m 29s
코드 1차 작성: 27m 03s
  - [tc3 fail] 향수 구성 단계에서 item_set = set(items); item_set.remove(-1)를 해서, 중복된 향도의 향료에 대한 빈도수 누락
디버깅 및 코드 2차 작성: 5m 34s

총 소요 시간: 46m 8s
'''

INF = float('inf')

def main():
    q = int(input())
    items = [-1]
    answer = []

    for _ in range(q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 1. 향료 준비
        if cmd == 1:
            items.extend(line[2:])
        # 2. 향료 추가
        elif cmd == 2:
            items.append(line[1])
        # 3. 향료 폐기
        elif cmd == 3:
            idx = line[1]
            if 0 < idx < len(items) and items[idx]>0:
                answer.append(str(items[idx]))
                items[idx] = -1
            else:
                answer.append('-1')
        # 4. 블렌딩
        elif cmd == 4:
            k = line[1]
            dp = [ INF ] * (k+1)
            dp[0] = 0

            item_set = set(items)
            for it in item_set:
                if it == -1: continue

                for i in range(1, k+1):
                    if i-it >= 0 and dp[i-it] != INF:
                        dp[i] = min(dp[i], dp[i-it]+1)
            answer.append( str(dp[k]) if dp[k]!=INF else '-1' )
        # 5. 향수 구성
        else:
            k = line[1]
            item_set = [v for v in items if v>0]

            # 빈도수 누적합
            arr = [0]*(k+1)

            for a in item_set:
                for b in item_set:
                    arr[ min(k, a+b) ] += 1

            for i in range(k-1, -1, -1):
                arr[i] += arr[i+1]

            cnt = 0
            for c in item_set:
                target_sum = max(k-c, 0)
                cnt += arr[target_sum]
            answer.append(str(cnt))
        # print()

    # 결과 출력
    print('\n'.join(answer))

main()
