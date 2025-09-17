'''
p.602 65. 이진 변환
https://school.programmers.co.kr/learn/courses/30/lessons/70129
소요시간: 20m 05s
'''
import time

def to_binary(n):
    result = ""
    while n > 1:
        result = str(n%2) + result
        n = n//2
    return "1" + result

def solution(s):
    ans1 = 0 # 0 제거 횟수
    ans2 = 0 # 진행 횟수

    while len(s)>1:
        # time.sleep(0.4)
        # print(s)
        ans2 += 1
        # 0 제거, 제거 수 카운트
        temp = ""
        for c in s:
            if c=='1':
                temp = temp + '1'
            else:
                ans1 += 1
        # print(temp)
        # 문자열 길이 반환
        # 이진수로 변환
        s = to_binary(len(temp))
        # print(s)
        # print()

    return [ans2, ans1]

# [3,8]
print(solution("110010101001"))
# [3,3]
print(solution("01110"))
# [4,1]
print(solution("1111111"))

'''
110010101001 -> 111111 /6 -> 110
110 -> 11 -> 10
10 -> 1 


'''