'''
42888. lv2 오픈채팅방
https://school.programmers.co.kr/learn/courses/30/lessons/42888
'''

# 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 채팅방에서 닉네임을 변경한다.
# 채팅방은 중복 닉네임을 허용
# 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
# 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.

import sys
input = sys.stdin.readline

def solution(record):
    map = {}
    answer_list = []

    for line in record:
        cmd = line.split()

        if cmd[0]=='Enter':
            map[ cmd[1] ] = cmd[2]
            answer_list.append([cmd[1], '님이 들어왔습니다.'])
        elif cmd[0]=='Leave':
            answer_list.append([cmd[1], '님이 나갔습니다.'])
        elif cmd[0]=='Change':
            map[ cmd[1] ] = cmd[2]

    # 문자열 결합
    for i in range(len(answer_list)):
        uid, msg = answer_list[i]
        answer_list[i] = ''.join([map[uid], msg])
    return answer_list


# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
