
'''
Lv. 3 [PCCP 모의고사 #1] 4번 - 운영체제
https://school.programmers.co.kr/learn/courses/20847/lessons/255903
57m 46s
'''

'''
프로그램의 우선순위와 호출된 시각에 따라 실행 순서를 결정
점수가 낮을수록 우선순위가 높은 프로그램

우선순위가 가장 높은 프로그램을 먼저 실행
호출된 각 프로그램은 자신보다 우선순위가 높은 호출된 프로그램이 모두 종료된 후에 실행
 실행 중인 프로그램보다 우선순위가 높은 프로그램이 호출되어도 실행 중이던 프로그램은 중단되지 않고 종료될 때까지 계속 실행됩니다
'''

import heapq

# program [우선순위, 호출시각, 실행시간]
def solution(program):
    answer = [0]*11
    # 호출시각 기준 역순 정렬 
    # 스택처럼 빼면서 관리할 예정
    programs = sorted(program, key=lambda x:x[1], reverse=True)
    # print(programs)

    q = [] # 작업 큐
    # heapq.heappush( q, programs[0] ) # 우선순위, 호출시각, 실행시간
    # t = programs[-1][1] + programs[-1][2] # 가장 먼저 실행된 프로그램이 종료된 시각
    t = 0
    # print(q)
    # temp = [] # 디버깅용 [우선순위, 종료시각, 호출시각, 실제 실행 시각]
    while programs or q:
        # print('t =',t)

        # 현재시각 이전에 호출된 프로그램들을 큐에 담음
        while programs and programs[-1][1] <= t:
            # print(' ', programs[-1])
            heapq.heappush( q, programs.pop() )
        
        # 우선순위가 가장 높은 프로그램 실행
        if q:
            a, b, c = heapq.heappop(q)
            answer[a] += (t - b) # 현재 시각 - 호출시각
            t += c
            # temp.append([a, t, b, t - c])
        # 큐는 비었는데 아직 프로그램이 남아있음
        elif programs:
            t = programs[-1][1]
    
    # print('temp', temp)
    answer[0]=t
    return answer

print()
print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
print([20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0])

print()
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
print([19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0])

# print()
# print(solution())
# print()