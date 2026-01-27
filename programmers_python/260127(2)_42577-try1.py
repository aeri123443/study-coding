'''
42577. 전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''

def solution(phone_book):
    # 길이: {}
    hash_map = {}
    
    # 전부 해시에 담기
    for num in phone_book:
        l = len(num)
        if l not in hash_map:
            hash_map[l] = set()
        hash_map[l].add(num)
    # print(hash_map)

    # 해시 하나씩 돌면서 확인
    for v in phone_book:
        # print(k,v)
        for i in range(1, len(v)):
            if i not in hash_map:
                continue

            if v[:i] in hash_map[i]:
                return False

    return True
    

print()
print(solution(["119", "97674223", "1195524421"]))
print(False)

print()
print(solution(["123","456","789"]))
print(True)

print()
print(solution(["12","123","1235","567","88"]))
print(False)

# 최소최대
print()
print(solution(["1","123","1235","567","88"]))
print(False)

print()
print(solution(["3","123","125","567","88"]))
print(True)

print()
print(solution(["3"]))
print(True)

# 최소최대
# print()
# print(solution())
# print()