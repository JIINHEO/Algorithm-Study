def solution(N, stages):

    fail_rate = {}
    total_user = len(stages)

    for i in range(1, N+1): # 5번 반복
        if total_user != 0: # 도달한 사람들
            fail_user = stages.count(i) # 도달하였지만 클리어하지 못함
            fail_rate[i] = fail_user/total_user #실패율
            total_user -= fail_user #이전 스테이지에 도달한 사람들을 빼줌
        else:
            fail_rate[i] = 0

    return sorted(fail_rate, key=lambda x:fail_rate[x], reverse=True) # 값을 내림 차순으로 정렬

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
