'''
12920. 선입 선출 스케줄링
https://school.programmers.co.kr/learn/courses/30/lessons/12920

경곗값 이분탐색 숙지!!
'''

def solution(n, cores):
    cores_len = len(cores)
    # n개의 작업을 완료하는 T초 찾기 (이분탐색)
    left = 0 # 최소 시간
    right = (n // cores_len + 1) * max(cores) # 최대 시간

    target_t = None
    while left < right:
        mid = (left+right)//2
        complete_num = sum( mid//c + 1 for c in cores )
        # print(left, right, mid, complete_num)
        if complete_num < n:
            left = mid + 1
        elif complete_num > n:
            right = mid - 1
        else:
            target_t = mid
            break
    if target_t is None: target_t = left
    # print('target_t', target_t)

    # T-1초에서 얼마나 작업이 진행되었는지?
    complete_cnt = sum( (target_t-1)//c + 1 for c in cores )
    # print(target_t, complete_cnt)

    # T초에서 n번째 작업이 어디서 완료되는지 확인
    for t in range(target_t, target_t+2):
        for idx, c in enumerate(cores):
            if t % c == 0:
                complete_cnt += 1
                if complete_cnt == n:
                    return idx+1
        # print(t, complete_cnt)
    return -1

print(solution(6, [1,2,3]))
print(solution(9, [1,2,3]))
print(solution(14, [1,2,3]))
print(solution(16, [1,2,3]))
print(solution(17, [1,2,3]))

# 최소
print(solution(1, [1,2,3]))
