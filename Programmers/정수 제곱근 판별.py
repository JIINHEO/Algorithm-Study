def solution(n):
    for i in range(1, n+1):
        if i*i == n :
            return (i+1)*(i+1)
        elif i*i > n:
            return -1

    return n

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3))


# <다른 코드>
    sqrt = n ** (1 / 2)

    if sqrt % 1 == 0:
        return int((sqrt + 1) ** 2)
    return -1

    # 또는 한줄로 ->
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1
    
    # n ** (1/2)..🤭 생각도 못했네요
