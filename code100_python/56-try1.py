'''
p.566 56. 문자열 내 마음대로 정렬하기 
https://school.programmers.co.kr/learn/courses/30/lessons/12915
소요시간: 5m 40s
'''

def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x:x[n])
    return strings

# ["car", "bed", "sun"]
print(solution(["sun", "bed", "car"], 1))
# ["abcd", "abce", "cdx"]
print(solution(["abce", "abcd", "cdx"], 2))