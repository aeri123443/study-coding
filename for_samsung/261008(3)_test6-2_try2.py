"""
6-2 신비의 숲의 가드너
https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4806/curated-cards/mock-woodcutter/description
시간초과, 향후 수정

설계 원본.
시간 흐름
    1) 나무 심기 or 가드너 활동 시작
    2) 대기 상태 변경 (복귀)
    3) 대기 상태인 가드너의 행동 결정

N*N

전역값
- 시간 기준 힙큐 (이벤트 큐)
    - 0 나무 성장
    - 1 가드너 대기상태
    - 2 나무 제거
- {나무들}
- {가드너들}
- 나무 class
- 가드너 class
- {현 시점 존재하는 나무}, {현 시점 존재하는 가드너}

기타 상태 관리
- 가드너별 힙큐

나무
    - 나무 번호 t 기준으로 지정하기
    - T 시각,(r,c)
    - 수확: T+a <= x < T+b
    - 수확된 나무는 다시 수확 불가

가드너
    - 번호: 1부터 입력순
    - T 시각,(r,c)
    - 택시거리 d 이내의 나무만 / 맨해튼
    - 수확 횟수
    - 가드너 별 나무 힙큐
    상태
        - 대기
            - 처음 활동 시작
            - 수확 끝나고 복귀한 후
        - 수확중
            - T + 택시거리*2 -> 복귀(대기)

가드너가 수확 가능한 나무
    조건
        - 수확됨/수확예정 아님
        - 거리 d 이내
        - 출발하는 시점에 수확 가능 상태
        - 도착하는 시점(T+d)에 썩지 않아야 함
    우선순위
        1) 거리 최소
        2) 썩는 시간최소
        3) 성숙 시각 최소
        4) 행 최소
        5) 열 최소

def 대기 상태 가드너의 최우선 목표 선택 # (조건/우선순위 참고)
    - 대기 가드너 set, 현재 존재하는 나무 set
    - 가드너 개인 큐에서 나무 뽑았는데 현존나무에 없으면 다시 뽑음
    - 반환: {tree: heapq(경쟁자 우선순위)}

def 경쟁 발생 및 승자 결정, 최종 행동 가드너 확정
    min = (가드너의 총 수확 개수, 가드너 고유 번호)
    - params: {tree: heapq(경쟁자 우선순위)}
    - params 순회하며 각 tree에 대한 경쟁 승자를 min에 업뎃ㅅ
    - return: 최종 행동 가드너

def 나무 수확 (규칙)
    1. def 대기 상태 가드너의 최우선 목표 선택 (조건/우선순위 참고)
        - 수확 가능한 나무가 없으면, 이번 턴 pass
    * 결정 가능한게 없으면 빈 값 반환
    2. def 경쟁 발생 및 승자 결정
        - 둘 이상의 가드너가 같은 나무 선택
            1) 총 수확 개수 최소
            2) 고유번호 최소
    3. 최종 행동 가드너 확정 --> 2.와 합침
        -> 2 중에서 고유번호 최소 한 명
    4. 상태 변경 및 과정 반복
        - 수확한 가드너 -> 시간 계산해서 전체 큐에 넣고. 점수 추가
        - {현재 존재하는 나무}에서 빼고
        - {전체 나무}에서도 빼거..

0. 값 입력 및 전처리
    - 명령 훑기
        - 나무 추가 -> 바로 이벤트 큐랑 나무 dict에 저장, 나무 사라지는 순간도 이벤트 큐에저장!
        - 가드너 추가 -> 일단 개인큐 빼고 다 저장(투입 시간 이벤트 큐랑 가드너 dixt에)
    - 가드너 개별 큐 추가
        - 거리 d 이내의 모든 나무에 대해 힙큐 생성


1. 이벤트 큐 탐색
    - T에 해당하는 모든 것을 담음
    - 나무 심기 -> 가드너 대기상태 -> 나무 제거
        - {현 시점 존재하는 나무}, {현 시점 존재하는 가드너} 업데이트
    - while 해당 시각에 더 수확할 나무를 선택하는 가드너가 없을 때까지
        - def 나무 수확
        - 수확 가능한 나무가 없으면(빈 값 반환받으면) break

"""

