def solution(s):
    return int(s[1:]) if s[0] == "-1" else int(s)
  # 문자열 첫번째가 "-1"일 경우 index 1부터 끝까지를 int 로 변환하여 반환하고,
  # 아닐경우 그대로 int로 변환하여 반환해라.

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("-1234"))

