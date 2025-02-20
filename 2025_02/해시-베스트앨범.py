# 장르 별로 가장 많이 재생된 노래를 두 개씩 모음
# 속한 노래가 많이 재생된 장르
# 장르 내에서 많이 재생된 노래
# 같은 장르에서 횟수가 같으면 고유 번호가 낮은 노래

# 1. 가장 많이 재생된 장르 순으로 정렬
# 2. 정렬된 장르 순회
# 2-1. 장르에서 가장 많이 재생된 노래 순서대로 2개 (1개면 1개)
# 2-2. 재생 횟수 같으면 고유 번호 낮은 노래 먼저


def solution(genres, plays):
    answer = []
    genre_dict = {}
    genre_playsum_dict = {}

    for i in range(len(genres)):
        if genres[i] in genre_dict.keys():
            genre_dict[genres[i]].append([plays[i], i])
            genre_playsum_dict[genres[i]] += plays[i]
        else:
            genre_dict[genres[i]] = [[plays[i], i]]
            genre_playsum_dict[genres[i]] = plays[i]

    sorting_buffer = []
    for k, v in genre_playsum_dict.items():
        sorting_buffer.append([v, k])
    sorting_buffer.sort()
    sorting_buffer.reverse()

    for [_, g] in sorting_buffer:
        genre_dict[g].sort()
        genre_dict[g].reverse()
        if len(genre_dict[g]) < 2:
            answer.append(genre_dict[g][0][1])
        else:
            if genre_dict[g][0][0] == genre_dict[g][1][0]:
                if genre_dict[g][0][1] > genre_dict[g][1][1]:
                    answer.append(genre_dict[g][1][1])
                    answer.append(genre_dict[g][0][1])
                    continue
            answer.append(genre_dict[g][0][1])
            answer.append(genre_dict[g][1][1])
    return answer
