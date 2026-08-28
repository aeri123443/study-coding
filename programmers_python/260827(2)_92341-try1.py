'''
92335. k진수에서 소수 개수 구하기

https://school.programmers.co.kr/learn/courses/30/lessons/92335
'''

# 진수 변환
def cal_k(n, k):
    if k == 10: return str(n)

    result = []
    while n >= 1:
        result.append(str(n % k))
        n //= k

    return ''.join(result[::-1])

# 소수 반환 함수
def is_prime(num):
    if num == 1: return False
    if num == 2: return True

    i = 2
    while i * i <= num:
        if num % i == 0 : return False
        i += 1

    return True


def solution(n, k):
    # print('00100100010'.split('0'))  # ['', '', '1', '', '1', '', '', '1', '']

    # 10진수 -> k 진수
    new_k = cal_k(n, k)

    # 0 스플릿, 빈 값 제거
    split_0 = [int(x) for x in new_k.split('0') if x]
    # 개수 카운트
    cnt = 0
    for x in split_0:
        if is_prime(x): cnt += 1

    return cnt

print(solution(1,	3)) # 3
print(solution(437674,	3)) # 3
print(solution(110011,	10)) # 2
