'''
9012. 괄호
https://www.acmicpc.net/problem/9012
'''

N = int(input())
arr = [input() for _ in range(N)]

for x in arr:
    stack = 0
    for y in x:
        if y == '(':
            stack += 1
        else:
            stack -= 1
            if stack<0:
                print('NO')
                break
    if stack==0:
        print("YES")
    elif stack>0:
        print("NO")
