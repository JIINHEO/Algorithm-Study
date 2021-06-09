def solution(s):

    if len(s) % 2 == 0 :
        return s[(len(s)-1)//2:(len(s)//2)+1]

    else:
        return s[len(s) // 2]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("abcde"))
print(solution("qwer"))



# <다른 풀이>
def solution(s):

  return s[(len(s)-1)//2:len(s)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("abcde"))
print(solution("qwer"))
