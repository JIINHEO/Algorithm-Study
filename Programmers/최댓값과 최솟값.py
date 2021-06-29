def solution(s): 
  s = sorted(list(map(int, s.split()))) 
  str = (f"{s[0]} {s[-1]}") 
  return str 

# 아래는 테스트를 위한 출력 코드입니다. 
print(solution("1 2 3 4")) 
print(solution("-1 2 3 -54"))
