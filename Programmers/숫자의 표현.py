def solution(n):
    count = 0

    for i in range(1,n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n :
                count +=1
            elif sum > n :
                break;
    return count

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution(15))