# # 1회독 2:44
# # 2회독 10:45
# # 설계 37:57
# # 표 작성 10:20
# # 총 소요 시간 2h 22m 27s


# 시간 흐름
#     1) 나무 심기 or 가드너 활동 시작
#     2) 대기 상태 변경 (복귀)
#     3) 대기 상태인 가드너의 행동 결정

import heapq
from collections import defaultdict

# N*N
DEBUG = False
INF = float('inf')
Q = int(input())
N = list(map(int, input().split()))[1]

# 전역값
events = [] # 시간 기준 힙큐 (이벤트 큐): (시간, 이벤트 번호 0 나무 추가(성숙_, 1 가드너 대기상태, 2 나무 썩음(제거))
trees = {} # {나무번호: 나무들}
gardeners = {} # - {가드너번호: 가드너들}
cur_gardeners = set() # {현 시점 존재하는 가드너}
cur_trees = set() # {현 시점 존재하는 나무}

# 나무
class Tree:
    def __init__(self, t, r, c, a, b):
        self.num = t # 변수 헷갈리니 그냥 분리함
        self.t = t
        self.start = t+a
        self.end = t+b
        self.pos = (r,c)

    def able(self, _t): # 수확 가능 여부 판정
        return self.start<=_t<self.end


# 가드너
class Gardener:
    def __init__(self, num, t, r, c, d):
        self.num = num
        self.t = t
        self.pos = (r,c)
        self.d = d
        self.tree_q = [] # 나무 우선순위
        self.cnt = 0 # 수확횟수


# 여기까지 12:35

# 0. 값 입력 및 전처리
def input_and_preprocess(): # 17:28
    # 1. 명령 훑기
    for _ in range(Q-1):
        cmd, t, r, c, *other = map(int, input().split())

        # 나무 추가 -> 바로 이벤트 큐랑 나무 dict에 저장, 나무 사라지는 순간도 이벤트 큐에저장!
        if cmd == 200:
            a, b = other
            tree = Tree(t, r, c, a, b)
            heapq.heappush(events, (tree.start, 0, tree.num))
            heapq.heappush(events, (tree.end, 2, tree.num))
            trees[tree.num] = tree

        # 가드너 추가 -> 일단 개인큐 빼고 다 저장(투입 시간 이벤트 큐랑 가드너 dict에)
        elif cmd == 300:
            d = other[0]
            gardener = Gardener(len(gardeners), t, r, c, d)
            heapq.heappush(events, (gardener.t, 1, gardener.num))
            gardeners[gardener.num] = gardener

    # 2. 가드너 개별 큐 추가
    for tree in trees.values():
        for gardener in gardeners.values():
            # 거리 d 이내의 모든 나무에 대해 힙큐 생성
            gr, gc = gardener.pos
            tr, tc = tree.pos
            dis = abs(gr-tr) + abs(gc-tc)
            if dis <= gardener.d:
                # 우선순위: 1) 거리 최소 2) 썩는 시간최소 3) 성숙 시각 최소 4) 행 최소 5) 열 최소
                heapq.heappush(gardener.tree_q, (dis, tree.end, tree.start, tr, tc, tree.num))

# 1-1. 특정 시각에 해당하는 모든 이벤트 큐를 추출
# - 나무 심기 -> 가드너 대기상태 -> 나무 제거
# - {현 시점 존재하는 나무}, {현 시점 존재하는 가드너} 업데이트
def pop_event_q(): # 8:47
    turn = events[0][0]
    while events and events[0][0] == turn:
        _, cmd, num = heapq.heappop(events)
        if cmd == 0:
            cur_trees.add(num)
        elif cmd == 1:
            cur_gardeners.add(num)
        elif cmd == 2:
            if num in cur_trees: cur_trees.remove(num)
            if num in trees: del trees[num]
    return turn

