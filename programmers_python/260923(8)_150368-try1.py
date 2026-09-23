'''
150368. 이모티콘 할인행사
https://school.programmers.co.kr/learn/courses/30/lessons/150368

문제 분석: 11m 48s
코드 1차 작성: 21m 52s
최종 디버깅: 0m 0s (바로 pass)

총 소요 시간: 33m 41s
'''
from itertools import product

INF = float('inf')

def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    answer = (-INF, -INF)

    for dc_case in product([10, 20, 30, 40], repeat=m):
        total_info = [0, 0] # 가입자 수, 판매액
        for u_dc, u_pr in users:
            u_price = 0
            for i, dc in enumerate(dc_case):
                if u_dc <= dc:
                    u_price += emoticons[i] * (1 - dc/100)
            if u_pr <= u_price:
                total_info[0] += 1
            else:
                total_info[1] += u_price
        answer = max(answer, (total_info[0], int(total_info[1])))

    return list(answer)

    return answer

# [1, 5400]
print(solution([[40, 10000], [25, 10000]],	[7000, 9000]))
# [4, 13860]
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],	[1300, 1500, 1600, 4900]))

