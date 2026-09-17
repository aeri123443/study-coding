'''
해적 선장 코디: 2025 하반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy

문제 분석: 20m 33s
1차 코드 작성: 53m 6s
  [시간 소요] 300 코드 작성하면서, p가 변경되면 ready_q와 상태가 일치하지 않을 수 있음을 깨달음 -> 좀 고민하다가 item에 ready_time 넣어서 관리하기로 함
  [시간 소요] 300 함수 교체에서 상태 업데이트를 미처 생각하지 못했었고, 해당 부분에서 시간이 소요됨
최종 디버깅: 0m 0s

총 소요 시간: 1h 13m 39s
'''
import heapq

# ===========================
# 전역 및 클래스
# ===========================
DEBUG = False
T, N = -1, -1

ready_q = []
rest_q = []

items = {}

class Item:
    def __init__(self, num, p, r):
        self.num = num
        self.p = p
        self.r = r
        self.ready_time = 0 # 해당 초 이상이 되어야 사격 가능

# ===========================
# 보조 함수
# ===========================

# 함선이 대기상태인지 확인
def is_ready(item, t):
    return item.ready_time <= t

# 초기 함선 입력
def setting_items(line):
    for n in range(N):
        idx = n*3+2
        num, p, r = line[idx: idx+3]

        new_item = Item(num, p, r)
        items[num] = new_item

        heapq.heappush(ready_q, (-p, num))

# 공격할 함선 (최대 5개)
def get_attack_items(t):
    attack_list = []

    cnt = 0
    while ready_q and cnt < 5:
        rev_p, num = heapq.heappop(ready_q)
        item = items[num]

        if not is_ready(item, t):
            continue

        if -rev_p != item.p:
            continue

        attack_list.append(num)
        cnt += 1

    return attack_list

# 장전 완료된 함선 업데이트
def update_queue(t):

    while rest_q:
        if rest_q[0][0] > t:
            return

        rt, num = heapq.heappop(rest_q)
        item = items[num]

        if is_ready(item, t):
            heapq.heappush(ready_q, (-item.p, num))
# ===========================
# 메인 로직
# ===========================
def main():
    global T, N


    T = int(input())
    ans = []

    for t in range(T):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 공격 준비
        if cmd == 100:
            N = line[1]
            setting_items(line)

        # 지원 요청
        elif cmd == 200:
            num, p, r = line[1:]
            items[num] = Item(num, p, r)
            heapq.heappush(ready_q, (-p, num))

        # 함포 교체
        elif cmd == 300:
            # 장전 완료된 함선 업데이트
            update_queue(t)
            if DEBUG: print()

            num, np = line[1:]
            item = items[num]
            item.p = np

            # 사격 대기 상태일 경우, 변경된 공격값을 새로 push
            if is_ready(item, t):
                heapq.heappush(ready_q, (-np, num))

        # 공격 명령
        elif cmd == 400:
            # 장전 완료된 함선 업데이트
            update_queue(t)
            if DEBUG: print()

            # 공격할 함선 (최대 5개)
            attack_list = get_attack_items(t)
            if DEBUG: print()

            # 대미지 계산 및 장전
            total = 0
            for num in attack_list:
                item = items[num]
                total += item.p
                item.ready_time = t + item.r
                heapq.heappush(rest_q, (item.ready_time, num))

            new_print = [total, len(attack_list), *attack_list]
            ans.append(' '.join(map(str, new_print)))

        if DEBUG: print()
    print('\n'.join(ans))

main()