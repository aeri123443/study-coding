'''
p.676 79. 단어 퍼즐
https://school.programmers.co.kr/learn/courses/30/lessons/12983
1) DP: "n번째 글자까지 완성할 수 있는 최솟값을 계속 구함"
-> 2) 일전의 "직전까지 구했다는 전제 하에 끄트머리만 붙이는 경우의 수"를 떠올려야 함 (여기까진 함)
-> 3) 기본 경우의 수는 stars에 따라 끝의 2자리만 채우면 되는 경우, 1자리만 채우면 되는 경우... 이런식이 될 수 있음
-> 4) x자리만 채우면 되는 경우라면, (완성 문자 길이-x)자리의 최소경우+1을 해주면 되겠다!
-> 5) 그럼 그렇게 x자리를 채우면 되는 경우<에 해당하는 문자 조각이 strs에 있나 확인해보면 되겠구나!
'''
def solution(strs, t):
    N = len(t)
    arr = [float('inf')]*(N+1)
    arr[0]=0
    sizes = {len(x) for x in strs}

    for i in range(1, N+1):
        for size in sizes:
            if size <= i and t[i-size:i] in strs:
                arr[i] = min(arr[i], arr[i-size]+1)

    if arr[-1] == float('inf'):
        return -1
    else: return arr[-1]

# 3
print(solution(["ba","na","n","a"], "banana"))

# -1
print(solution(["ba","an","nan","ban","n"], "banana"))

# 2
print(solution(["app","ap","p","l","e","ple","pp"], "apple"))
