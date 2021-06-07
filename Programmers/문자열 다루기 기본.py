def solution(s):

    if len(s)==4 or len(s) == 6:
        for i in s:
            if 'a' <= i <= 'z':
                return False
        return True
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("a234"))
print(solution("1234"))



#<다른 코드>
def solution(s):
    return s.isdigit() and len(s) in (4, 6)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("a234"))
print(solution("1234"))
