def solution(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        prepre = 0
        pre = 1
        for i in range(2, n+1):
            fibo = pre + prepre
            prepre = pre
            pre = fibo

    return fibo % 1234567

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3))
print(solution(5))
