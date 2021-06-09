def solution(a, b):
    if a > b: a, b = b, a
    sum = 0
    for i in range(b-a+1):
        sum += a
        a += 1

    return sum


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))



#<다른 코드>


def solution(a, b):
  
  if a > b: a, b = b, a
    
  return sum(range(a,b+1))
