'''
p.561 54. 계수 정렬 구현하기
소요시간:
'''

def solution(s):
    alpabet = [0]*26
    for c in s:
        alpabet[ord(c)-97] += 1
    
    answer=""
    for i, v in enumerate(alpabet):
        if v>0:
            answer += chr(i+97)*v

    return answer

print(solution('hello'))
print(solution('algorithm'))