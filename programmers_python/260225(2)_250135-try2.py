'''
250135. lv.2 [PCCP 기출문제] 3번 / 충돌위험 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/250135

'''

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 초 단위로 변환
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    # 각 바늘의 현재 각도 계산 함수 (12시간 기준 360도)
    def get_angles(total_sec):
        # 시침: 12시간(43200초)에 360도 -> 1초에 1/120도
        h_angle = (total_sec % 43200) * 360 / 43200
        # 분침: 1시간(3600초)에 360도 -> 1초에 1/10도
        m_angle = (total_sec % 3600) * 360 / 3600
        # 초침: 1분(60초)에 360도 -> 1초에 6도
        s_angle = (total_sec % 60) * 360 / 60
        return h_angle, m_angle, s_angle

    # 시작 시점에 이미 겹쳐있는지 확인
    h_a, m_a, s_a = get_angles(start)
    if s_a == h_a or s_a == m_a:
        answer += 1

    # 1초씩 진행하며 확인
    for t in range(start, end):
        curr_h, curr_m, curr_s = get_angles(t)
        next_h, next_m, next_s = get_angles(t + 1)
        
        # '0도'로 되돌아가는 경우를 위해 360도로 보정
        if next_h == 0: next_h = 360
        if next_m == 0: next_m = 360
        if next_s == 0: next_s = 360
        
        # 초침이 시침을 추월했는지 확인
        h_over = curr_s < curr_h and next_s >= next_h
        # 초침이 분침을 추월했는지 확인
        m_over = curr_s < curr_m and next_s >= next_m
        
        if h_over and m_over:
            # 시침과 분침이 동시에 겹치는 경우 (예: 12시 정각)
            if next_h == next_m:
                answer += 1
            else:
                answer += 2
        elif h_over or m_over:
            answer += 1
            
    return answer

print()
print(solution(0, 5, 30, 0, 7, 0))
print(2)

print()
print(solution(12, 0, 0, 12, 0, 30))
print(1)

print()
print(solution(0, 6, 1, 0, 6, 6))
print(0)

print()
print(solution(11, 59, 30, 12, 0, 0))
print(1)

print()
print(solution(11, 58, 59, 11, 59, 0))
print(1)

print()
print(solution(1, 5, 5, 1, 5, 6))
print(2)

print()
print(solution(0, 0, 0, 23, 59, 59))
print(2852)

# print()
# print(solution())
# print()