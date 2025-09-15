'''
p.563 55. 정렬이 완료된 두 배열 합치기
소요시간: 13m 01s
'''

def solution(arr1, arr2):
    p1, p2 = 0,0
    
    answer = []
    while p1<len(arr1) and p2<len(arr2):
        if arr1[p1]<=arr2[p2]:
            answer.append(arr1[p1])
            if p1==len(arr1)-1:
                answer.extend(arr2[p2:])
                break
            p1 += 1
        else:
            answer.append(arr2[p2])
            if p2==len(arr2)-1:
                answer.extend(arr1[p1:])
                break
            p2 += 1

        
    return answer

print(solution([1,3,5], [2,4,6]))
print(solution([1,2,3], [4,5,6]))
print(solution([4,5,6], [1,2,3]))
print(solution([2,4,6], [1,3,5]))
print(solution([2,4,6,9,20], [1,3,5,6]))
print(solution([2,4,6,9,20], [1,3,5,7]))
print(solution([2,4,6,9,20], [1,3,5,21]))
print(solution([2,4,20,21,22,23], [1,19]))
print(solution([2,4,20], [1,19]))
print(solution([2,4,20], [1,21]))
