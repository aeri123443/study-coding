'''
42579. 베스트앨범
https://school.programmers.co.kr/learn/courses/30/lessons/42579

문제 분석: 7m 48s
코드 작성: 18m 34s
디버깅: 0m 0s
total: 26m 22s
'''

'''
장르 별로 가장 많이 재생된 노래를 두 개씩 모아
1 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
'''

from collections import defaultdict
from pprint import pprint

def solution(genres, plays):
    songs = defaultdict(list)
    totals = defaultdict(int)

    for i, [g, p] in enumerate(zip(genres, plays)):
        songs[g].append((-p, i))
        totals[g] += p
    # pprint(songs)
    # pprint(totals)

    genres_sorted = sorted(totals.items(), key=lambda x:-x[1])
    # print(genres_sorted)

    answer = []
    for g, _ in genres_sorted:
        if len(songs[g]) == 1:
            answer.append(songs[g][0][1])
        else:
            answer.extend([b for a, b in sorted(songs[g])[:2]])

    return answer

# [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
# [4, 1, 5, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop", "rock"],[500, 600, 150, 800, 2500, 2000]))
# [4, 1, 5, 0, 3]
print(solution(["classic", "pop", "classic", "classic", "pop", "rock"],[(500+800)//2, 600, 150, (500+800)//2, 2500, 2000]))
