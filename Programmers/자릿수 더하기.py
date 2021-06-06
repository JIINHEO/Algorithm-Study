def solution(n):
    return sum(list(map(int, str(n)))) #문자열로 변환한 n을 list에 int형으로 저장한것을 sum합니다. 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(987))

