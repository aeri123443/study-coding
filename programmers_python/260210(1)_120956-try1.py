'''
120956. lv0 옹알이(1)
https://school.programmers.co.kr/learn/courses/30/lessons/120956
'''

def solution(babbling):
    dic = { "aya", "ye", "woo", "ma" }
    answer = 0

    for word in babbling:
        # print(word)
        # word = list(word)
        i = j = 0
        # len_cnt = 0
        word_stack = []
        while j<len(word):
            # j-i가 2,3의 배수가 될때까지 j를 늘림
            l = j-i+1
            if l%2==0 or l%3==0:
                # print(i, j, word[i:j+1])
                if word[i:j+1] in dic:
                    if not word_stack or word_stack[-1]!=word[i:j+1]:
                        # len_cnt += l
                        word_stack.append(word[i:j+1])
                        # print(word[i:j+1])
                        i = j + 1
            j += 1
        # print(len_cnt)
        if word == ''.join(word_stack):
            # print('good', word)
            answer += 1
        # else:
            # print('nope')

    return answer

print()
print(solution(["aya", "yee", "u", "maa"]))
print(1)

print()
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(2)