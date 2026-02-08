
'''
42747. lv2 H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    citations.sort(reverse=True)

    for i,v in enumerate(citations):
        if i+1 > v:
            return i
    return len(citations)

print()
print(solution([3, 0, 6, 1, 5]))
print(3)

print()
print(solution([6,5,4,1,0]))
print(3)

print()
print(solution([0,3,6,7,8,9]))
print(4)


print()
print(solution([5,5,5,5]))
print(4)