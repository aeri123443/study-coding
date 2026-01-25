'''
60057. lv2 문자열 압축
https://school.programmers.co.kr/learn/courses/30/lessons/60057
'''

import sys
input = sys.stdin.readline

def solution(s):
    n = len(s)
    answer = float('inf')
    if n==1:
        return 1
    for gap in range(1, n//2+1):
        answer_arr = []
        # 단위: 1~1000
        target = s[0:gap]
        cnt = 1
        for i in range(gap,n,gap):
            tmp = s[i:i+gap]
            if target == tmp:
                cnt += 1
            else:
                # 문자열 붙이기
                # print(cnt, target)
                if cnt>1:
                    answer_arr.append(str(cnt))
                answer_arr.append(''.join(target))
                # 타겟 리셋
                target = s[i:i+gap]
                cnt = 1

        # 마지막 문자열 붙이기
        # print(cnt, target)
        if cnt>1:
            answer_arr.append(str(cnt))
        answer_arr.append(''.join(target))

        # 최소 문자열 크기 저장
        # print(gap, len( ''.join(answer_arr) ), ''.join(answer_arr) )
        answer = min(answer, len( ''.join(answer_arr) ))

    return answer

# 7
print(solution('aabbaccc'))

# 9
print(solution('ababcdcdababcdcd'))

# 8
print(solution('abcabcdede'))

# 14
print(solution('abcabcabcabcdededededede'))

# 17
print(solution('xababcdcdababcdcd'))

# 안 자르는게 제일 나은 경우
# 8
print(solution('abcdefgh'))

# 최소 케이스
print(solution('a'))
# 최대 케이스
print(solution('cksngjnqfkkrppdqkqodhqwluvtzmfhsobnrviouyrvdvaipodakciikneiwkwwpjbhieluotsagfopviwyujbzcowomwqdxrzxdlmgyywwvrlwxvdfrasehsxjwzsnzwftjurziwzcjwvtheekbaidhbpnaczkqayilffjiammgpykfgyueqafmfkyryyahljuodqewywrmxwxenlpxomjwobtcuolxhowjvrjzroytpcisomrscqundpeylsipokycovnxbyfqbdunjlbxhizllmqxilpqtmcosknokzaazbxulrzsqchvnejahessegluzeghzwcqodzrvzaekwqysaqhtgesyujajojaupzeytxwqykytxgwppasugujgbzekmsgmoqlcugjdflcqrpfbnjublqmlvxafsdpdaiptrdfjmtjlkqlzektbpbtlrppkhfqngsipkeatyqvbivpxrohuzvtjklyibahidrbckpkzxvqdwkwanguoykdoctevqmczoouynmfganarlmahmuspswlstjptvxdsnhakzvizffthkwyiihsacwongvpoofsyzqjkretpvavfejdoenpacfomgekbqdsfysgcbhaygfdfehtbpwatqrigkfijbvgyefwjlwerignllejaicjzmtskohrlygqyvcvueyuiianevexieqjigienatehqljglymsdcckhzaaravxvkvphjfohcgucswjyxpxjsxolvmuemogahercokuqtznudfqnxdkvgczyjepcrohymsxfyhrtgspxbjmucgaddmfrdkmbwvtfooptgiujetbqygmmerdgrlwmckxgbhpeilcxmkztodghjmpdfgvvwyixwjzkmrjlodsbjgosowslbxgwbwkngtidqecybrmhoeryqxkwiupiwiolluhzinmijraihwuwaabjkgfrhgdsuwzoyyxbfqgcxgmosgkacvtxirmcabrgyz'))