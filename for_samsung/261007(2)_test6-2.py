# 1회독 7m 56s
# 2회독 16m 45s
# 설계 32m 48s + 3m 18s
#
# [!] 나무가 같은 위치에 중복으로 주어질 경우
# [!] 실행큐 굳이 필요 없을 것 같은데?? 그냥 다음 활동가능시간을 대기큐에 새로 넣으면 될듯.
# [!] 점수도 바로 업데이트해도 어차피 큐에 있는동안은 못 수확하니까 상태 꼬일 일 없을듯
#


import heapq
from collections import defaultdict

DEBUG= True
INF = float('inf')

Q = int(input())
N = int(input().split()[1])

trees = {}
people = {}

people_q = []
tree_q = []

# 나무
class Tree:
    def __init__(self, num, t, r, c, a, b):
        self.num = num
        self.pos = (r,c)
        self.start = (t+a) # T + a부터 성숙(수확 가능)
        self.end = (t+b) # T + b 되는 순간 열매 썩음 (수확 실패)

# 가드너(최대 20)
# - 상태
#     - 대기
#         - 처음 활동 시작
#         - 수확 마친후 복귀
#     - 수확중
#         - T + (해당 나무까지의 택시 거리)*2 이후 에 복귀
class Person:
   def __init__(self, num, t, r, c, d):
       self.num = num
       self.pos = (r, c) # r, c 집
       self.t = t # 활동 시작 시간
       self.max_d = d # d 거리 이내의 나무만 수확가능
       self.tree_q = [] # 우선순위에 따른 나무큐
       self.score = 0

# 전역 입력 12m 06s
#     -
#
# 가드너: 수확 가능한 나무
#     - 필수 조건
#         1. 아직 다른 가드너가 수확하지 않음, 수확할 예정도 아님
#         2. 집 -> 나무 거리 d 이내
#         3. 출발하는 시점에, 나무가 수확가능 (성숙했고, 안 썩었고)
#         4. 도착한다고 했을 때에도 썩지 않아야 함
#     - 우선순위
#         1) 거리최소
#         2) 썩는 시간 최소 -> 성숙 시간최소
#         3) 행최소 -> 열최소

# 시각 T
#     1. 나무심기 or 가드너 활동 시작
#     2. 집으로 복귀하는 가드너를 대기 상태로
#     3. 대기 상태인 모든 가드너는 '특정 시각 행동 결정 과정'에 따라 자신의 행동을 결정

def cal_dis(ar, ac, br, bc):
    return abs(ar-br) + abs(ac-bc)

# 초깃값 입력
def input_data(): # 36m 44s
    # 나무/가드너 정보를 {}에 저장
    t_num = 1
    p_num = 1
    for _ in range(Q-1):
        cmd, t, c, r, *other = map(int, input().split())
        if cmd == 200: # 나무
            a, b = other
            tree = Tree(t_num, t, r, c, a, b)
            trees[t_num] = tree
            heapq.heappush(tree_q, (tree.start, tree.num))
            t_num += 1
        elif cmd == 300: # 가드너
            d = other[0]
            person = Person(p_num, t, r, c, d)
            people[p_num] = person
            heapq.heappush(people_q, (t, person.num))

            p_num+=1

    # for 나무, 각 가드너에게 나무 우선순위 큐
    for tree in trees.values():
        tr, tc = tree.pos
        for person in people.values():
            # 필수 조건
            # 1. 집 -> 나무 거리 d 이내
            # 2. 출발하는 시점에, 나무가 수확가능 (성숙했고, 안 썩었고)
            # 3. 도착한다고 했을 때에도 썩지 않아야 함
            d = cal_dis(tr, tc, *person.pos)
            if person.max_d >= d and person.t+d < tree.end:
                # 우선순위
                # 1) 거리최소
                # 2) 썩는 시간 최소 -> 성숙 시간최소
                # 3) 행최소 -> 열최소
                info = (d, tree.end, tree.start, tr, tc, tree.num)
                heapq.heappush(person.tree_q, info)

def main():
    # 0. 초깃값 입력
    input_data()
    if DEBUG: print()

    while tree_q or people_q:
        # q[0] 기준 T값 츠츨
        t = max(tree_q[0][0] if tree_q else -INF, people_q[0][0] if people_q else -INF)

        # 1-2. 큐에 있던 가드너/나무 중 T초 전인 원소들 추출
        tree_set = set()
        while tree_q:
            if tree_q[0][0] <= t:
                _, t_num = heapq.heappop(tree_q)
                tree_set.add(t_num)
            else: break
        people_set = set()
        while people_q:
            if people_q[0][0] <= t:
                _, p_num = heapq.heappop(people_q)
                people_set.add(p_num)
            else: break


        # 해당 시각 T에 더 행동할 가드너가 없을 때까지 반복
        acted = set() # 이번 턴에서 행동한 가드너
        cannot = set() # 이번 턴에서 행동하지 못하는 가드너
        while len(people_set) != len(acted)+len(cannot) and trees:
            # 나무: 수확 규칙
            # 1. 각 가드너의 최우선 목표 선택
            want_tree_dict = defaultdict(list) # 각 나무를 차지하려고 하는 가드너 목록
            for p_num in people_set:
                if p_num in acted or p_num in cannot: continue
                t_num = -1
                person = people[p_num]

                ptq = person.tree_q
                while ptq:
                    dis, te, ts, tr, tc, tn = heapq.heappop(ptq)
                    if tn in trees and tn in tree_set and t+dis*2 < te:
                        t_num = tn
                        break

                # [!] 한번 안 되면 이 턴에서는 아예안될거라 걍 후보에서 빼도 될듯
                if t_num == -1:
                    cannot.add(p_num)
                else: # 경쟁 우선순위에 따라 넣음
                    heapq.heappush(want_tree_dict[t_num], (person.score, person.num))

            # 2. 경쟁 발생 및 승자 결정
            # - 선택된 나무가 없으면 종료
            if not want_tree_dict:
                break

            act_candidate = []
            for t_num, q in want_tree_dict.items():
                # 우선순위에 따라 나무 선점자 결정
                heapq.heappush(act_candidate, (q[0][1], t_num))

            # 3. 최종 행동 가드너
            final_act, final_t_num = heapq.heappop(act_candidate)

            # 4. 상태 변경 및 과정 반복
            acted.add(final_act)
            for t_num, q in want_tree_dict.items():
                tree = trees[t_num]
                tr, tc = tree.pos
                for _, p_num in q:
                    if p_num != final_act:
                        person = people[p_num]
                        heapq.heappush(person.tree_q, (cal_dis(tr, tc, *person.pos), tree.end, tree.start, tr, tc, t_num))
            del trees[final_t_num]
        print()
        # 과정이 끝나면
    print()
    #     - 도착시간 등 이슈로 해당 시각에 나무를 못 뽑는 가드너가 있을 수 있음 ->따로 빼두기
main()