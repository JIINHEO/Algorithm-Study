def solution(x):
     n = list(map(int, str(x)))
     sum = 0
     for i in range(len(n)):
         sum += n[i]

     if x % sum == 0 :
         return True
     else:
         return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(12))



# 오 이렇게 한 줄로도 가능하군요 ! 🤩

# def solution(x):
#     return x % sum(list(map(int, str(x)))) == 0

# 정수의 각 자릿수를 합하기 위해 list 로 나눠줬습니다. 
# (이전 문제에서 바보같이.. 배열을 사용해서 나눴기 때문에😓 이번엔 list 를 사용했습니다.!!)
