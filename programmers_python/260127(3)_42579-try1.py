'''
42579. lv3 베스트앨범
https://school.programmers.co.kr/learn/courses/30/lessons/42579
32m 09s
'''

from pprint import pprint
#  장르 별로 가장 많이 재생된 노래를 두 개씩

# 속한 노래가 많이 재생된 장르를 먼저 수록
    # 장르 내에서 많이 재생된 노래 먼저
    # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    # 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.

def solution(genres, plays):
    N = len(genres)
    genres_total = {}
    genres_plays = {}

    # 해시 채우기
    for i in range(N):
        g, p = genres[i], plays[i]

        if g not in genres_total:
            genres_total[g] = 0
            genres_plays[g] = []

        genres_total[g] += p
        genres_plays[g].append([i, p])


    # 장르 순위
    genres_total = sorted([[k,v] for k,v in genres_total.items()], key=lambda x:-x[1])

    # pprint(genres_plays)
    # pprint(genres_total)

    # 장르 별로 노래 담기
    answer = []
    for g, _ in genres_total:
        # print(g)
        # print(genres_plays[g])
        g_playlist = genres_plays[g]

        # 장르 내 노래가 하나일 경우
        if len(g_playlist) == 1:
            answer.append(g_playlist[0][0])
            continue

        g_playlist.sort(key=lambda x:(-x[1], x[0]))
        # print(g_playlist)
        answer.extend([g_playlist[0][0], g_playlist[1][0]])
    # answer = []
    return answer

print()
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print([4, 1, 3, 0])

# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
print()
print(solution(["classic", "pop", "classic", "classic", "classic", "pop"], [500, 600, 500, 150, 800, 2500]))
print([5,1,4,0])

# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
print()
print(solution(["classic", "pop", "classic", "classic", "classic"], [500, 2500, 500, 150, 500]))
print([1,0,2])

# 재생 횟수가 같은 노래 3개가 있다면?
print()
print(solution(["classic", "pop", "classic", "classic", "classic", "pop"], [500, 600, 500, 150, 500, 2500]))
print([5,1,0,2])
