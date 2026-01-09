'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
소요시간: 97m 14s
'''

# 소수 dp
dp = {1:False, 2:True}

# 진수 변환
def change_base(n, base):
    result = []
    while n>0:
        n, mod = divmod(n, base)
        result.append(str(mod))
    return ''.join(reversed(result))

# 소수 판별
def is_prime(k):
    global dp

    # 2는 소수임
    if k==2: return True

    # 이미 검사해본 소수 목록인지?
    if k in dp:
        return dp[k]
    
    # 1, 짝수는 소수가 아님
    if k==1 or k%2==0:  
        dp[k] = False
        return False
    

    # 2부터 뤁k까지 나눠봄
    for i in range(2, int(k**0.5) + 1):
        if k%i==0:
            dp[k] = False
            return False
        
    # 다 나눠지면 소수임!
    dp[k] = True
    return True

# 메인
def solution(n, k):

    # 진수 변환
    new_num = change_base(n, k)
    # 0 기준으로 글자 자르기
    arr = new_num.split('0')
    # print(arr)

    answer = 0
    for x in arr:
        if not x: continue 
        # 10진수로 변환
        tmp_dec = int(x)
        # 소수면 정답 카운트
        if is_prime(tmp_dec):
            # print(tmp_dec)
            answer+=1
    return answer


# 3
print(solution(437674, 3))

# 2
print(solution(110011, 10))
     
     