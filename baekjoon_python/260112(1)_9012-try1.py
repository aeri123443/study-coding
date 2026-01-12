'''
9012. <실버4> 괄호
https://www.acmicpc.net/problem/9012
'''

import sys
input = sys.stdin.readline

def vps(txt):

    # 괄호가 홀수 개면 바로 NO 출력
    if len(txt)%2 != 0:
        return "NO"
    
    # 스택 쌓기
    stack = []
    for c in txt:
        if c=='(':
            stack.append(c)
        else:
            if len(stack)==0:
                return "NO"
            else:
                stack.pop()
        # print(c, stack)
    
    # 짝을 모두 찾았는지 확인
    if len(stack)==0:
        return "YES"
    else: 
        return "NO"

T = int(input())

for _ in range(T):
    # 개행문자 제거
    txt = input().strip()
    print(vps(txt))

