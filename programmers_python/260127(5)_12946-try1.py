'''
12946. lv2 하노이의 탑
https://school.programmers.co.kr/learn/courses/30/lessons/12946
'''

def solution(n):
    answer = []

    # n, from, via, to
    def game(n, f, v, t): 
        # global answer   

        if n==1:
            answer.append([f,t])
            return

        game(n-1, f, t, v)
        answer.append([f,t])
        game(n-1, v, f, t)
        
    game(n, 1, 2, 3)
        
    return answer

print()
print(solution(2))
# print([ [1,2], [1,3], [2,3] ])

print()
print(solution(3))
# print([ [1,2], [1,3], [2,3] ])

# print()
# print(solution())
# print()

# print()
# print(solution())
# print()