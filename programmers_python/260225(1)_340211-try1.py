'''
340211. [PCCP 기출문제] 3번 / 충돌위험 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/340211
1h 13m 20s
굳이 모든 경로를 저장할 필요는 없음!
'''

'''
모든 로봇은 0초에 동시에 출발
로봇은 1초마다 r 좌표와 c 좌표 중 하나가 1만큼 감소하거나 증가한 좌표로 이동
항상 최단 경로로 이동하며 최단 경로가 여러 가지일 경우, r 좌표가 변하는 이동을 c 좌표가 변하는 이동보다 먼저
로봇이 물류 센터를 벗어나는 경로는 고려하지 않습니다.

로봇이 2대 이상 모인다면 충돌할 가능성이 있는 위험 상황
'''

from collections import defaultdict, deque, Counter
from pprint import pprint

def solution(points, routes):
    robot_nums = len(routes)
    
    ###########
    ### 각 로봇의 실제 이동 좌표 저장
    ###########
    route_dict = defaultdict(list)
    max_len = 0

    # 시작 좌표 넣기
    for i in range(robot_nums):
        sr, sc = points[routes[i][0]-1]
        route_dict[i+1].append( (sr, sc) )

    for i, route in enumerate(routes):
        robot = i+1
        cp = route[0]

        for np in route:
            if cp==np: continue # 첫 좌표 패스

            r1, c1 = points[cp-1]
            r2, c2 = points[np-1]

            r_cnt, c_cnt = r2-r1, c2-c1

            def append_route(cnt, drc, robot):
                nonlocal route_dict
                
                # print(route_dict[robot])
                # print(route_dict[robot][-1])
                cr, cc = route_dict[robot][-1]
                
                for _ in range(cnt): 
                    cr, cc = cr+drc[0], cc+drc[1]
                    route_dict[robot].append( (cr, cc) )


            # r 먼저 이동
            if r_cnt>0:
                append_route(abs(r_cnt), (+1, 0), robot)
            elif r_cnt<0:
                append_route(abs(r_cnt), (-1, 0), robot)

            # c 이동
            if c_cnt>0:
                append_route(abs(c_cnt), (0, +1), robot)
            elif c_cnt<0:
                append_route(abs(c_cnt), (0, -1), robot)

            cp = np

        max_len = max(max_len, len(route_dict[robot]))

    # print(max_len)
    # pprint(route_dict)

    ###########
    ### 각 로봇에 대하여 충돌 검사
    ###########

    answer = 0
    for i in range(max_len):
        # print(route_dict)
        tmp_counter = Counter(rt[i] for rt in route_dict.values() if len(rt)>i)
        # pprint(tmp_counter)
        for v in tmp_counter.values():
            if v > 1:
                answer += 1

    return answer

print()
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(1)

print()
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(9)

print()
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))
print(0)

# print()
# print(solution())
# print()