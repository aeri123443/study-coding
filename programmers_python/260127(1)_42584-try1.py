'''
42584. 주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
'''

def solution(prices):
    N = len(prices)
    answer = [0]*N
    stack = []

    # 단조 스택
    for i in range(N-1):
        cur_price, nxt_price = prices[i], prices[i+1]
        if cur_price <= nxt_price:
            stack.append(i)
        else:
            answer[i] = 1
            while stack:
                if prices[stack[-1]] > nxt_price:
                    pop_idx = stack.pop()
                    answer[pop_idx] = i+1-pop_idx
                else:
                    break
    # print(answer)

    # 아직 채워지지 않은 값 넣기
    for i, v in enumerate(answer):
        if v==0:
            answer[i] = N-1-i

    return answer

print()
print(solution([1, 2, 3, 2, 3]))
print([4, 3, 1, 1, 0])

print()
print(solution([1,5,4,9,3,8,7,1,2,6,8]))
print([10,1,2,1,3,1,1,3,2,1,0])

# 스택이 다 비어있을 때?
print()
print(solution([5,5,5,5,5]))
print([4,3,2,1,0])

# 최소 최대
print()
print([1,1])
print(solution([1,0]))

