def solution(seoul):

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["Jane","Kim"]))




#<다른 코드>
def solution(seoul):
  return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["Jane","Kim"]))
