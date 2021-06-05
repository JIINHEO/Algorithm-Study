def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3))
