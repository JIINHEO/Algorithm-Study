def solution(n):
    return list(map(int, (str(n)[::-1])))
  # 정수 n을 문자열로 변환하고 뒤집어 int형으로 저장합니다.


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(12345))
