'''
12924. lv2 숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924
34m 07s
'''

def solution(n):
    i, j = 1, 2

    answer = 1 # 기본적으로 자기 자신을 포함

    total = i+j
    while i < j:
        # print(i, j, total)
        if total < n:
            j += 1
            total += j

        elif total > n:
            total -= i
            i += 1

        else: # total == n
            # print('total == n', i, j)
            answer += 1
            j += 1
            total = total - i + j
            i += 1

    return answer

print(solution(15))
print(solution(1))
print(solution(2))
print(solution(10))