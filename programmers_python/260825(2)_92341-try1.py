'''
92341. 주차 요금 계산
https://school.programmers.co.kr/learn/courses/30/lessons/92341

문제 분석: 6m 55s
코드 작성: 25m 41s
최종 디버깅: 0m 0s

총 소요 시간: 31m 39s
'''
import math

MAX_TIME = 23*60 + 59
def solution(fees, records):
    car_info = {} # 차량 번호: [누적 시간, 마지막 in 시간]

    for rec in records:
        t, num, status = rec.split()

        h, m = map(int, t.split(':'))

        new_min = h*60 + m
        
        if status == 'IN':
            if num in car_info:
                car_info[num][1] = new_min
            else:
                car_info[num] = [0, new_min, -1]
        else: # OUT
            car_info[num][2] = new_min
            car_info[num][0] += (new_min - car_info[num][1])


    ans = []
    for num, (m, i, o) in car_info.items():

        # IN > OUT일 경우 아직 출차되지 않음, 23:59 기준으로 업데이트
        if i >= o:
            total_time = m + (MAX_TIME-i)
        else:
            total_time = m

        price = fees[1] + max(0, math.ceil((total_time-fees[0])/fees[2]))*fees[3]
        ans.append((num, price))

    ans.sort()

    return [x[1] for x in ans]

# [14600, 34400, 5000]
print(solution([180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [0, 591]
print(solution([120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# [14841]
print(solution([1, 461, 1, 10],	["00:00 1234 IN"]))
