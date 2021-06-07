def solution(n):
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    return sum(a)
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(6))

# return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
