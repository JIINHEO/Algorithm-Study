#이것이 코딩테스트다. with 파이썬

#2가지 방식으로 구현한 팩토리얼 예제 5-5

def factorial_iterative(n): #반복문
    result = 1
    # 1부터 n 까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

#재귀적으로 구현한 n!
def factorial_recursive(n): #재귀
    if n <= 1: #n이 1이하인 경우 1을 반환
        return 1
    #n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

print('반복적으로 구혀:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
