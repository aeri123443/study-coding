'''
43165. lv2 타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''

def solution(numbers, target):
    n = len(numbers)

    answer = 0

    def recur(idx, total): 
        nonlocal answer

        if idx == n:
            if total==target: 
                answer += 1
            return
        
        recur(idx+1, total+numbers[idx])
        recur(idx+1, total-numbers[idx])

    recur(0, 0)

    return answer

print()
print(solution([1, 1, 1, 1, 1], 3))
print(5)

print()
print(solution([4, 1, 2, 1], 4))
print(2)

# print()
# print(solution())
# print()
