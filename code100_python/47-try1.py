'''
p.488 47. 1부터 N까지 숫자 중 합이 10이 되는 조합 구하기
소요시간: 20m 53s
'''

def dfs(i, N, sum, group, result):
    if i<=N:
        # print(i, group)

        # i를 선택하지 않았을 때
        dfs(i+1, N, sum, group, result)

        # i를 선택했을 때
        sum = sum + i
        new_group = [*group, i]
        # 10 되면 멈춤
        if sum == 10:
            # print("!! 10 !! ", new_group)
            result.append(new_group)
        # 10보다 작을 때
        elif sum < 10:
            dfs(i+1, N, sum, new_group, result)
        
def solution(N):    
    result = []
    dfs(1, N, 0, [], result)
    return sorted(result)

print(solution(5))
print(solution(2))
print(solution(7))
