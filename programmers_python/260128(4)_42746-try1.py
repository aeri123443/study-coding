
'''
시침: 360/24h
분침: 360/60m
초침: 360/60s
0시 = 0분 = 0초
1시 = 5분 = 5초
'''


def solution(h1, m1, s1, h2, m2, s2):

    # 1초에 몇도씩 증가하는가?
    # 0.004166666666666667 0.1 6.0
    # for_h = 360 / (24*60*60)
    # for_m = 360 / (60*60)
    # for_s = 360 / (60)
    for_h = 0.004166666666666667
    for_m = 0.1
    for_s = 6.0
    # print(for_h, for_m, for_s)

    # print((24*60*60))
    # print((60*60))
    # print((60))

    # 현재 시/분/초침 각도 계산
    h = h1 * for_h
    m = m1 * for_m
    s = s1 * for_s
    # print(h, m, s)

    # 현재 시간
    ch, cm, cs = h1, m1, s1

    answer = 0

    # 현재 각도가 일치하나?
    if h==s or m==s:
        answer += 1

    # 그 시간의 시침분침도 확인해야함
    # 1초씩 증가
    # 0~360도 중 어느 위치에 있는지

    flag_sh = h > s
    flag_sm = m > s
    while True:

        # 현재 시간 업데이트
        if cs >= 59: 
            cs -= 59
            cm += 1
        else: 
            cs += 1
        if cm >= 60: 
            cm -= 59
            ch += 1

        if [ch, cm, cs] >= [h2, m2, s2]:
            break
        
        print(f'{ch}h {cm}m {cs}s', end=' ')
        
        # 각 시분초침 위치 업데이트

        h += for_h
        m += for_m
        s += for_s

        if h >= 360: h -= 360
        if m >= 360: m -= 360
        if s >= 360: s -= 360

        print(h, m, s)
        
        # 각도 추월하는 순간 비교
        # flag_sh = h > s
        # flag_sm = m > s
        flag_reverse = False
        if  (h > s) != (flag_sh)  :
            flag_sh = h > s
            flag_reverse = True
        if (m > s) != (flag_sm) :
            flag_sm = m > s
            flag_reverse = True
        
        if flag_reverse:
            print('here')
            answer += 1

    return answer


# print()
# print(solution(0, 5, 30, 0, 7, 0))
# print(2)

print()
print(solution(12, 0, 0, 12, 0, 30))
print(1)

# print()
# print(solution(0, 6, 1, 0, 6, 6))
# print(0)

# print()
# print(solution(11, 59, 30, 12, 0, 0))
# print(1)

# print()
# print(solution(11, 58, 59, 11, 59, 0))
# print(1)

# print()
# print(solution(1, 5, 5, 1, 5, 6))
# print(2)

# print()
# print(solution(0, 0, 0, 23, 59, 59))
# print()

