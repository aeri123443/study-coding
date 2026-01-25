'''
64065. lv2 튜플
https://school.programmers.co.kr/learn/courses/30/lessons/64065
'''

# 중복된 원소 O
# 원소에 정해진 순서
# 원소의 순서가 다르면 서로 다른 튜플

import sys
input = sys.stdin.readline

def solution(s):

    # 입력값을 집합을 포함한 리스트로 변환
    # 집합 크기 기준으로 정렬
    arr = s.strip('{{').strip('}}').split('},{')
    n = len(arr)
    loop_arr = ['']*(n+1)
    answer_arr = []
    for i in range(n):
      arr[i] = set(map(int, arr[i].split(',')))
      loop_arr[len(arr[i])] = arr[i]
    # print(loop_arr)

    # 하나씩 제하기
    for i in range(n):
        if i == 0:
            # print(list(loop_arr[i+1])[0])
            answer_arr.append(list(loop_arr[i+1])[0])
        else:
            # print(i, loop_arr[i+1], loop_arr[i])
            # print( loop_arr[i+1] - loop_arr[i] )
            answer_arr.append(list(  loop_arr[i+1] - loop_arr[i]  )[0])
            
    return answer_arr

# [2, 1, 3, 4]
print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))
# [111, 20]
print(solution("{{20,111},{111}}"))
# [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# [123]
print(solution("{{123}}"))
# [3, 2, 4, 1]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
