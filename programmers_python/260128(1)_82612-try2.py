'''
82612#. lv1 부족한 금액 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/82612
문제 생기신다던 코드로 돌려봄
'''

def solution(price, money, count):
    
    total = price * count * (count + 1) // 2
    diff = total - money

    return diff if total-money > 0 else 0

# print(solution(3, 20, 4))
# print(solution(3, 30, 4))
# print(solution(3, 40, 4))
print(solution(2500, 1000000000, 2500))