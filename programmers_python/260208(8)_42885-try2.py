'''
42885. lv2 구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''



def solution(people, limit):
    people_sorted = sorted(people, reverse=True)
    answer = 0

    # 투포인터
    i, j = 0, len(people)-1
    
    while i<=j:
        if people_sorted[i] + people_sorted[j] <= limit:
            i+=1
            j-=1
        # 남은 인원 중 가장 무거운 사람 A와 가장 가벼운 사람 Z를 같이 태울 수 없다면, 
        # 어차피 A는 혼자 타야 한다.
        else: 
            i+=1

        answer+=1
    return answer


print()
print(solution([70, 50, 80, 50], 100))
print(3)

print()
print(solution([70, 80, 50], 100))
print(3)


# print()
# print(solution())
# print()