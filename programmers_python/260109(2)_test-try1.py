'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
소요시간: 97m 14s
'''

def solution(n, lost, reserve):
    lost
    reserve.sort()
    lost = set(lost)
    reserve = set(reserve)

    arr = [1]*n

    # 로스트 체크
    for x in lost:
        arr[x-1] = 0

    # 내가 도난당한 경우 체크
    trash = set()
    for x in reserve:
        if arr[x-1] == 0:
            arr[x-1] = 1
            trash.add(x)
    reserve = reserve - trash

    # 여벌 순환
    for x in reserve:
        i = x-1
        # 내가 도난당했으면 내가 가져감
        # if arr[i] == 0:
        #     arr[i] = 1
        # 왼쪽 애 없으면 왼쪽 애 줌
        if i>0 and arr[i-1]==0:
            arr[i-1]=1
        # 오른쪽 애 없으면 오른쪽 애 줌
        elif i<n-1 and arr[i+1]==0:
            arr[i+1]=1
    # print(arr)      
    return arr.count(1)


# 5
print(solution(5, [2, 4], [1, 3, 5]))
      
# 4
print(solution(5, [2, 4], [3]))

# 5
print(solution(8, [3,4,6,7], [5]))

# 8
print(solution(8, [3,5], [4,6]))

# 7
print(solution(8, [3,5,4], [4,6]))

# 8
print(solution(8, [2,7], [1,8]))

# 4
print(solution(5, [2,3], [1,2]))