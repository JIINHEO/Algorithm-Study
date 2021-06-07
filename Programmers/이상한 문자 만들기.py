def solution(s):

    s = s.split(' ')

    for i in range(len(s)):
        f = ""
        for j in range(0, len(s[i])):
            if j % 2 == 0:
                f += (s[i])[j].upper() # 대문자로 변환
            else:
                f += (s[i])[j].lower() # 소문자로 변환
        s[i] = f

    return ' '.join(s)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("try hello world"))
print(solution("hello"))
