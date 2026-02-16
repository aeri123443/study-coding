'''
42895. Lv.3 N으로 표현
https://school.programmers.co.kr/learn/courses/30/lessons/42895
'''
from pprint import pprint

def solution(N, number):
    dp = [set() for _ in range(9)] #8+1
    dp[0] = {0}
    dp[1] = {N}

    if N == number: return 1

    # i개의 N으로 만들 수 있는 결과값 조합
    for i in range(2, 9):
        if int(str(N)*i) == number:
            return i
        dp[i].add(int(str(N)*i))

        # dp[i]는 dp[j]와 dp[i-j]의 연산으로 만들 수 있다 (j < i) 
        for j in range(1, i):
            
            set_a, set_b = dp[j], dp[i-j]
            for a in set_a:
                for b in set_b:
                    # 타겟 넘버가 나온다면 바로 반환
                    if a+b==number or a-b==number or a*b==number:
                        return i
                    if b!=0 and a//b==number:
                        return i
                    
                    dp[i].add( a+b )
                    dp[i].add( a-b )
                    if b>0: dp[i].add( a//b )
                    dp[i].add( a*b )
           
    # print(dp[4])
    return -1

print()
print(solution(5, 12))
print(4)

print()
print(solution(2, 11))
print(3)


print()
print(solution(1, 1))
print(1)

print()
print(solution(9, 9))
print(1)

# print()
# print(solution())
# print()