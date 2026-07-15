'''
17687. [3차] n진수 게임
https://school.programmers.co.kr/learn/courses/30/lessons/17687

문제 분석: 7m 6s
코드 작성: 33m 00s
디버깅: 0m 0s
total: 40m 06s
'''
MAPPING = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

# 10 -> n진수 변환
def number_conversion(num, base):
    if num == 0: return '0'

    result = []
    q = num
    while q > 0:
        q, r = divmod(q, base)
        if r < 10:
            result.append(r)
        else:
            result.append(MAPPING[r])

    return ''.join(map(str, result[::-1]))

def solution(n, t, m, p):
    # t*m 길이가 나올 때까지 이어붙이기
    max_len = t * m
    cur_len = 0
    nums = []
    i = 0
    while cur_len <= max_len:
        changed_num = number_conversion(i, n)

        nums.append(changed_num)
        cur_len += len(changed_num)
        i += 1

    # n자리 숫자만 골라 붙이기
    nums_to_str = ''.join(nums)
    # print(nums_to_str)
    answer = []
    for i in range(max_len):
        if i % m + 1 == p:
            answer.append(nums_to_str[i])
    return ''.join(answer[:t])

# 0111
print(solution(2,	4,	2,	1))
# 02468ACE11111111
print(solution(16,	16,	2,	1))
# 13579BDF01234567
print(solution(16,	16,	2,	2))
# print(solution())
