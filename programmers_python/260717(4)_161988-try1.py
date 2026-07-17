'''
161988. 연속 펄스 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/161988
'''

def solution(sequence):
    n = len(sequence)
    # 하나의 펄스 적용 배열만 구하고, 합의 절대값이 가장 큰 값을 구하면 됨
    pulse = [ x if i%2==0 else -x for i, x in enumerate(sequence)]

    # 누적합 구하기
    sum_arr = [0, pulse[0]]
    for i in range(1, n):
        sum_arr.append( sum_arr[-1] + pulse[i] )

    # 누적합 배열의 최대 차이(절댓값)가 정답
    # 최대 차이와 최소 차이를 구한 후 절댓값 비교

    # 최대 차이
    print(max())
    min_val = sum_arr[0]
    max_diff = sum_arr[0]
    for i in range(1, n+1):
        cur = sum_arr[i]
        max_diff = max(max_diff, cur - min_val)
        min_val = min(min_val, cur)

    # 최소 차이
    max_val = sum_arr[0]
    min_diff = sum_arr[0]
    for i in range(1, n+1):
        cur = sum_arr[i]
        min_diff = min(min_diff, cur - max_val)
        max_val = max(max_val, cur)

    return max(abs(max_diff), abs(min_diff))

# print(solution([2, 3, -6, 1, 3, -1, 2, 4])) # 10