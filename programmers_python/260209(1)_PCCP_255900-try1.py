
'''
Lv. 1 [PCCP 모의고사 #1] 1번 - 외톨이 알파벳
https://school.programmers.co.kr/learn/courses/20847/lessons/255900
30m 59s
'''

from collections import Counter

#  2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 외톨이 문자열
def solution(input_string):
    n = len(input_string)
    s_counter = Counter(input_string)
    # print(s)

    # 순회하면서 연속으로 되어있는지 확인
    # 연속이 아니면 두 부분으로 나뉘어져 있다는 뜻!
    answer = set()
    cur_x = input_string[0]
    cur_cnt = 1
    for i in range(1, n):
        if cur_x==input_string[i]:
            cur_cnt += 1
        else:
            if cur_cnt != s_counter[cur_x] and s_counter[cur_x]>1:
                answer.add(cur_x)
            cur_x = input_string[i]
            cur_cnt = 1

    
    # 정렬 및 반환
    return ''.join(sorted(answer)) if answer else 'N'

print()
print(solution("edeaaabbccd"))
print("de")

print()
print(solution("eeddee"))
print("e")

print()
print(solution("string"))
print("N")

print()
print(solution("zbzbz"))
print("bz")

print()
print(solution("abbcac"))
print("ac")
