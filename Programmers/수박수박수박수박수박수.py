def solution(n):
    s=""
    
    for i in range(1, n+1):
        if i%2==1:
            s += "수"
        else:
            s += "박"
            
    return s

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(4))



#<다른 코드>
  return "수박"*(n//2) + "수"*(n%2)
