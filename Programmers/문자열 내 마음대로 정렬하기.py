def solution(strings, n):

    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for j in range(len(strings)):
        answer.append(strings[j][1:])

    return answer

    #return sorted(sorted(strings), key = lambda x: x[n])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))


#<다른 풀이>

def solution(strings, n):

    return sorted(sorted(strings), key = lambda x: x[n])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))
