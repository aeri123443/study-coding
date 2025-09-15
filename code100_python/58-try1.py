'''
p.569 58. K번째수
https://school.programmers.co.kr/learn/courses/30/lessons/42748
소요시간: 6m 13s
'''

def solution(array, commands):
    answer = []

    for cmd in commands:
        tmp_arr = array[cmd[0]-1:cmd[1]]
        answer.append( sorted(tmp_arr)[cmd[2]-1])    

    return answer

# [5, 6, 3]
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
print(solution([1, 5, 2, 6, 3, 7, 4], [[3, 3, 1]]))
