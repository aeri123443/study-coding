'''
해적 선장 코디: 2025 하반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy/description

문제 분석: 17m 45s
코드 1차 작성: 47m 49s
 - [시간 소요] 300 상태 교체에서, p가 변동되었는데 큐에 넣은 걸 그냥 쓰면서 우선순위에 오류 발생
1차 디버깅 및 분석: 15m 47s
 - [tc3 fail] q에 (t+r, -p, idx)를 한번에 넣고 t+r 순서로 빼는 바람에, 해당 시간에 발사 가능한 다른 t+r의 선박들이 누락됨
   -> t+r을 하나씩 빼고 비교하는 방법은 시간초과의 여지가 있다고 판단
   -> (-p, idx, t+r) 등의 우선순위 조정도 결국 하나씩 빼서 비교하기 때문에 시간초과의 여지가 있다고 판단
   -> 이에 준비큐, 대기큐로 상태를 분리하는 방안으로 계획 수정
코드 2차 작성: 16m 16s

총 소요 시간: 1h 16m 11s
'''

import heapq

#############################################
### 전역 변수 및 클래스
#############################################

class Item:
    def __init__(self, num, p, r):
        self.num = num
        self.p = p
        self.r = r
        self.ready = 0

T = -1
hour = 0
items = {}
ready_q = []  # 준비 큐: 장전 중 (시간, 아이디)
waiting_q = [] # 대기 큐: 사격 대기 상태 (공격력, 아이디)

#############################################
### 보조 함수
#############################################
def add_item(num, p, r):
    # 아이템 추가
    item = Item(num, p, r)
    items[num] = item

    # 대기큐에 바로 넣음
    heapq.heappush(waiting_q, (-p, num))

# 해당 작업이 대기 상태로 넘어갈 수 있는지 확인
def is_ready(t, num):
    item = items[num]
    return t >= item.ready
#############################################
### 메인 로직
#############################################
def main():
    global T, hour, items, q

    T = int(input())
    answer = []

    for t in range(T):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 매 초마다 준비 큐 -> 대기 큐 진행
        while ready_q:
            rt, num = ready_q[0] # 준비 완료 시간, 넘버

            if is_ready(t, num):
                item = items[num]
                heapq.heappop(ready_q)
                heapq.heappush(waiting_q, (-item.p, num))
            else:
                break


        # 공격 준비
        if cmd == 100:
            n = line[1]
            for i in range(n):
                idx = 2 + i*3
                num, p, r = line[idx:idx+3]
                add_item(num, p, r)
        # 지원 요청
        elif cmd == 200:
            num, p, r = line[1:]
            add_item(num, p, r)
        # 함포 교체
        elif cmd == 300:
            num, p = line[1:]
            item = items[num]
            item.p = p
            # 업데이트된 p를 다시 넣음
            # 준비 상태일 경우, 굳이 다시 넣을 필요가 없음
            # 대기 상태일 경우, 대기 큐에 넣은 후, 향후 p가 다르면 후처리하면 됨
            if is_ready(t, num):
                heapq.heappush(waiting_q, (-p, num))
        # 공격 명령
        elif cmd == 400:
            # 시간 기준, 발포 가능한 선박 리스트를 꺼냄
            # 현재 시간 기준 필수
            candidates = []
            while waiting_q and len(candidates) < 5:
                rev_p, num = waiting_q[0]

                # 상태가 변경되었다면 제거 후 넘어감
                if -rev_p != items[num].p:
                    heapq.heappop(waiting_q)
                    continue

                p = -rev_p
                heapq.heappop(waiting_q)
                candidates.append( (-p, num) )
                # if ready_t <= t:
                #     heapq.heappop(waiting_q)
                #     candidates.append( (-p, num) )
                # else:
                #     break

            # 선박 정렬
            candidates.sort()

            # 공격 완료한 선박을 다시 큐에 넣음 + 정답 기록
            # 디버깅 포인트: candidates가 없을 경우?
            answer_line = [0, len(candidates)]

            for _, num in candidates:
                item = items[num]
                p, r = item.p, item.r

                answer_line[0] += p
                answer_line.append(num)

                item.ready = t+r
                heapq.heappush(ready_q, (t+r, num))

            answer.append( ' '.join(map(str, answer_line)) )

        # print()
    print('\n'.join(answer))

main()