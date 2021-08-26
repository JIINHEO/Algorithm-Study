def solution(s):
    p = 0
    y = 0
    for i in range(len(s)):
        x = s[i]
        if x == 'p' or x == 'P':
            p += 1
        elif x == 'y' or x == 'Y':
            y += 1

    if p == y :
        return True
    elif p == 0 and y == 0 :
        return True
    else : return False

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution("pPoooyY"))
print(solution("Pyy"))
