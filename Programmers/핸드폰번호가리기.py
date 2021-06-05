def solution(phone_number):
  return '*' * (len(phone_number) - 4) + phone_number[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("01033334444"))
