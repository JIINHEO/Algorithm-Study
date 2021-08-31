def solution(s):
    stack= []

    for i in s:
        if i == "(" :
            stack.append(i)
        else : # s[i] == ")"
            if len(stack) != 0 :
               stack.pop()
            else :
                return False

    if len(stack)==0: return True
    else: return False

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
