def solution(s, n):
    
    s_list = list(s)
    
    for i in range(len(s_list)):
        if (ord(s_list[i])) == 32: #공백
            continue
        elif 65<= ord(s_list[i])<=90 and (ord(s_list[i])+n) > 90: #대문자
            s_list[i] = chr(ord(s_list[i]) + n-26)
        elif 97<= ord(s_list[i])<=122 and (ord(s_list[i])+n) > 122: #소문자
            s_list[i] = chr(ord(s_list[i]) + n-26)
        else:
            s_list[i] = chr(ord(s_list[i]) + n)

    return ''.join(s_list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))




#<다른 코드>

def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if 'A' <= i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif 'a' <= i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else:
                answer += ' '
    return answer

