def solution(arr, divisor):

    answer = []

    for i in range(len(arr)):
        if arr[i]%divisor == 0 :
            answer.append(arr[i])

    if len(answer) == 0 :
        return [-1]

    return sorted(answer)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([5, 9, 7, 10],5))
print(solution([2, 36, 1, 3],1))
print(solution([3,2,6],10))




# <다른 풀이>

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
