def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) #numbers 를 string으로 변환
    numbers.sort(key=lambda x:x*3, reverse= True)
    answer = str(int(''.join(numbers)))
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([0,0,0,0]))
print(solution([3, 30, 34, 5, 9]))
