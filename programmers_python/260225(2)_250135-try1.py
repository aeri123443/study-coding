'''
250135. lv.2 [PCCP 기출문제] 3번 / 충돌위험 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/250135
'''
# print(24*3600)
# print(23*120, 59*2)

# deg/sec
S_DS = 360 / 60
M_DS = 360 / 60 / 60
H_DS = 360 / 12 / 60 / 60

# 초 - 시/분 상대속도
S_H_RV = S_DS - H_DS
S_M_RV = S_DS - M_DS

# 시침, 분침은 각각 초침과 몇 초에 한 번씩 겹치는가?
H_GAP = 360 / S_H_RV
M_GAP = 360 / S_M_RV

# print(H_GAP, M_GAP)

def solution(h1, m1, s1, h2, m2, s2):

    # 00:00:00 ~ h:m:s 몇 번 겹치는지 계산
    def cal_cnt(sec):

        # 시침, 분침 겹치는 횟수 sec//H_GAP, sec//M_GAP
        cnt = 0
        cnt += sec//H_GAP
        cnt += sec//M_GAP

        # 00:00:00, 12:00:00에서 한 번씩 뺌
        return cnt

    sec_start = 3600 * h1 + 60 * m1 + s1
    sec_end = 3600 * h2 + 60 * m2 + s2
    return int(cal_cnt(sec_end) - cal_cnt(sec_start-1))

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