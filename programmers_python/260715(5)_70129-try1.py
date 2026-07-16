'''
70129. 이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129

문제 분석: 2m 12s
코드 작성: 9m 19s
디버깅: 0m 0s
total: 11m 31s
'''

def solution(s):
    answer = [0, 0] # [변환 횟수, 0 제거 수]
    while s != "1":
        l = len(s)
        print(s)
        cnt_one = s.count("1")

        # 0 제거
        answer[0] += 1
        answer[1] += (l-cnt_one)

        # 2진수 변환
        s = str(bin(len("1"*cnt_one)))[2:]
    return answer

print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3]
print(solution("1111111")) # [4,1]
