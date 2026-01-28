'''
82612#. lv1 부족한 금액 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/82612
'''

def solution(price, money, count):
    
    if count%2==0:
        sum_num = (1+count)*(count//2)
    else:
        sum_num = (1+count)*(count//2)+(count+1)//2

    result = price*sum_num

    return max(result-money, 0)

# print(solution(3, 20, 4))
# print(solution(3, 30, 4))
# print(solution(3, 40, 4))
print(solution(2500, 1000000000, 2500))
