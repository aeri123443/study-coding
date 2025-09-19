'''
p.667 77. 도둑질
https://school.programmers.co.kr/learn/courses/30/lessons/42897
소요시간: 25m 38s
'''

def solution(money):
    N = len(money)
    # 첫 원소를 선택했을때/그러지 않았을 때를 구분
    T = [0]*N
    T[0] = money[0]
    T[1] = money[1]
    T[2] = money[0] + money[2]
    F = [0]*N
    F[1] = money[1]
    F[2] = money[2]
    
    for i in range(3, N):
        if i == N-1:
            F[i] = max(F[i-3], F[i-2]) + money[i]
        else:
            T[i] = max(T[i-3], T[i-2]) + money[i]
            F[i] = max(F[i-3], F[i-2]) + money[i]
    # print()
    return max(T[N-3:]+F[N-3:])

# 4
print(solution([1, 2, 3, 1]))
# 111
print(solution([5,0,0,100,0,6,0]))
# 111
print(solution([5,0,0,0,100,0,0,6,0]))
# 109
print(solution([5,1,0,100,0,0,8]))
