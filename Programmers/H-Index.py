def solution(citations):
    citations.sort(reverse=True) #내림차순으로 정렬

    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations) # h보다 모두 큰 경우 인덱스 길이인 h를 반환


print(solution([3, 0, 6, 1, 5]))
