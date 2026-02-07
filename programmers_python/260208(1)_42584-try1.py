'''
42584. lv2 주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
37m 50s
'''

def solution(prices):
    N = len(prices)
    stack = []
    answer = [0]*(N)

    stack.append([0,prices[0]]) # [0:idx, 1:value]

    for i in range(1, N-1):
        # print()
        # print(i)
        if (stack) and (stack[-1][1] <= prices[i]):
            stack.append([i, prices[i]])
        else:
            while (stack) and (stack[-1][1] > prices[i]):
                idx, val = stack.pop()
                answer[idx] = i - idx
            stack.append([i, prices[i]])
        # print('answer', answer)
        # print('stack', stack)
    
    while stack:
        i, v = stack.pop()
        answer[i] = N-1-i

    return answer

print()
print(solution([1, 2, 3, 2, 3]))
print([4, 3, 1, 1, 0])

print()
print(solution([1,2,3,2,1,0,5]))
print([5,3,1,1,1,1,0])

# print()
# print(solution())
# print()