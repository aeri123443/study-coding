'''
p.575 60. 튜플
https://school.programmers.co.kr/learn/courses/30/lessons/64065
소요시간: 29m 37s

'''
def solution(s):
    # 문자열 분리
    arr1 = s[2:-2].split('},{')
    arr2 = []
    for a in arr1:
        arr2.append( set(map(int, a.split(','))))
    
    # 길이순 정렬
    arr2.sort(key=lambda x:len(x))
    # print(arr2)

    answer = [list(arr2[0])[0]]
    for i in range(1, len(arr2)):
        answer.append( list(arr2[i]-arr2[i-1])[0] )
        # print( arr2[i]-arr2[i-1] )
    return answer

# [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# [2, 1, 3, 4]
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# [111, 20]
print(solution("{{20,111},{111}}"))
# [123]
print(solution("{{123}}"))
# [3, 2, 4, 1]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
