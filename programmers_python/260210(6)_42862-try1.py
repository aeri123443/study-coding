'''
42862. Lv.1 체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862
31m 34s
'''

'''
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''

def solution(n, lost, reserve):
    lost = set(lost)
    reserve.sort()
    # 수업에 참가할 수 있는 학생들 표시 (양옆 패딩, 최종 계산 시 2 빼기)
    answer = [1]*(n+2)
    for l in lost:
        answer[l] = 0

    # 여벌을 가져온 학생 중 도난당한 사람은 체육복을 빌려줄 수 없음
    for r in reserve:
        if r in lost:
            answer[r] = 1
        # 그 외의 경우, 왼쪽 먼저 보고 오른쪽 봄
        elif answer[r-1] == 0:
            answer[r-1] = 1
        elif answer[r+1] == 0:
            answer[r+1] = 1

    return sum(answer)-2

print()
print(solution(5, [2, 4], [1, 3, 5]))
print(5)

print()
print(solution(5, [2, 4], [3]))
print(4)

print()
print(solution(3, [3], [1]))
print(2)

print()
print(solution(10, [3, 4], [4,5]))
print(9)

print()
print(solution(2, [1], [1]))
print(2)

print()
print(solution(3, [1], [3]))
print(2)

print()
print(solution(3, [1], [2]))
print(3)

# print(solution())
# print()