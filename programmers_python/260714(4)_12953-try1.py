'''
12953. N개의 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953
'''

# 두 수의 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 두 수의 최소공배수
def lcm(a, b):
    return (a*b) // gcd(a,b)

# lcm
def solution(arr):
    if len(arr) == 1:
        return arr[0]

    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)

    return answer
# 168
print(solution([2,6,8,14]))
# 6
print(solution([1,2,3]))
