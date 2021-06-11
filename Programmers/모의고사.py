def solution(answers):
    result = []
    p = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    c1, c2, c3 = 0,0,0

    for i in range(len(answers)):
        s1, s2, s3 = i % len(p[0]) ,i % len(p[1]) ,i % len(p[2])

        if (p[0])[s1] == answers[i]:
            c1 +=1
        if (p[1])[s2] == answers[i]:
            c2 += 1
        if (p[2])[s3] == answers[i]:
            c3 += 1

    k = max(c1, c2, c3)
    result = []
    if k == c1:
        result.append(1)
    if k == c2:
        result.append(2)
    if k == c3:
        result.append(3)

    return result
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

