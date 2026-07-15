'''
42888. 오픈채팅방
https://school.programmers.co.kr/learn/courses/30/lessons/42888

문제 분석: 2m 32s
코드 작성: 9m 34s
디버깅: 0m 0s
total: 12m 06s
'''

def solution(record):
    id_to_name = {}
    answer = []

    for cmd in record:
        cmd_split = cmd.split(' ')

        if cmd_split[0] == "Enter":
            id_to_name[cmd_split[1]] = cmd_split[2]
            answer.append([cmd_split[1], "님이 들어왔습니다."])
        elif cmd_split[0] == "Leave":
            answer.append([cmd_split[1], "님이 나갔습니다."])
        else: # Change
            id_to_name[cmd_split[1]] = cmd_split[2]

    for i, (uid, txt) in enumerate(answer):
        answer[i] = ''.join([id_to_name[uid], txt])

    return answer

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))