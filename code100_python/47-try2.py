'''
p.488 47. 1부터 N까지 숫자 중 합이 10이 되는 조합 구하기
반복문 활용해보기
'''

def backtrack(start, N, sum, group, result):

    for i in range(start, N+1):
        new_sum = sum + i   
        if new_sum == 10:
            result.append([*group, i])      
        elif new_sum < 10:
            backtrack(i+1, N, new_sum, [*group, i], result)

def solution(N):    
    result = []
    backtrack(1, N, 0, [], result)
    return sorted(result)

print(solution(5))
print(solution(2))
print(solution(7))
