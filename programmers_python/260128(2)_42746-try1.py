'''
42746. lv2 가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746
'''

def solution(numbers):

    hash_map = {}
    for number in numbers:
        number = str(number)
        tmp_str = number * (12//len(number))
        if tmp_str not in hash_map:
            hash_map[tmp_str] = []
        hash_map[tmp_str].append(number)
    # print(hash_map)

    sorted_list = sorted(hash_map.keys(), reverse=True)
    # print(sorted_list)

    answer = []
    for x in sorted_list:
        for y in hash_map[x]:
            # print(y)
            answer.append(y)

    # print(answer)
    for x in answer:
        if int(x) > 0:
            return ''.join(answer)

    return "0"

print()
print(solution([3, 30, 34, 5, 9]))
print("9534330")

print()
print(solution([6, 10, 2]))
print("6210")

print()
print(solution([0, 0, 0]))
print("0")

print()
print(solution([24, 3434, 34]))
print("34343424")

print()
print(solution([9, 99, 999]))
print("999999")

print()
print(solution([9]))
print("9")

print()
print(solution([0]))
print("0")

# print()
# print(solution([1000]*100000))

print()
print(solution([0]*100000))
print(0)