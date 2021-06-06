def solution(num):
    count = 0
    
    while(num > 1): # num이 1보다 클 경우 반복
        count += 1  # count +1
        
        if num%2 == 0 : # 짝수일 경우 /2
            num /= 2
        else:           # 홀수일 경우 *3+1
            num = num*3+1

        if count == 500: # Count가 500이 채워지면 -1을 반환
            return -1
    return count

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(16))
