def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        match = []
        for j in i:
            if j in skill:
                match.append(j)

        print(match)
        for k in range(len(match)):
            if match[k] != skill[k]:
                break
        else:
            answer +=1

    return answer


# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
