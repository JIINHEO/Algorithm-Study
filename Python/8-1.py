# 이것이 코딩 테스트다 with 파이썬

# 피보나치 함수 소스코드 8-1

# 피보나치 함수(Fibonacci Function)을 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo (x - 2)

print(fibo(4))


# <출력>
# 3
