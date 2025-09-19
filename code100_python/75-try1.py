'''
p.658 75. 정수 삼각형
https://school.programmers.co.kr/learn/courses/30/lessons/43105
소요시간: 25m 29s
'''

def solution(triangle):
    N = len(triangle)
    arr = [[triangle[0][0]]]

    for i in range(N-1):
        tmp = [0]*(i+2)
        for j in range(i+1):
            tmp[j] = max(tmp[j], arr[i][j]+triangle[i+1][j])
            tmp[j+1] = max(tmp[j+1], arr[i][j]+triangle[i+1][j+1])
        # print(tmp)
        arr.append(tmp)

    # print(arr)
    return max(arr[-1])

# 30
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
# print(solution(999))
