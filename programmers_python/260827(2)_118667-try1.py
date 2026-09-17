'''
118667. 두 큐 합 같게 만들기

https://school.programmers.co.kr/learn/courses/30/lessons/92335
'''
P = 'pop'
I = 'insert'
INF = float('inf')

# qa에서 빼고, qb의 값을 넣는 연산 -> 이후 슬라이딩 윈도우로 최솟값 리턴
def least_cal(qa, sum_a, qb, target_sum):
    arr = []

    arr.append((sum_a, 0, P))
    for i, a in enumerate(qa):
        sum_a -= a
        arr.append((sum_a, i+1, P))

    sum_b = 0
    arr.append((sum_b, 0, I))
    for i, b in enumerate(qb):
        sum_b += b
        arr.append((sum_b, i+1, I))

    arr.sort()

    min_cal = INF
    s, e = 0, len(arr)-1

    def check_next_same(_s, _e):
        # s의 다음이나 e의 다음이 같은 값일 경우, 편의상 그 포인터를 먼저 이동
        if _s+1 < len(arr) and arr[_s] == arr[_s+1]:
            return True, (_s+1, _e)
        elif _e-1 >= 0 and arr[_e] == arr[_e-1]:
            return True, (_s, _e-1)
        else:
            return False, (_s, _e)

    while s < e:
        cur_sum = arr[s][0] + arr[e][0]
        s_tu = arr[s]
        e_tu = arr[e]

        if cur_sum == target_sum and s_tu[2]!=e_tu[2]:
            min_cal = min(min_cal, s_tu[1]+e_tu[1])

        next_same, next_pos = check_next_same(s, e)

        if next_same:
            s, e = next_pos
            continue

        if cur_sum <= target_sum:
            s += 1
        else:
            e -= 1

    return min_cal

def solution(q1, q2):

    # 타겟값 계산
    q1_sum = sum(q1)
    q2_sum = sum(q2)

    # 두 수의 합이 홀수면, 두 배열의 합을 같게 만들 수 없음
    if (q1_sum+q2_sum) % 2 != 0:
        print()
        return -1

    target_sum = (q1_sum+q2_sum) // 2
    min1 = least_cal(q1, q1_sum, q2, target_sum)
    min2 = least_cal(q2, q2_sum, q1, target_sum)
    print()

    answer = min(min1, min2)

    return answer if answer!=INF else -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) #2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) #7
print(solution([1, 1], [1, 5]))  #-1