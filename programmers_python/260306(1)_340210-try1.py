'''
340210. lv.3 [PCCP 기출문제] 4번 / 수식 복원하기
https://school.programmers.co.kr/learn/courses/30/lessons/340210
59m 13s
'''

'''
2 ~ 9진법 중 하나
A, B는 음이 아닌 두 자릿수 이하의 정수
C는 알파벳 X 혹은 음이 아닌 세 자릿수 이하의 정수
'''

# 진법 변환 (n->10 10->n)

# 10진수 -> n진수 
def tenToN(num, n):
    if num==0: return '0'

    result = []
    
    while num > 0:
        num, md = divmod(num, n)
        # print(num, md)
        result.append(md)
        
    return ''.join(map(str, result[::-1]))
    
def solution(expressions):
    # expressions 전체 훑으면서 X가 아닌 수식에 대해 가능한 진법 담고
    
    # 후보 진법들
    tmp_set = {i for i in range(2,10)}
    
    for exp in expressions:
            
        exp_list = exp.split()
        
        # 1~9진법 탐색
        for n in range(2, 10):
            if n not in tmp_set:
                continue
                
            # print(exp_list[0], n)
            # print(int('14', 2))
            try:
                a = int(exp_list[0], n)
                b = int(exp_list[2], n)
                # 마지막이 X면 계산을 진행하지 않음
                if exp_list[4] == 'X':
                    continue
                c = int(exp_list[4], n)
                cal = exp_list[1]
                
                # n진법에서 수식이 일치하는지 확인
                # 일치하지 않으면 tmp_set에서 뺌
                if cal == '+':
                    if a+b != c:
                        tmp_set.remove(n)
                else: # '-'
                    if a - b != c:
                        tmp_set.remove(n)
            except ValueError:
                tmp_set.remove(n)
            
    # print(tmp_set)       
            
    # 각 expressions에 따라 X 또는 특정값 반환
    answer = []
    for exp in expressions:
        if exp[-1] != 'X': continue
        
        exp_list = exp.split()
        tmp = set()

        for n in tmp_set:
            # n진수를 10진수로 변환
            a = int(exp_list[0], n)
            b = int(exp_list[2], n)
            cal = exp_list[1]
            
            # 계산 결과를 n진수로 변환
            if cal=='+': 
                c = tenToN(int(a+b), n)
            elif cal=='-':
                c = tenToN(int(a-b), n)
            tmp.add(c)
            if len(tmp) > 1 : break
        # print(tmp)
        
        if len(tmp) == 1:
            answer.append( f"{exp_list[0]} {exp_list[1]} {exp_list[2]} = {c}"  )
        else:
            answer.append( f"{exp_list[0]} {exp_list[1]} {exp_list[2]} = ?" )
    return answer