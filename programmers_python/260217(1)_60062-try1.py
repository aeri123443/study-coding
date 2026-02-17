'''
64064. Lv.3 불량 사용자
https://school.programmers.co.kr/learn/courses/30/lessons/64064
29m 35s
'''

'''
가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 
아이디 당 최소 하나 이상의 '*' 문자를 사용하였습니다.
알파벳 소문자와 숫자로만 구성
같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.
'''
import re
from itertools import product

def solution(user_id, banned_id):
    # U = len(user_id)
    B = len(banned_id)

    # 정규식 표현에 맞게 변환
    banned_id = [s.replace('*', '.') for s in banned_id]
    # print(banned_id)

    # 각 밴아이디에 따른 후보 리스트들 담기
    banned_list = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if re.search(rf"^{ban}$", user):
                tmp.append(user)
        if tmp:
            banned_list.append(tmp)
        else:
            return 0
    
    # print(banned_list)
    
    # 데카르트곱
    answer_set = set()
    for ban_user in product(*banned_list):

        # 겹치는 아이디가 있는 경우 넘어감
        if len(set(ban_user)) < B:
            continue

        # 정렬 후 튜플로 담음
        answer_set.add( tuple(sorted(ban_user))  )
    # print(answer_set)
    return len(answer_set)

print()
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(2)

print()
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(2)

print()
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
print(3)

print()
print(solution(["frodo", "frido", "fradi", "crodo", "crodoo", "abc123", "acc123", "frodoc"], ["fr*d*", "*rodo", "******", "a*c123", "******"]))
print()

# print()
# print(solution())
# print()
