'''
p.572 59. 가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746
소요시간: 62m 15s
시간초과
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)

    arr = [numbers[0]]
    # for p로 포인터 이동
    for p in range(1,len(numbers)):
        target_num = numbers[p]
        max_num = int(''.join(arr))
        tmp_arr = [*arr]
        for i in range(len(arr)+1):
            tmp = [*arr[:i],target_num,*arr[i:]]
            if max_num < int(''.join(tmp)):
                max_num = int(''.join(tmp))
                tmp_arr = tmp
        # print(tmp_arr)
        arr = [*tmp_arr]
    # print(arr)

    return ''.join(arr)

# '9534330'
print(solution([3, 30, 34, 5, 9]))
# '6210'
print(solution([6, 10, 2]))
# '6111110'
print(solution([6, 110, 11, 1]))
# '6111100'
print(solution([1, 100, 11, 6]))
