'''
p.644 70. LCS 길이 계산하기
소요시간: 9m 45s
'''

def solution(str1, str2):
    n1, n2 = len(str1)+1, len(str2)+1
    ij_map = [[0]*n2 for _ in range(n1)]

    for i in range(1, n1):
        for j in range(1, n2):
            # print(i,j)
            # if i==5 and j==6: print(ij_map)
            if str1[i-1] == str2[j-1]:
                ij_map[i][j] = ij_map[i-1][j-1]+1
            else:
                ij_map[i][j] = max(ij_map[i-1][j], ij_map[i][j-1])
    
    return ij_map[-1][-1]
# 4
print(solution("ABCBDAB", "BDCAB"))
# 4
print(solution("AGGTAB", "GXTXAYB"))