# def 대기 상태 가드너의 최우선 목표 선택 # (조건/우선순위 참고)
def gardeners_want_trees(turn):
    gardeners_want = defaultdict(list)

    for g_num in cur_gardeners:
        g = gardeners[g_num]
        # 거리 순서 정렬이었어서... 아직 성장하지 않은걸지도 모름. 전체 나무에 없던 거 아닌 이상 모아뒀다가 다시 넣자
        tmp = []
        tq = g.tree_q
        while tq:
            dis, te, ts, tr, tc, tn = tq[0]

            if tn not in trees:
                heapq.heappop(tq)
                continue

            tree = trees[tn]
            # 조건 만족하나?
            # - 수확됨/수확예정 아님
            # - 거리 d 이내 -> 아니었으면 tq에 안담겻음
            # - 출발하는 시점에 수확 가능 상태
            # - 도착하는 시점(T+d)에 썩지 않아야 함
            if tn in cur_trees and tree.able(turn) and tree.able(turn+dis):
                heapq.heappush(gardeners_want[tn], (g.cnt, g.num)) # 1) 총 수확 개수 최소 2) 고유번호 최소
                break
            else:
                tmp.append(heapq.heappop(tq))

        for hq in tmp: heapq.heappush(tq, hq)

    return gardeners_want

def get_final_actor(gardeners_want):
    final = (INF, INF)

    for t_num in gardeners_want.keys():
        g_num = gardeners_want[t_num][0][1]
        final = min(final, (g_num, t_num))

    return final

# def 나무 수확 (규칙)
# ㅋㅋㅋㅋㅋㅋㅋ수확을 영어로 모름 ㅠㅠ 땡스기빙데이~
def thanks_tree(turn):
    # ========================================================
    # 1. 대기 상태 가드너의 최우선 목표 선택 (조건/우선순위 참고)
    #     - 수확 가능한 나무가 없으면, 이번 턴 pass
    # ========================================================
    gardeners_want = gardeners_want_trees(turn)
    if not gardeners_want: return False

    # ========================================================
    # 2. 경쟁 발생 및 승자 결정, 3. 최종 행동 가드너 확정
    # - 둘 이상의 가드너가 같은 나무 선택
    #     1) 총 수확 개수 최소
    #     2) 고유번호 최소
    # -> 2 중에서 고유번호 최소 한 명
    # ========================================================
    final_actor, final_tree  = get_final_actor(gardeners_want)

    # 아맞다... 1.~3.까지 35:50
    
    # ========================================================
    # 4. 상태 변경 및 과정 반복 8:9
    #     - 수확한 가드너 -> 시간 계산해서 전체 큐에 넣고. 점수 추가
    #     - {현재 존재하는 나무}에서 빼고
    #     - {전체 나무}에서도 빼거..
    # ========================================================
    tr, tc = trees[final_tree].pos
    cur_trees.remove(final_tree)
    del trees[final_tree]
    cur_gardeners.remove(final_actor)
    
    fa = gardeners[final_actor]
    fa.cnt += 1
    
    gr, gc = fa.pos
    dis = abs(gr-tr) + abs(gc-tc)
    heapq.heappush(events, (dis*2+turn, 1, final_actor))
    # if DEBUG: print()
    return True

def main():
    # ======================================================
    # 0. 값 입력 및 전처리
    # ======================================================

    input_and_preprocess()
    # # if DEBUG: print()

    # ======================================================
    # 1. 이벤트 큐 탐색
    # ======================================================
    while events and trees:

        # 1-1. 특정 시각에 해당하는 모든 이벤트 큐를 추출
        turn = pop_event_q()

        # while 해당 시각에 더 수확할 나무를 선택하는 가드너가 없을 때까지
        while True:
            if not thanks_tree(turn):
                break

            # - def 나무 수확
        # - 수확 가능한 나무가 없으면(빈 값 반환받으면) break
            # if DEBUG: print()

    # 출력 결과 작성 및 예제 케이스 4개 대조 1:29
    answer = []
    for g_num in range(len(gardeners)):
        answer.append(gardeners[g_num].cnt)

    print(' '.join(map(str, answer)))

main()

# 다른 케이스 없나 3:41
# 가드너 한명이고, 나무가 없을때 -> 0 출력 확인
# 나무 하나고, 가드너 없을,,.,?? -> 출력 방식이 달라질텐데, 지문에 없는 걸 보니 ㄱㅊ을듯