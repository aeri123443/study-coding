'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
소요시간: 97m 14s
'''

def solution(q, r, code):
    answer = ''
    n = len(code)
    for idx in range(n):
        if idx%q==r:
            answer += code[idx]

    return answer


# jerry
print(solution(3, 1, "qjnwezgrpirldywt"))
      
# programmers
print(solution(1, 0, "programmers"))