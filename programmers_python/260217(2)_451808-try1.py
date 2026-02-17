'''
451808. Lv.3 숫자 야구
https://school.programmers.co.kr/learn/courses/30/lessons/451808
나중에 다시 풀어보자...
'''
from itertools import permutations

PASSWORD = [5,4,2,9]

# 임시 함수, 제출시 제외
def submit(num):
    s = list(map(int, list(str(num))))
    ball = 0
    strike = 0

    for idx, c in enumerate(s):
        if c in PASSWORD:
            if s[idx] == PASSWORD[idx]:
                strike += 1
            else:
                ball += 1
    
    return f"{strike}S {ball}B"

# 후보 숫자들
ALL = [int(''.join(arr)) for arr in permutations(['1','2','3','4','5','6','7','8','9'], 4)]

def score(num, pw):
    pw = list(map(int, list(str(pw))))
    s = list(map(int, list(str(num))))
    ball = 0
    strike = 0

    for idx, c in enumerate(s):
        if c in pw:
            if s[idx] == pw[idx]:
                strike += 1
            else:
                ball += 1
    
    return f"{strike}S {ball}B"

def solution(n, submit):
    # global number_list

    number_list = ALL[:]

    while number_list:
        n -= 1

        # 숫자 하나 뽑기
    
        best_num = number_list[0]
        worst_cnt = float('inf')

        if len(number_list) < 2000:
            for target in number_list:
                case_counter = {}
                for nu in number_list:
                    case_counter_key = score(nu, target)
                    if case_counter_key not in case_counter:
                        case_counter[case_counter_key] = 0
                    case_counter[case_counter_key] += 1
                worst_case = max(case_counter.values())
                if worst_cnt > worst_case:
                    best_num = target
                    worst_cnt = worst_case


        result = submit(best_num)

        if result=="4S 0B": 
            print('founded!!', n)
            return best_num

        # 해당 결과를 만족하지 않는 숫자 후보들로 줄이기
        new_list = []
        for num in number_list:
            if num==best_num: continue # 자기 자신은 후보에서 뺌
            if score(best_num, num)==result:
                new_list.append(num)
        number_list = new_list

        # print(len(number_list))

    return 0


print(solution(6, submit))

