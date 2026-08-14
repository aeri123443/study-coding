'''
코드트리 채점기: 2023 상반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-judger

문제 분석: 59m 21s
  - [시간 소요] 시간 복잡도를 줄이는 방향에 대해 gemini와 상의
코드 작성: 1h 11m 28s
  - [시간 소요] 상태 관리 할 자료구조가 많아서 신중하게 코딩함...
1차 디버깅: 2m 43s
  - [TC2 error] 채점 종료 시, 채점 진행중이지 않은 채점기면 넘어간다는 조건을 잊어서 에러가 발생

총 소요 시간: 2h 13m 34s
'''

import heapq
from collections import defaultdict

# ================================================
# 전역 선언
# ================================================
Q, N = -1, -1
INF = float('inf')

# 대기 큐
waiting_q = defaultdict(list) # domain: heapq(우선순위, 요청 시간, url_id)
waiting_set = set() # 대기중인 url 목록(도메인, url_id)

# 진행 중 / 쉬는 채점기
task_set = set() # 작업중인 domain 목록
ready_items = [] # 쉬고 있는 채점기 heapq (jid)
task_items = {} # 일하고 있는 채점기 (jid: ud, ui, 채점 시작 시간)

# 채점 종료
history = defaultdict(int) # 도메인: 이후 채점 가능 시간

# ================================================
# 보조 함수
# ================================================

# 대기 큐에 작업 추가
def append_waiting_q(t, p, u):
    ud, ui = u.split('/')

    # 같은 url이 채점 대기 큐에 있을 경우 추가하지 않음
    if (ud, ui) in waiting_set: return

    # 대기 큐와 대기 셋에 추가
    heapq.heappush(waiting_q[ud], (p, t, ui))
    waiting_set.add((ud, ui))


# 채점 가능한 도메인들의 최우선순위 리스트 중에서, 가장 우선순위를 가지는 것!
def get_task_item(t):
    item_info = (INF, INF, INF, INF) # (p, t, ud, ui)

    for ud in waiting_q:

        # 채점 진행중인 도메인이면 넘어감
        if ud in task_set: continue

        # 최근 완료된 도메인이 있고, 채점 가능 시간 전이면 넘어감!
        if ud in history and t < history[ud]: continue

        top_p, top_t, top_ui = waiting_q[ud][0]
        item_info = min(item_info, (top_p, top_t, ud, top_ui)) # (p, t, ud, ui)

    if item_info[0] == INF: return -1,-1,-1,-1

    # 선정된 작업을 대기 큐에서 제거 및 반환
    heapq.heappop(waiting_q[item_info[2]])
    waiting_set.remove((item_info[2], item_info[3]))

    if not waiting_q[item_info[2]]:
        del waiting_q[item_info[2]]

    return item_info
# ================================================
# 메인 로직
# ================================================
def main():
    global Q, N, ready_items

    Q = int(input())
    ans = []

    for _ in range(Q):
        line = list(input().split())
        cmd = line[0]

        # 채점 준비
        if cmd == '100':
            N, u = int(line[1]), line[2]
            ready_items = [jid for jid in range(1, N+1)]
            heapq.heapify(ready_items)
            append_waiting_q(0, 1, u)

        # 채점 요청
        elif cmd == '200':
            t, p, u = int(line[1]), int(line[2]), line[3]
            append_waiting_q(t, p, u)

        # 채점 시도
        elif cmd == '300':
            # 쉬는 채점기가 없으면 pass
            if len(task_items) == N: continue

            t = int(line[1])

            # 채점 가능한 도메인들의 최우선순위 리스트 중에서, 가장 우선순위를 가지는 것!
            _, _, ud, ui = get_task_item(t)

            # 채점 가능한 도메인이 없을 경우 넘어감
            if ud == -1: continue

            # 채점 시작
            jid = heapq.heappop(ready_items) # 번호가 가장 작은 채점기
            task_items[jid] = (ud, ui, t) # (jid: ud, ui, 채점 시작 시간)
            task_set.add(ud)

        # 채점 종료
        elif cmd == '400':
            end_t, jid = int(line[1]), int(line[2])

            # 진행중이지 않으면 넘어감
            if jid not in task_items: continue

            # 작업 중 / 쉬는 채점기 업데이트
            ud, ui, start_t = task_items[jid]
            task_set.remove(ud)
            heapq.heappush(ready_items, jid)
            del task_items[jid]

            # 채점 종료 업데이트
            gap = end_t - start_t
            standard_t = start_t + 3 * gap
            history[ud] = standard_t

        # 채점 대기 큐 조회
        elif cmd == '500':
            total = 0
            for q in waiting_q.values():
                total += len(q)
            ans.append(total)
        # print()
    print('\n'.join(map(str, ans)))

main()