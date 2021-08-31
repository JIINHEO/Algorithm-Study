def solution(A,B):

    A.sort()
    B.sort(reverse=True)
    result = 0

    for i in range(len(A)):
        result += int(A[i] * B[i])

    return result

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution([1,4,2],[5,4,4]))
