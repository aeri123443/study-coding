'''
12920. 선입 선출 스케줄링
https://school.programmers.co.kr/learn/courses/30/lessons/12920

시간초과
'''

def solution(n, cores):
    task_num = 1
    cores_len = len(cores)
    # 작업 리스트 (작업중인 번호, 작업 완료 시간)
    core_list = [(0,0) for _ in range(cores_len)]

    t = 0
    while True: # 작업 끝날 때까지
        t += 1

        for i in range(cores_len):
            working_num, complete_time = core_list[i] #향후 working_num 제거 가능

            if  complete_time == 0 or complete_time == t:
                core_list[i] = [task_num, t+cores[i]]
                if task_num == n: return i+1
                task_num += 1
        # print(t, core_list)
        if task_num > n :
            break

    return None

print(solution(6, [1,2,3]))
print(solution(9, [1,2,3]))
print(solution(14, [1,2,3]))

# 최소
print(solution(1, [1,2,3]))
