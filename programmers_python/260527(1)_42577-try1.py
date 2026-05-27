'''
42577. 전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577

16m 08s
'''

def solution(phone_book):
    phone_set = set(phone_book)

    for p_number in phone_book:
        p_number_list = list(p_number)
        p_number_len = len(p_number_list)

        for i in range(p_number_len):
            target = ''.join(p_number_list[:i+1])
            if target != p_number and ''.join(p_number_list[:i+1]) in phone_set:
                # print(p_number, target)
                return False

    return True

# false
# print(solution(["119", "97674223", "1195524421"]))
#
# # true
# print(solution(["123","456","789"]))
#
# # false
# print(solution(["12","123","1235","567","88"]))

# true
print(solution(["119", "97674223", "5521195524421"]))
