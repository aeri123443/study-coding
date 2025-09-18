'''
p.648 72. 조약돌 문제
걸리는 부분도 있다면 그것도 하나의 경우의 수로 과감하게 빼버릴 수 있는 능력이 필요
'''

def solution(arr):
    N = len(arr[0])
    answer_arr = [[0]*(N+1) for _ in range(4)]


    for i in range(1, N+1):
        answer_arr[0][i] = arr[0][i-1] + max(answer_arr[1][i-1], answer_arr[2][i-1])
        answer_arr[1][i] = arr[1][i-1] + max(answer_arr[0][i-1], answer_arr[2][i-1], answer_arr[3][i-1])
        answer_arr[2][i] = arr[2][i-1] + max(answer_arr[0][i-1], answer_arr[1][i-1])
        answer_arr[3][i] = arr[0][i-1] + arr[2][i-1] + answer_arr[1][i-1]
    
    return max([answer_arr[j][-1] for j in range(4)])

# 19
print(solution([[1, 3, 3, 2], [2, 1, 4, 1], [1, 5, 2, 3]]))
# 32
print(solution([[1, 7, 13, 2, 6], [2, -4, 2, 5, 4], [5, 3, 5, -3, 1]]))
