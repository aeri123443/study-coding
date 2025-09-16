'''
p.595 63. 두 행렬을 곱한 후 전치 행렬 만들기
소요시간: 10m 35s
'''
import pprint

def solution(m1, m2):
    answer = [[0]*3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            tmp = 0
            for k in range(3):
                tmp += m2[k][i]*m1[j][k]
            # print(tmp)
            answer[i][j] = tmp

    return answer
pprint.pprint(solution([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ], [ [9, 8, 7], [6, 5, 4], [3, 2, 1] ]))
pprint.pprint(solution([ [2, 4, 6], [1, 3, 5], [7, 8, 9] ], [ [9, 1, 2], [4, 5, 6], [7, 3, 8] ]))
