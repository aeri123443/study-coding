'''
118667. k진두 큐 합 같게 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/118667
'''

# 투포인터로 후보 범위 반환
def get_candidate_range(q, target_sum):

    prefix_sum = [0]
    for idx in range(len(q)):
        prefix_sum.append(prefix_sum[-1]+q[idx])

    result = []

    i = 0
    j = 0

    while 0<=j<len(prefix_sum) and 0<=i<len(prefix_sum):
        cur_diff = prefix_sum[j] -prefix_sum[i]

        if cur_diff > target_sum:
            i += 1
        elif cur_diff < target_sum:
            j += 1
        else:
            result.append((i,j))
            j += 1

    return result

def get_least_cal(candidate_range, sj):
    result = float('inf')

    for ei, ej in candidate_range:
        if ej < sj: continue
        result = min(result, ei+ej)

    # si - 0 + ej - sj
    return result - sj if result!=float('inf') else -1

def solution(q1, q2):

    # 타겟합 구하기
    target_sum = sum(q1) + sum(q2)
    if target_sum % 2 != 0: return -1
    target_sum //= 2

    # 투포인터로 후보 범위 반환
    q = [*q1, *q2, *q1]
    candidate_range = get_candidate_range(q, target_sum)

    # 후보 범위 중 가장 연산 수가 적은 경우를 반환
    if not candidate_range:
        return -1

    answer = get_least_cal(candidate_range, len(q1))

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) #2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) #7
print(solution([1, 1], [1, 5]))  #-1
print(solution([3, 10, 1, 1], [1, 1, 1, 2]))