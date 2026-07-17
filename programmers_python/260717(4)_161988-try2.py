'''
161988. 연속 펄스 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/161988
'''

def solution(sequence):
    n = len(sequence)
    # 하나의 펄스 적용 배열만 구하고, 합의 절대값이 가장 큰 값을 구하면 됨
    pulse = [ x if i%2==0 else -x for i, x in enumerate(sequence)]

    # 누적합 구하기
    sum_arr = [0]
    for i in range(n):
        sum_arr.append( sum_arr[-1] + pulse[i] )

    # 누적합 배열의 최대 차이가 정답
    return max(sum_arr) - min(sum_arr)

print(solution([2, 3, -6, 1, 3, -1, 2, 4])) # 10