def solution(participant, completion):
    completion.sort()
    participant.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return  participant[-1]

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
