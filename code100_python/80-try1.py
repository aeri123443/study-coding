'''
p.699 80. 거스름돈 주기
소요시간: 9m 57s
'''

def division(n):
    global remain, answer
    answer.extend([n]*(remain//n))
    remain = remain%n

def solution(amount):
    global remain, answer
    remain = amount
    answer = []

    while remain>0:
        if remain >= 100: division(100)
        elif remain >= 50: division(50)
        elif remain >= 10: division(10)
        elif remain >= 1: division(1)
    return answer

# [100, 10, 10, 1, 1, 1]
print(solution(123))

# [100, 100, 100, 50]
print(solution(350))
