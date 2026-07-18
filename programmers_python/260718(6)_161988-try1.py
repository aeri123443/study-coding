'''
161988. 연속 펄스 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/161988
'''

def solution(sequence):
    arr = [0] + [ v if i%2==0 else -v for i, v in enumerate(sequence)]
    for i in range(1, len(sequence)+1):
        arr[i] += arr[i-1]

    return max(arr) - min(arr)

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))