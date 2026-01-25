'''
12951. lv2 JadenCase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''

import sys
input = sys.stdin.readline
# print = sys.stdout.write

def solution(s):
    # print(ord('0')) # 48
    # print(ord('A')) # 65
    # print(ord('a')) # 97

    answer_arr =[]    
    for i in range(len(s)):
        if s[i]==' ':
            answer_arr.append(' ')

        # 단어의 첫글자인지?
        elif i==0 or s[i-1]==' ':
            # 첫글자가 소문자면 대문자로
            if 97<=ord(s[i])<123:
                answer_arr.append(s[i].upper())
            else:
                answer_arr.append(s[i])
        # 단어의 첫글자가 아니라면...
        else:
            # 소문자로 반환
            answer_arr.append(s[i].lower())

    # print(str_arr)
    return ''.join(answer_arr)

# "3people Unfollowed Me"
print(solution("3people unFollowed me"))

# "For The Last Week"
print(solution("for the last 5week"))

print(solution("Aa aA Zz zZ"))
print(solution(" Aa aA Zz zZ "))
print(solution("  Aa  aA  Zz  zZ "))
