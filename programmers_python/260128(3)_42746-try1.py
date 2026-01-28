

def solution(record):
    hash_map = {}
    answer = []
    for r in record:
        cmd = r.split()

        # Enter & Change
        if cmd[0]=='Enter' or cmd[0]=="Change":
            hash_map[cmd[1]] = cmd[2]

        # Enter & Leave
        if cmd[0]=='Enter':
            answer.append([cmd[1], '님이 들어왔습니다.'])
        elif cmd[0]=='Leave':
            answer.append([cmd[1], '님이 나갔습니다.'])

    return [ f'{hash_map[a]}{b}' for a,b in answer]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
print(["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])
