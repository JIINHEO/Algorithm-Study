def solution(arr):
    answer = 0
    
    for i in range(len(arr)):
        answer += arr[i]

    return (answer/len(arr))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1,2,3,4]))
