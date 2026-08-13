'''
코드트리 오마카세: 2023 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-omakase

문제 분석: 30m 43s
코드 작성: 41m 18s
최종 디버깅: 0m 0s
총 소요 시간: 1h 12m 1s
'''

# ============================================
# 전역 선언부
# ============================================

L, Q = -1, -1

person = {} # name: [입장 시간, 좌석, 마지막 초밥 먹은 시간(=퇴장 시간)]
food = [] # (t, x, name) 임시로 저장
events = [] # 이벤트 기록 후 정렬. (t, 이벤트 종류)
# ============================================
# 보조 함수
# ============================================

# 기본 데이터 입력
def input_data():
    global L, Q

    L, Q = map(int, input().split())

    for _ in range(Q):
        line = list(input().split())

        # 100: 초밥 제작
        if line[0] == '100':
            t, x, name = int(line[1]), int(line[2]), line[3]
            food.append((t, x, name))
        # 200: 손님 입장
        elif line[0] == '200':
            t, x, name, n = int(line[1]), int(line[2]), line[3], int(line[4])
            person[name] = [t, x, 0] # 입장 시간, 좌석, 마지막 초밥 먹은 시간
        # 300: 사진 촬영
        elif line[0] == '300':
            t = int(line[1])
            events.append((t, 'pic', 0))

# 이벤트 시간 기록
def check_event():

    # 초밥 추가 및 먹히는 시간
    for t, x, name in food:
        # 초밥 추가 이벤트
        events.append((t, 'food', +1))

        b2 = (x - t) % L
        t1 = max(t, person[name][0])

        # t1초에 name 앞에 있는 벨트는?
        x1 = person[name][1]
        b1 = (x1-t1)%L

        # 몇 초 후에 b2이 name(x2) 앞으로 오는지?
        after_t = (b1-b2)%L
        t2 = t1 + after_t

        # 초밥 삭제 이벤트
        events.append((t2, 'food', -1))
        # 손님 마지막 초밥 섭취 시간 업데이트
        person[name][2] = max(person[name][2], t2)

    # 손님 입장 및 퇴장 시간 업데이트
    for name, (in_t, x, out_t) in person.items():
        events.append((in_t, 'person', +1))
        events.append((out_t, 'person', -1))

# ============================================
# 메인 로직
# ============================================
def main():
    # 기본 데이터 입력
    input_data()
    # print()

    # 이벤트 시간 기록
    check_event()
    events.sort() # t, cmd(food->person->pic) 순서 정렬
    # print()

    ans = [] # 정답 기록
    remain = [0, 0]  # 남은 사람 수, 남은 초밥 수
    for _, cmd, d in events:
        if cmd == 'food':
            remain[1] += d
        elif cmd == 'person':
            remain[0] += d
        elif cmd == 'pic':
            ans.append(f'{remain[0]} {remain[1]}')

    print('\n'.join(ans))


main()