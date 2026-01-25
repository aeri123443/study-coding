'''
60058. lv2 괄호 변환
https://school.programmers.co.kr/learn/courses/30/lessons/60058
'''

import sys
input = sys.stdin.readline

def solution(p):
    # arr = list(p)
    n = len(p)
    # print(n)

    # 균형잡힌 괄호 문자열(u)의 끝 인덱스 반환
    def get_u_idx(si):
        check = [0,0]
        for i in range(si, n):
            if p[i]=='(':
                check[0] += 1
            else:
                check[1] += 1
            if check[0] == check[1]:
                return i+1 # 끝나는 인덱스+1!!

    # 올바른 문자열 확인
    def is_correct(si, ei):
        # print(si, ei)
        # print(p[si:ei])
        stack_cnt = 0
        for s in p[si:ei]:
            if s == '(':
                stack_cnt += 1
            else:
                if stack_cnt==0:
                    return False
                stack_cnt -= 1

        return True if stack_cnt==0 else False
    
    # 재귀 시!작~
    def recur(si, ei):
        # print()
        # print(si, ei)
        # u찾기
        u_ei = get_u_idx(si)
        # print('u', p[si:u_ei])
        # print('v', p[u_ei:ei])

        # u가 올바른 괄호열인지?
        if is_correct(si, u_ei):
            # print('u is correct')
            # v에 대해 다시 재귀 수행
            if u_ei == ei:
                result = ''
            else:
                result = recur(u_ei, ei)
            # print('result', result)
            # print(p[si:u_ei], result)
            return ''.join([p[si:u_ei], result])
        else:
            # print('u is not correct')
            tmp = []
            tmp.append('(')
            # v에 대해 다시 재귀 수행
            if u_ei == ei:
                result = ''
            else:
                result = recur(u_ei, ei)
            # print('result', result)
            tmp.append(result)
            tmp.append(')')
            # u의 첫 번째와 마지막 문자를 제거하고, 
            # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            for i in range(si+1, u_ei-1):
                if p[i] == '(':
                    tmp.append(')')
                else:
                    tmp.append('(')
            return ''.join(tmp)
    
    # ei = get_u_idx(0)
    # print(ei)
    return recur(0, n)
    # return is_correct(0, ei)

print(solution("(()())()"))
print("(()())()")

print(solution(")("))
print("()")

print(solution("()))((()"))
print('()(())()')

