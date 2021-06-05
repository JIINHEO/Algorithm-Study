def solution(a, b):

    mul = a*b

    while b != 0 : #유클리드 호제법 (나머지가 0이 될때까지 나눠준다)
        temp = b
        b = a % b 
        a = temp

    return [a, int(mul/a)] #최소공배수는 두 수를 곱하고 최대공약수로 나눈다.


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, 12))

