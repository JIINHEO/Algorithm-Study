def solution(arr):
    answer = []
    answer.append(arr[0])
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != answer[j]:
            answer.append(arr[i])
            j += 1
    return answer

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
