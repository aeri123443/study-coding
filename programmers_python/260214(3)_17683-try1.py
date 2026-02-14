'''
17683. Lv. 2 [3차] 방금그곡
https://school.programmers.co.kr/learn/courses/30/lessons/17683
55m
'''

def string_to_list(s):
    arr = []
    for c in s:
        if c=='#':
            arr[-1] = arr[-1]+c
        else:
            arr.append(c)
    return arr

def solution(m, musicinfos):
    answer = None # 곡 제목, 라디오 재생 시간
    m = string_to_list(m)
    lm = len(m)

    for music in musicinfos:
        s_time, e_time, name, mel = music.split(',')
        (sh, sm), (eh, em) = map(int, s_time.split(':')), map(int, e_time.split(':'))

        # 재생시간 계산
        play_time = (eh-sh)*60 + em-sm

        # mel 문자열 재구성
        mel = string_to_list(mel)
        lmel = len(mel)
        if lmel < play_time:
            mel = mel*(play_time//lmel) + mel[:play_time%lmel]
        else:
            mel = mel[:play_time]
        
        lmel = len(mel)
        # print(mel)

        # 노래 일치 확인
        is_same = False
        for i in range(lmel-lm+1):
            if m[0] == mel[i]:
                if m == mel[i:i+lm]:
                    is_same = True
                    break

        if is_same:
            # print(name)
            if answer == None:
                answer = [name, play_time]
            # 재생 시간이 더 길면 교체
            elif answer[1] < play_time:
                answer = [name, play_time]

        
    return answer[0] if answer else "(None)"

print()
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print("HELLO")

print()
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print("FOO")

print()
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print("WORLD")

# print()
# print(solution())
# print()

# 다음날 00:00 포함인지 홛인
