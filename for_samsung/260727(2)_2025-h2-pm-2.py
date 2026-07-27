'''
가로등 설치: 2025 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/street-light-installation/description

문제 분석: 19m 43s
코드 1차 작성: 2h 0m 42s
  - [코드 작성 오래 걸림] 연결리스트를 사용할지를 계속 고민하면서 코드를 고침
디버깅: 6m 54s
  - [tc16 fail] heapq 우선순위 잘못 설정함 (-dis, xa, xb, a, b)로 해야 했는데, (-dis, a, b)로 하여 오류 발생.
    -> 문제에서 dis가 같을 경우 x 좌표값이 적은 순서대로라고 나와 있는데, 그냥 item 번호를 기준으로 최소힙을 구현해버림 ㅠ ,,
코드 2차 작성: 6m 15s
총 소요 시간: 2h 33m 37s
'''

import heapq
import math

############################################
#### 전역 및 클래스
############################################

class Item:
    def __init__(self, num, x):
        self.num = num
        self.x = x
        # 연결리스트 응용: 이전, 다음에 대한 번호 정보
        self.prev = None
        self.next = None

INF = float('inf')
N, M, Q = -1, -1, -1
items = {}
max_num = -1 # 현재 최대 번호
hq = []
# sides = [(), ()] # 양끝 가로등 넘버 [(왼쪽 사이드: 거리, num), (오른쪽 사이드: 거리, num)]
front = None
rear = None

############################################
#### 보조 함수
############################################
def get_max_dis_inside():
    dis, xa, xb, a, b = -1, -1, -1, -1, -1
    while hq:
        dis, xa, xb, a, b = heapq.heappop(hq)  # 디버깅 포인트: dis가 홀수일 경우
        if a in items and b in items:
            break

    return -dis, xa, xb, a, b
############################################
#### 메인 로직
############################################
def main():
    global N, M, Q, items, max_num, hq, front, rear

    answer = []
    Q = int(input())

    for _ in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 상태 확인
        if cmd == 100:
            N, M = line[1], line[2]
            m_list = line[3:]

            max_num = M
            # 아이템 일괄 추가 및 거리 정보 저장
            items = { i+1:Item(i+1, v) for i, v in enumerate(m_list) }

            for num, item in items.items():
                if num == 1:
                    front = item
                else:
                    if num == M:
                        rear = item

                    prev_item = items[num-1]

                    # 최대 거리 업데이트
                    tmp_distance = (prev_item.x-item.x, prev_item.x, item.x, prev_item.num, item.num) # (-거리, s, e)
                    heapq.heappush(hq, tmp_distance)

                    # 아이템 연결
                    prev_item.next = item
                    item.prev = prev_item
        # 가로등 추가
        elif cmd == 200:
            dis, xa, xb, a, b = get_max_dis_inside()

            a_item, b_item = items[a], items[b]
            max_num += 1


            # 리스트 연결
            new_item = Item(max_num, a_item.x + math.ceil(dis/2)) # 디버깅 포인트: 반올림 여부
            # new_distance = new_item.x - a_item.x
            items[max_num] = new_item

            a_item.next = new_item
            new_item.prev = a_item
            new_item.next = b_item
            b_item.prev = new_item

            # 최대 거리 정보 업데이트
            heapq.heappush(hq, (a_item.x-new_item.x, a_item.x, new_item.x, a, max_num))
            heapq.heappush(hq, (new_item.x-b_item.x, new_item.x, b_item.x, max_num, b))
        # 가로등 제거
        elif cmd == 300:
            d_num = line[1]
            d_item = items[d_num]

            # f, r 업데이트
            if d_item == front:
                front = front.next
                front.prev = None
            elif d_item == rear:
                rear = rear.prev
                rear.next = None
            else:
                next_item = d_item.next
                prev_item = d_item.prev
                new_distance = next_item.x - prev_item.x

                prev_item.next = d_item.next
                next_item.prev = d_item.prev

                heapq.heappush(hq, (-new_distance, prev_item.x, next_item.x, prev_item.num, next_item.num) )

            del items[d_num]

        # 최소 전력 계산
        elif cmd == 400:
            dis, xa, xb, a, b = get_max_dis_inside()
            heapq.heappush(hq, (-dis, xa, xb, a, b)) # 다시 큐에 넣어야 함

            r = max( (front.x-1), (N-rear.x), dis/2  )
            answer.append( str(int(r*2)) )

        # print()
    print('\n'.join(answer))

main()