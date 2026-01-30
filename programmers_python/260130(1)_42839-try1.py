'''
42839. lv2 소수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/42839
21m 34s
'''

from itertools import permutations

# 소수인지 판별하는 함수

def is_prime(x):
    # 2는 소수다
    if x==2: return True
    # 짝수는 소수가 아니다
    if x==1 or x%2 == 0: return False
    # 1과 자신 외의 숫자로 나눠지면 소수가 아니다
    for i in range(3, x, 2):
        if x%i == 0: return False
    return True


def solution(numbers):
    num_arr = list(numbers) # O(7)
    # 순열조합 꺼내고
    # 순열은 set으로 담고   
    answer = 0
    per = set()
    for i in range(1, len(numbers)+1):
        per.update({int(''.join(x)) for x in permutations(num_arr, i)})
    # print(per)
    for x in per:
        if is_prime(x): 
            # print(x)
            answer+=1
    return answer

# print()
# print(solution("17"))
# print(3)


# print()
# print(solution("011"))
# print(2)


print()
print(solution("9365019"))
print()


# print()
# print(solution())
# print()