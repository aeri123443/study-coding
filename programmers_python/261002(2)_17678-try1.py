'''
17678. 셔틀버스
https://school.programmers.co.kr/learn/courses/30/lessons/17678

문제 분석: 15m 49s
1차 코드 작성: 49m 10s
    - TC fail: 클로드 도움, 필요한 것은 마지막 버스이니 last_info 업데이트
2차 코드 작성: 6m 53s

총 소요 시간: 1h 11m 53s
'''
def update_time(h, m):
    dh = m // 60
    return h+dh, m - (dh*60)

def solution(n, t, m, timetable):
    # 버스 도착 시간 리스트
    bus_time = []
    bh, bm = 9, 0
    for _ in range(n):
        bus_time.append((bh, bm))
        bh, bm = update_time(bh, bm+t)

    lh, lm = bus_time[-1]

    cru_table = []
    for tt in timetable:
        th, tm = map(int, tt.split(':'))
        if (th, tm) > (lh, lm): continue
        cru_table.append((th,tm))
    cru_table.sort()

    # 버스 도착 시간에 따라, 크루 배치, 마지막 차를 몇 명이 타는지 체크
    c_idx = 0 # 크루 인덱스
    last_info = [(9,0),0,(9,0)] # 마지막 버스: 시간, 몇 명이 타는지, 가장 늦는 크루(시간)
    for bh, bm in bus_time:
        info = [(bh, bm), 0, (-1,-1)]
        while info[1] < m and c_idx < len(cru_table):
            ch, cm = cru_table[c_idx]
            if (bh, bm) >= (ch, cm):
                c_idx += 1
                info[1] += 1
                info[2] = (ch,cm)
            else:
                break
        last_info = info

    # 마지막 차가 차지 않았으면, 마지막 버스 시간에 도착
    if last_info[1] < m:
        ah, am = lh, lm
    # 마지막 차가 모두 찼으면, 최대 시간 -1에 도착
    else:
        ah, am = last_info[2]
        ah, am = update_time(ah, am-1)

    ah = str(ah) if ah >= 10 else '0'+str(ah)
    am = str(am) if am >= 10 else '0'+str(am)

    return ah + ':' + am

print(solution(5,	5,	2,	["09:00", "09:00", "09:06", "09:11"]))

# 09:00
print(solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"]))

# 09:09
print(solution(2,	10,	2,	["09:10", "09:09", "08:00"]))

# 08:59
print(solution(2,	1,	2,	["09:00", "09:00", "09:00", "09:00"]))

# 00:00
print(solution(1,	1,	5,	["00:01", "00:01", "00:01", "00:01", "00:01"]))

# 09:00
print(solution(1,	1,	1,	["23:59"]))

# 18:00
print(solution(10,	60,	45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

# 09:04
print(solution(3,	3,	2,	["09:00", "09:02", "09:03", "09:03", "09:05"]))
